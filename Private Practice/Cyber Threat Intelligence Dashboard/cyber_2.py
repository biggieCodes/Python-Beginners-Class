
# Top frame for buttons and filter
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
import os
import random
from datetime import datetime
import matplotlib.pyplot as plt
from collections import Counter
import threading
import requests  # Added import for fetching real-time threat data
import time
# Create main window
root = tk.Tk()
root.title("Cyber Threat Intelligence Dashboard")
root.geometry("800x600")  # Increased window size for better display
root.config(bg="#1e1e1e")

title = tk.Label(root, text="🛡 Cyber Threat Intelligence Dashboard",
                font=("Helvetica", 18, "bold"), fg="#00ffcc", bg="#1e1e1e")
title.pack(pady=10)

# === AlienVault OTX Threat Fetching ===
OTX_API_KEY = "7b92ae4fd7169949aee933c7086156c3110381f077ac906ccaaaa5ca3f633ae5"  # Real API key
OTX_ENDPOINT = "https://otx.alienvault.com/api/v1/pulses/subscribed"

def fetch_threat_data():
    headers = {
        "X-OTX-API-KEY": OTX_API_KEY
    }

    try:
        response = requests.get(OTX_ENDPOINT, headers=headers)
        response.raise_for_status()
        data = response.json()

        # Clear existing logs
        tree.delete(*tree.get_children())

        # Insert top 10 threats
        for pulse in data.get("results", [])[:10]:
            timestamp = pulse.get("modified", "N/A")
            threat_type = pulse.get("name", "Unknown")
            source_ip = pulse.get("author_name", "AlienVault")
            severity = "High" if "ransomware" in threat_type.lower() else "Medium"

            tree.insert("", "end", values=(timestamp, threat_type, source_ip, severity))

        status_label.config(text="✅ Live Threat Data Fetched from OTX")

    except Exception as E:
        messagebox.showerror("Fetch Error", f"Failed to fetch real-time data:\n{E}")

# Export Logs function
def export_logs():
    if not tree.get_children():
        messagebox.showinfo("Export", "No logs to export.")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV files", "*.csv")],
        title="Save threat logs as CSV"
    )

    if file_path:
        try:
            with open(file_path, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Timestamp", "Threat Type", "Source IP", "Severity"])
                for child in tree.get_children():
                    writer.writerow(tree.item(child)["values"])
            messagebox.showinfo("Export", f"Logs successfully saved to:\n{file_path}")
        except Exception as e:
            messagebox.showerror("Export Error", f"An error occurred while exporting:\n{e}")

# Clear logs function
def clear_logs():
    confirm = messagebox.askyesno("Clear Logs", "Are you sure you want to clear all logs?")
    if confirm:
        for item in tree.get_children():
            tree.delete(item)
        status_label.config(text="🟢 Logs cleared. System ready.")

# Load logs from file
def load_logs_from_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("CSV files", "*.csv")],
        title="Select Threat Log CSV"
    )
    if not file_path:
        return

    try:
        tree.delete(*tree.get_children())  # Clear existing logs
        with open(file_path, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                log = (row["Timestamp"], row["Threat Type"], row["Source IP"], row[" Severity"])
                tree.insert("", "end", values=log)
        status_label.config(text="✅ Logs loaded from file.")
    except Exception as e:
        messagebox.showerror("Load Error", f"Failed to load logs:\n{e}")

# Apply filter for severity
def apply_filter():
    selected_filter = severity_var.get()
    if selected_filter == "All":
        for item in tree.get_children():
            tree.see(item)  # Show all items
    else:
        items = tree.get_children()
        for item in items:
            if tree.item(item)['values'][3] == selected_filter:
                tree.see(item)
            else:
                tree.hide(item)

# Show chart for severity distribution
def show_severity_chart():
    severities = []
    for item in tree.get_children():
        log_data = tree.item(item)["values"]
        if len(log_data) == 4:
            severities.append(log_data[3])

    if not severities:
        messagebox.showinfo("No Data", "No logs to display in the chart.")
        return

    count = Counter(severities)
    labels = list(count.keys())
    values = list(count.values())

    plt.figure(figsize=(6, 4))
    bars = plt.bar(labels, values, color=["green", "orange", "red", "purple"])
    plt.title("Threat Severity Distribution")
    plt.xlabel("Severity Level")
    plt.ylabel("Number of Threats")

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, height, f'{int(height)}', ha='center', va='bottom')

    plt.tight_layout()
    plt.show()

