import sqlite3
import tkinter as tk

def handle_delete(entry_id, status_label, window):
    # Get the record ID to delete
    try:
        record_id = entry_id.get().strip()
    except ValueError:
        status_label.config(text="Invalid ID.")
        return
    print("THis is " +record_id)
    # Delete the record from the database
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM user WHERE id = ?", (record_id,))
    conn.commit()
    conn.close()

    
    # Update the status label
    status_label.config(text=f"Record with ID {record_id} deleted successfully.")

    # Clear the record ID entry field
    entry_id.delete(0, tk.END)

    # Reset the status label after 5 seconds
    window.after(5000, lambda: status_label.config(text=""))
