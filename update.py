import sqlite3
import tkinter as tk
import re

def handle_update(entry_id, entry_first_name, entry_last_name, entry_country, entry_city, entry_email, entry_phone, status_label, window):
    record_id = entry_id.get().strip()
    first_name = entry_first_name.get().strip()
    last_name = entry_last_name.get().strip()
    country = entry_country.get().strip()
    city = entry_city.get().strip()
    email = entry_email.get().strip()
    phone = entry_phone.get().strip()

    try:
        int(record_id)
    except ValueError:
        status_label.config(text="Invalid ID.")
        return

    # Validation (same as insert.py)
    name_pattern = r"^[A-Za-z]+$"
    email_pattern = r"^[^@]+@[^@]+\.[^@]+$"
    phone_pattern = r"^\d{10}$"

    if not re.match(name_pattern, first_name):
        status_label.config(text="Invalid input: First name must contain only letters.")
        return
    if not re.match(name_pattern, last_name):
        status_label.config(text="Invalid input: Last name must contain only letters.")
        return
    if not re.match(name_pattern, country):
        status_label.config(text="Invalid input: Country name must contain only letters.")
        return
    if not re.match(name_pattern, city):
        status_label.config(text="Invalid input: City name must contain only letters.")
        return
    if not re.match(email_pattern, email):
        status_label.config(text="Invalid input: Please enter a valid email address.")
        return
    if not re.match(phone_pattern, phone):
        status_label.config(text="Invalid input: Phone number must be exactly 10 digits.")
        return

    # Update the record in the database
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE user SET first_name = ?, last_name = ?, country = ?, city = ?, email = ?, phone = ? WHERE id = ?", (first_name, last_name, country, city, email, phone, record_id))
    conn.commit()
    conn.close()

    # Update status
    status_label.config(text=f"Record with ID {record_id} updated successfully.")

    # Clear entries
    entry_id.delete(0, tk.END)
    entry_first_name.delete(0, tk.END)
    entry_last_name.delete(0, tk.END)
    entry_country.delete(0, tk.END)
    entry_city.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_phone.delete(0, tk.END)

    # Reset the status label after 5 seconds
    window.after(5000, lambda: status_label.config(text=""))
