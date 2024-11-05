import sqlite3
import tkinter as tk
from tkinter import scrolledtext

def display_all_records(status_label, window):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        status_label.config(text="No records available.")
        return

    display_window = tk.Toplevel()
    display_window.title("All Records")
    text_area = scrolledtext.ScrolledText(display_window, wrap=tk.WORD, width=80, height=20)
    text_area.pack()

    for row in rows:
        record_text = f"ID: {row[0]}, Name: {row[1]} {row[2]}, Country: {row[3]}, City: {row[4]}, Email: {row[5]}, Phone: {row[6]}\n"
        text_area.insert(tk.END, record_text + "\n")

    text_area.config(state=tk.DISABLED)