# Top frame for buttons and filter
top_frame = tk.Frame(root, bg="#1e1e1e")
top_frame.pack(fill=tk.X, padx=20, pady=(10, 0))

# Buttons
export_btn = tk.Button(top_frame, text="Export Logs", bg="#333", fg="white", command=export_logs)
export_btn.pack(side=tk.RIGHT, padx=5)

clear_btn = tk.Button(top_frame, text="Clear Logs", bg="#333", fg="white", command=clear_logs)
clear_btn.pack(side=tk.RIGHT, padx=5)

chart_btn = tk.Button(top_frame, text="Show Severity Chart", bg="#333", fg="white", command=show_severity_chart)
chart_btn.pack(side=tk.RIGHT, padx=5)

load_btn = tk.Button(top_frame, text="Load Logs", bg="#333", fg="white", command=load_logs_from_file)
load_btn.pack(side=tk.RIGHT, padx=5)

# Add the new Fetch Threat Data button
api_btn = tk.Button(top_frame, text="Fetch Threat Data", bg="#333", fg="white", command=fetch_threat_data)
api_btn.pack(side=tk.RIGHT, padx=5)

# Filter
severity_options = ["All", "Low", "Medium", "High", "Critical"]
severity_var = tk.StringVar()
severity_var.set("All")  # default value
filter_menu = ttk.Combobox(top_frame, textvariable=severity_var, values=severity_options, state="readonly")
filter_menu.pack(side=tk.LEFT, padx=(0, 10))
filter_btn = tk.Button(top_frame, text="Apply Filter", bg="#333", fg="white", command=apply_filter)
filter_btn.pack(side=tk.LEFT)

# Threat logs table setup
log_frame = tk.Frame(root, bg="#1e1e1e")
log_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

columns = ("timestamp", "threat_type", "source_ip", "severity")
tree = ttk.Treeview(log_frame, columns=columns, show="headings", height=15)
tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(log_frame, orient="vertical", command=tree.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tree.configure(yscrollcommand=scrollbar.set)

tree.heading("timestamp", text="Timestamp")
tree.heading("threat_type", text="Threat Type")
tree.heading("source_ip", text="Source IP")
tree.heading("severity", text="Severity")

tree.column("timestamp", width=150)
tree.column("threat_type", width=200)
tree.column("source_ip", width=150)
tree.column("severity", width=100)

status_label = tk.Label(root, text="🟢 System Ready", font=("Arial", 12), bg="#1e1e1e", fg="white")
status_label.pack(pady=5)

# Simulate threat logs (for testing)
threat_types = ["Brute Force Attack", "Phishing Attempt", "DDoS Attack", "SQL Injection", "Malware Detected"]
def generate_ip():
    return f"{random.randint(10, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"

def generate_threat():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    threat = random.choice(threat_types)
    ip = generate_ip()
    severity = random.choice(["Low", "Medium", "High", "Critical"])
    return (timestamp, threat, ip, severity)

def insert_threat_log():
    while True:
        log = generate_threat()
        selected_filter = severity_var.get()
        if selected_filter == "All" or log[3] == selected_filter:
            root.after(0, lambda log=log: tree.insert("", "end", values=log))
            root.after(0, lambda: status_label.config(text=f"⚠️ {log[3]} Threat Detected!"))
        time.sleep(random.randint(2,5))

thread = threading.Thread(target=insert_threat_log, daemon=True)
thread.start()

root.mainloop()
