import sqlite3
import tkinter as tk
from delete import handle_delete
from insert import handle_insert
from fields import create_fields
from view import view_records


# Create a SQLite database and table
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user
    (id INTEGER PRIMARY KEY NOT NULL,
     first_name TEXT NOT NULL,
     last_name TEXT NOT NULL,
     country TEXT NOT NULL,
     city TEXT NOT NULL,
     email TEXT NOT NULL,
     phone TEXT NOT NULL);
''')
conn.commit()


# Create a Tkinter window
window = tk.Tk()
window.title("Database Editor")

# Create fields for the name and email inputs
first_name, last_name, country, city, email, phone = create_fields(window)

# Create insert and delete buttons
button_insert = tk.Button(window, text="Insert", command=lambda: handle_insert(first_name, last_name, country, city, email, phone, status_label, window))
button_insert.pack()

label_id = tk.Label(window, text="Delete record with ID:")
label_id.pack()
entry_id = tk.Entry(window)
entry_id.pack()

button_delete = tk.Button(window, text="Delete", command=lambda: handle_delete(entry_id, status_label,window))
button_delete.pack()

#Create view buttons
label_id = tk.Label(window, text="View record with ID:")
label_id.pack()
entry_id = tk.Entry(window)
entry_id.pack()

button_view = tk.Button(window, text="View", command=lambda: view_records(entry_id, status_label,window))
button_view.pack()

# Create a label for displaying status messages
status_label = tk.Label(window, text="")
status_label.pack()


# Start the Tkinter event loop
window.mainloop()

# Close the connection
conn.close()