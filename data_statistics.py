import sqlite3
import tkinter as tk

def show_statistics(status_label, window):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM user")
    total_records = cursor.fetchone()[0]

    cursor.execute("SELECT country, COUNT(*) as count FROM user GROUP BY country ORDER BY count DESC LIMIT 1")
    common_country = cursor.fetchone()
    common_country = common_country[0] if common_country else "N/A"

    stats_window = tk.Toplevel()
    stats_window.title("Data Statistics")
    
    label_total = tk.Label(stats_window, text=f"Total Records: {total_records}")
    label_total.pack()

    label_country = tk.Label(stats_window, text=f"Most Common Country: {common_country}")
    label_country.pack()

    conn.close()
