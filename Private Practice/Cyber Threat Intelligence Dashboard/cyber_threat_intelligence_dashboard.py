# This code creates a simple Cyber Threat Intelligence Dashboard using Tkinter.

import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os
import requests
from datetime import datetime
from tkinter import messagebox, filedialog
import matplotlib.pyplot as plt
from collections import Counter




# Create main window
root = tk.Tk()
root.title("Cyber Threat Intelligence Dashboard")
root.geometry("700x500")
root.config(bg="#1e1e1e")  # dark mode vibes

# Title
title = tk.Label(root, text="🛡 Cyber Threat Intelligence Dashboard", 
                 font=("Helvetica", 18, "bold"), fg="#00ffcc", bg="#1e1e1e")
title.pack(pady=10)


import tkinter as tk

# Function to fetch threat data
def fetch_threat_data():
    print("Fetching threat data...")
fetch_threat_data()

# Create main window
root = tk.Tk()
root.title("Cyber Threat Intelligence Dashboard")

# Create top frame
top_frame = tk.Frame(root)
top_frame.pack(pady=10)

# Create button
api_btn = tk.Button(top_frame, text="Fetch Threat Data", bg="#333", fg="white", command=fetch_threat_data)
api_btn.pack()

def load_logs_from_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("CSV files", "*.csv")],
        title="Select Threat Log CSV"
    )
    messagebox.showerror("Load Error", f"Failed to load logs:\n{Exception}")
    load_btn = tk.Button(top_frame, text="Load Logs", bg="#333", fg="white", command=load_logs_from_file)
    load_btn.pack(side=tk.RIGHT, padx=8)

def clear_logs():
    confirm = messagebox.askyesno("Clear Logs", "Are you sure you want to clear all logs?")
    if confirm:
        for item in tree.get_children():
            tree.delete(item)
        status_label.config(text="🟢 Logs cleared. System ready.")
        messagebox.showinfo("Clear Logs", "All logs have been cleared.")


def export_logs():
    print("Exporting logs...")

root = tk.Tk()
root.title("Log Exporter")

frame = tk.Frame(root)
frame.pack(pady=10)

#export_button = tk.Button(frame, text="Export Logs", command=export_logs)
#export_button.pack()

root.mainloop()

def show_severity_chart():
    print("Showing severity chart...")

chart_btn = tk.Button(top_frame, text="Show Severity Chart", bg="#333", fg="white", command=show_severity_chart)
chart_btn.pack(side=tk.RIGHT, padx=10, pady=5)

chart_btn = tk.Button(top_frame, text="Show Severity Chart", bg="#333", fg="white", command=show_severity_chart)
chart_btn.pack(side=tk.RIGHT, padx=10, pady=5)
# For macOS: Play the "Glass" system sound (you can change it to any sound file you like)

root = tk.Tk()
top_frame = tk.Frame(root)
top_frame.pack()

api_btn = tk.Button(top_frame, text="Fetch Threat Data", bg="#333", fg="white", command=fetch_threat_data)
api_btn.pack()

os.system("afplay /System/Library/Sounds/Glass.aiff")

# === Export Logs to CSV ===
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

