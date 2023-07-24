import sqlite3
import tkinter as tk
import re

def handle_insert(entry_first_name, entry_last_name, entry_country, entry_city, entry_email, entry_phone, status_label, window):
    # Get the values from the entry fields
    print(entry_first_name)
    first_name = entry_first_name.get().strip()
    last_name = entry_last_name.get().strip()
    country = entry_country.get().strip()
    city = entry_city.get().strip()
    email = entry_email.get().strip()
    phone = entry_phone.get().strip()
    print(first_name)
    
    # Regular expressions for validation
    name_pattern = r"^[A-Za-z]+$"
    email_pattern = r"^[^@]+@[^@]+\.[^@]+$"
    phone_pattern = r"^\d{10}$"

    # Validate the input for each field
    if not re.match(name_pattern, first_name):
        status_label.config(text="First name must only contain letters.")
        return
    if not re.match(name_pattern, last_name):
        status_label.config(text="Last name must only contain letters.")
        return
    if not re.match(name_pattern, country):
        status_label.config(text="Country name must only contain letters.")
        return
    if not re.match(name_pattern, city):
        status_label.config(text="City name must only contain letters.")
        return
    if not re.match(email_pattern, email):
        status_label.config(text="Invalid email format.")
        return
    if not re.match(phone_pattern, phone):
        status_label.config(text="Phone number must be 10 digits.")
        return

    # Insert the record into the database
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user (first_name, last_name, country, city, email, phone) VALUES (?, ?, ?, ?, ?, ?)", (first_name, last_name, country, city, email, phone))
    user_id = cursor.lastrowid  # Get the id of the newly inserted record
    conn.commit()
    conn.close()

    # Update the status label
    status_label.config(text=f"Record of {first_name} {last_name} inserted successfully.")

    # Clear the entry fields
    entry_first_name.delete(0, tk.END)
    entry_last_name.delete(0, tk.END)
    entry_country.delete(0, tk.END)
    entry_city.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_phone.delete(0, tk.END)

    # Reset the status label and remove the image after 5 seconds
    window.after(1000, lambda: status_label.config(text=""))

