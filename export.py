import sqlite3
import csv
import tkinter as tk
from tkinter import filedialog

def export_to_csv(status_label):
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    
    if not file_path:
        status_label.config(text="Export canceled.")
        return

    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user")
    rows = cursor.fetchall()
    conn.close()

    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "First Name", "Last Name", "Country", "City", "Email", "Phone"])
        writer.writerows(rows)

    status_label.config(text="Records exported successfully to CSV.")
