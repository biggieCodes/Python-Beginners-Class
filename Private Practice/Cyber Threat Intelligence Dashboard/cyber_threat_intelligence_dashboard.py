# This code creates a simple Cyber Threat Intelligence Dashboard using Tkinter.

import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("Cyber Threat Intelligence Dashboard")
root.geometry("700x500")
root.config(bg="#1e1e1e")  # dark mode vibes

# Title
title = tk.Label(root, text="🛡 Cyber Threat Intelligence Dashboard", 
                 font=("Helvetica", 18, "bold"), fg="#00ffcc", bg="#1e1e1e")
title.pack(pady=10)

# Top frame for filter and export
top_frame = tk.Frame(root, bg="#1e1e1e")
top_frame.pack(fill=tk.X, padx=20)

# Filter dropdown
filter_label = tk.Label(top_frame, text="Filter by Severity:", fg="white", bg="#1e1e1e")
filter_label.pack(side=tk.LEFT, padx=5)

severity_options = ["All", "Low", "Medium", "High", "Critical"]
severity_var = tk.StringVar()
severity_var.set("All")  # default value

filter_menu = ttk.Combobox(top_frame, textvariable=severity_var, values=severity_options, state="readonly")
filter_menu.pack(side=tk.LEFT, padx=5)

# Export button
export_btn = tk.Button(top_frame, text="Export Logs", bg="#333", fg="white")
export_btn.pack(side=tk.RIGHT, padx=5)

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




