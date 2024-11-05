import sqlite3
import tkinter as tk

def handle_search(entry_field, search_by, status_label, window):
    query = entry_field.get().strip()
    
    # Mapping of display names to actual column names
    column_mapping = {
        "First Name": "first_name",
        "Last Name": "last_name",
        "Country": "country",
        "City": "city",
        "Email": "email",
        "Phone": "phone"
    }

    # Get the actual column name
    search_column = column_mapping.get(search_by)
    
    if not search_column:
        status_label.config(text="Invalid search field selected.")
        return

    # Connect to database and perform search
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM user WHERE {search_column} LIKE ?", (f"%{query}%",))
    rows = cursor.fetchall()
    conn.close()

    if rows:
        result_window = tk.Toplevel()
        result_window.title("Search Results")
        for row in rows:
            result_text = f"ID: {row[0]}, Name: {row[1]} {row[2]}, Country: {row[3]}, City: {row[4]}, Email: {row[5]}, Phone: {row[6]}"
            label_result = tk.Label(result_window, text=result_text)
            label_result.pack()
    else:
        status_label.config(text=f"No records found for {search_by} containing '{query}'.")

    entry_field.delete(0, tk.END)
