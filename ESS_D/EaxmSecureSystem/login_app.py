import tkinter as tk
from tkinter import messagebox

# Dummy user data for authentication
users = {
    "user1": "password1",
    "user2": "password2"
}

def login():
    username = entry_username.get()
    password = entry_password.get()
    
    if username in users and users[username] == password:
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
        # Here you can redirect to another window or perform other actions
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Create the main window
root = tk.Tk()
root.title("Login")

# Create and place the username label and entry
label_username = tk.Label(root, text="Username:")
label_username.pack(pady=5)

entry_username = tk.Entry(root)
entry_username.pack(pady=5)

# Create and place the password label and entry
label_password = tk.Label(root, text="Password:")
label_password.pack(pady=5)

entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Create and place the login button
button_login = tk.Button(root, text="Login", command=login)
button_login.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()