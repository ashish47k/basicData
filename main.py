import sqlite3
import tkinter as tk
from delete import handle_delete
from insert import handle_insert
from fields import create_fields
from view import view_records
from update import handle_update
from search import handle_search
from display_all import display_all_records
from export import export_to_csv
from data_statistics import show_statistics

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

# Create insert 
button_insert = tk.Button(window, text="Insert", command=lambda: handle_insert(first_name, last_name, country, city, email, phone, status_label, window))
button_insert.pack()

#Create delete buttons
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

#Update button
label_update_id = tk.Label(window, text="Update record with ID:")
label_update_id.pack()
entry_update_id = tk.Entry(window)
entry_update_id.pack()
button_update = tk.Button(window, text="Update", command=lambda: handle_update(entry_update_id, first_name, last_name, country, city, email, phone, status_label, window))
button_update.pack()


# Search functionality
label_search = tk.Label(window, text="Search by:")
label_search.pack()
search_options = ["First Name", "Last Name", "Country", "City", "Email", "Phone"]
search_var = tk.StringVar(window)
search_var.set(search_options[0])
search_menu = tk.OptionMenu(window, search_var, *search_options)
search_menu.pack()
entry_search = tk.Entry(window)
entry_search.pack()
button_search = tk.Button(window, text="Search", command=lambda: handle_search(entry_search, search_var.get(), status_label, window))
button_search.pack()

# Display all records button
button_display_all = tk.Button(window, text="Display All Records", command=lambda: display_all_records(status_label, window))
button_display_all.pack()

# Export to CSV button
button_export = tk.Button(window, text="Export to CSV", command=lambda: export_to_csv(status_label))
button_export.pack()

# Show statistics button
button_statistics = tk.Button(window, text="Show Statistics", command=lambda: show_statistics(status_label, window))
button_statistics.pack()


# Create a label for displaying status messages
status_label = tk.Label(window, text="")
status_label.pack()


# Start the Tkinter event loop
window.mainloop()

# Close the connection
conn.close()