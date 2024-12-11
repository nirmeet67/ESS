import tkinter as tk
from tkinter import messagebox, ttk
import re
from database import create_database, add_user

def submit_form():
    # Retrieve the data from the form
    first_name = entry_first_name.get().strip()
    last_name = entry_last_name.get().strip()
    enrollment_number = entry_enrollment_number.get().strip()
    studying_year = entry_studying_year.get().strip()
    studying_sem = entry_studying_sem.get().strip()
    email_id = entry_email_id.get().strip()
    phone_number = entry_phone_number.get().strip()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()

    # Validations
    if not first_name or not last_name or not enrollment_number or not studying_year or not studying_sem or not email_id or not phone_number or not password or not confirm_password:
        messagebox.showerror("Error", "All fields are required!")
        return

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
        return

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email_id):
        messagebox.showerror("Error", "Invalid email format!")
        return

    if not phone_number.isdigit() or len(phone_number) < 10:
        messagebox.showerror("Error", "Phone number must be at least 10 digits and contain only numbers!")
        return

    # Save user data to the database
    if add_user(first_name, last_name, enrollment_number, studying_year, studying_sem, email_id, phone_number, password):
        messagebox.showinfo("Success", "Signup successful!")
    else:
        messagebox.showerror("Error", "User  with this enrollment number or email already exists.")

# Create the main window
root = tk.Tk()
root.title("Student Signup")

# Create and place labels and entry fields
tk.Label(root, text="First Name").grid(row=0, column=0, padx=10, pady=10)
entry_first_name = tk.Entry(root)
entry_first_name.grid(row=0, column=1)

tk.Label(root, text="Last Name").grid(row=1, column=0, padx=10, pady=10)
entry_last_name = tk.Entry(root)
entry_last_name.grid(row=1, column=1)

tk.Label(root, text="Enrollment Number").grid(row=2, column=0, padx=10, pady=10)
entry_enrollment_number = tk.Entry(root)  
entry_enrollment_number.grid(row=2, column=1)

tk.Label(root, text="Studying Year").grid(row=3, column=0, padx=10, pady=10)
entry_studying_year = tk.Entry(root)
entry_studying_year.grid(row=3, column=1)

tk.Label(root, text="Studying Sem").grid(row=4, column=0, padx=10, pady=10)
entry_studying_sem = tk.Entry(root)
entry_studying_sem.grid(row=4, column=1)

tk.Label(root, text="Email ID").grid(row=5, column=0, padx=10, pady=10)
entry_email_id = tk.Entry(root)
entry_email_id.grid(row=5, column=1)

tk.Label(root, text="Phone Number").grid(row=6, column=0, padx=10, pady=10)
entry_phone_number = tk.Entry(root)
entry_phone_number.grid(row=6, column=1)

tk.Label(root, text="Password").grid(row=7, column=0, padx=10, pady=10)
entry_password = tk.Entry(root, show='*')
entry_password.grid(row=7, column=1)

tk.Label(root, text="Confirm Password").grid(row=8, column=0, padx=10, pady=10)
entry_confirm_password = tk.Entry(root, show='*')
entry_confirm_password.grid(row=8, column=1)

tk.Button(root, text="Sign Up", command=submit_form).grid(row=9, columnspan=2, pady=10)

# Initialize the database
create_database()

# Start the main loop
root.mainloop()