# === Clear All Logs from Table ===
def clear_logs():
    confirm = messagebox.askyesno("Clear Logs", "Are you sure you want to clear all logs?")
    if confirm:
        for item in tree.get_children():
            tree.delete(item)
        status_label.config(text="🟢 Logs cleared. System ready.")
        messagebox.showinfo("Clear Logs", "All logs have been cleared.")

    def load_logs_from_file():
        file_path = filedialog.askopenfilename(
            filetypes=[("CSV files", "*.csv")],
            title="Select Threat Log CSV"
        )
        if not file_path:
            return

    file_path = "path/to/file.csv"  # Replace "path/to/file.csv" with the actual file path
    try:
        with open(file_path, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if "Timestamp" in row and "Threat Type" in row and "Source IP" in row and "Severity" in row:
                    log = (row["Timestamp"], row["Threat Type"], row["Source IP"], row["Severity"])
                    tree.insert("", "end", values=log)

        status_label.config(text="✅ Logs loaded from file.")
    except Exception as e:
        messagebox.showerror("Load Error", f"Failed to load logs:\n{e}")

# === Top Frame for Buttons ===
top_frame = tk.Frame(root, bg="#222", pady=10)
top_frame.pack(fill=tk.X)


# Button to load logs from CSV
load_btn = tk.Button(top_frame, text="Load Logs", bg="#333", fg="white", )
load_btn.pack(side=tk.RIGHT, padx=8)
messagebox.showinfo("Clear Logs", "All logs have been cleared.")

# Top frame for filter and export
top_frame = tk.Frame(root, bg="#1e1e1e")
top_frame.pack(fill=tk.X, padx=20)

export_btn = tk.Button( text="Export Logs", bg="#333", fg="white", command=export_logs)
export_btn.pack(side=tk.RIGHT, padx=5)

clear_btn = tk.Button(top_frame, text="Clear Logs", bg="#333", fg="white", command=clear_logs)
clear_btn.pack(side=tk.RIGHT, padx=5)


import matplotlib.pyplot as plt
from collections import Counter

def show_severity_chart():
    severities = []

    for item in tree.get_children():
        log_data = tree.item(item)["values"]
        if len(log_data) == 4:
            severities.append(log_data[3])  # Index 3 is Severity

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


# Button to show severity chart
chart_btn = tk.Button(top_frame, text="Show Severity Chart", bg="#333", fg="white", command=show_severity_chart)
chart_btn.pack(side=tk.RIGHT, padx=5)



# Clear logs button



#clear_btn = tk.Button(top_frame, text="Clear Logs", bg="#333", fg="white")
#clear_btn.pack(side=tk.RIGHT, padx=5)

# Filter dropdown
filter_label = tk.Label(top_frame, text="Filter by Severity:", fg="white", bg="#1e1e1e")
filter_label.pack(side=tk.LEFT, padx=5)

severity_options = ["All", "Low", "Medium", "High", "Critical"]
severity_var = tk.StringVar()
severity_var.set("All")  # default value

filter_menu = ttk.Combobox(top_frame, textvariable=severity_var, values=severity_options, state="readonly")
filter_menu.pack(side=tk.LEFT, padx=5)


# Threat logs table
log_frame = tk.Frame(root)
log_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

columns = ("timestamp", "threat_type", "source_ip", "severity")
tree = ttk.Treeview(log_frame, columns=columns, show="headings", height=15)
tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Scrollbar for table
scrollbar = ttk.Scrollbar(log_frame, orient="vertical", command=tree.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tree.configure(yscrollcommand=scrollbar.set)

# Set column headers
tree.heading("timestamp", text="Timestamp")
tree.heading("threat_type", text="Threat Type")
tree.heading("source_ip", text="Source IP")
tree.heading("severity", text="Severity")

# Set column width
for col in columns:
    tree.column(col, width=150)

# Status area
status_label = tk.Label(root, text="🟢 System Ready", font=("Arial", 12), bg="#1e1e1e", fg="white")
status_label.pack(pady=5)

import threading
import time
import random
from datetime import datetime

# Threat sample data
threat_types = ["Brute Force Attack", "Phishing Attempt", "DDoS Attack", "SQL Injection", "Malware Detected"]
severities = ["Low", "Medium", "High", "Critical"]

# Function to simulate source IP
def generate_ip():
    return f"{random.randint(10, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"

# Function to generate random threat log
def generate_threat():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    threat = random.choice(threat_types)
    ip = generate_ip()
    severity = random.choice(severities)
    return (timestamp, threat, ip, severity)

# Function to insert threat log into the table
def insert_threat_log():
    while True:
        log = generate_threat()

        # Filter check
        selected_filter = severity_var.get()
        if selected_filter == "All" or log[3] == selected_filter:
            # Add log to GUI in main thread
            root.after(0, lambda log=log: tree.insert("", "end", values=log))
            root.after(0, lambda: status_label.config(text=f"⚠️ {log[3]} Threat Detected!"))

        time.sleep(random.randint(2, 4))  # simulate delay between threats

# Run threat simulation in background thread
thread = threading.Thread(target=insert_threat_log, daemon=True)
thread.start()


# Run the app
root.mainloop()



