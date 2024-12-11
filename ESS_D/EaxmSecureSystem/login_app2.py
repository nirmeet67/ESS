import tkinter as tk
from tkinter import messagebox
from database import authenticate_user

def login():
    username = entry_username.get().strip()
    password = entry_password.get()

    user = authenticate_user(username, password)
    if user:
        messagebox.showinfo("Success", "Login successful!")
    else:
        messagebox.showerror("Error", "Invalid username or password.")

# Create the main window
root = tk.Tk()
root.title("User  Login")

# Create and place labels and entry fields
tk.Label(root, text="Email ID").grid(row=0, column=0, padx=10, pady=10)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1)

tk.Label(root, text="Password").grid(row=1, column=0, padx=10, pady=10)
entry_password = tk.Entry(root, show='*')
entry_password.grid(row=1, column=1)

tk.Button(root, text="Login", command=login).grid(row=2, columnspan=2, pady=10)

# Start the main loop
root.mainloop()