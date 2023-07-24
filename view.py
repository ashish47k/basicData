import sqlite3
import tkinter as tk

def view_records(entry_id,status_label, window):
     # Check ID from the entry field
    try:
        id = int(entry_id.get())
    except ValueError:
        status_label.config(text="Invalid ID.")
        return

    #Connect to database for the record with the given ID
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user WHERE id = ?", (id,))
    row = cursor.fetchone()
    conn.close()

    if row is None:
        status_label.config(text=f"No record found with ID {id}.")
    else:
        #Display record it in a new window
        window = tk.Toplevel()
        window.title(f"Record with ID {id}")

        label_id = tk.Label(window, text=f"ID: {row[0]}")
        label_id.pack()

        label_name = tk.Label(window, text=f"Name: {row[1]}")
        label_name.pack()

        label_country = tk.Label(window, text=f"Country: {row[2]}")
        label_country.pack()

        label_city = tk.Label(window, text=f"City: {row[3]}")
        label_city.pack()

        label_email = tk.Label(window, text=f"Email: {row[4]}")
        label_email.pack()

        label_phone = tk.Label(window, text=f"Phone: {row[5]}")
        label_phone.pack()


    # Update the status label and clear the field
    status_label.config(text="")
    entry_id.delete(0, tk.END)