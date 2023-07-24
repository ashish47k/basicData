import tkinter as tk
      
def create_fields(window):
    # Create labels and entries for the fields
    label_first_name = tk.Label(window, text="FirstName:")
    label_first_name.pack()
    first_name = tk.Entry(window)
    first_name.pack()

    label_last_name = tk.Label(window, text="LastName:")
    label_last_name.pack()
    last_name = tk.Entry(window)
    last_name.pack()

    label_country = tk.Label(window, text="Country:")
    label_country.pack()
    country = tk.Entry(window)
    country.pack()    

    label_city = tk.Label(window, text="City:")
    label_city.pack()
    city = tk.Entry(window)
    city.pack()

    label_email = tk.Label(window, text="Email:")
    label_email.pack()
    email = tk.Entry(window)
    email.pack()

    label_phone = tk.Label(window, text="Phone:")
    label_phone.pack()
    phone = tk.Entry(window)
    phone.pack()


    return first_name, last_name, country, city, email, phone