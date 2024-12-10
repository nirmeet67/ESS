import tkinter as tk
from tkinter import messagebox, ttk
import re
import random
import smtplib
from twilio.rest import Client

# Global variable to store OTPs
otp_email = None
otp_phone = None

# Twilio credentials
TWILIO_ACCOUNT_SID = 'AC0680cfd02714ab6215665500a9eef2f0'
TWILIO_AUTH_TOKEN = '61037098cd8d9a0aeb04f1047d71eee1'
TWILIO_PHONE_NUMBER = '+13204222138'

# List of country codes
COUNTRY_CODES = [
    ("+1", "United States"),
    ("+91", "India"),
    ("+44", "United Kingdom"),
    ("+61", "Australia"),
    ("+81", "Japan"),
    # Add more country codes as needed
]

def generate_otp():
    """Generate a random 6-digit OTP."""
    return random.randint(100000, 999999)

def send_otp_email(email):
    """Send an OTP to the email."""
    global otp_email
    otp_email = generate_otp()
    
    # Set up the server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    
    # Login to your email account
    server.login('your_email@gmail.com', 'your_app_password')  # Use App Password if 2FA is enabled
    
    # Create the email content
    subject = "Your OTP Code"
    body = f"Your OTP code is: {otp_email}"
    message = f'Subject: {subject}\n\n{body}'
    
    # Send the email
    server.sendmail('your_email@gmail.com', email, message)
    server.quit()

def send_otp_phone(phone):
    """Send an OTP to the phone number."""
    global otp_phone
    otp_phone = generate_otp()
    
    # Create a Twilio client
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    
    # Send the SMS
    client.messages.create(
        body=f"Your OTP code is: {otp_phone}",
        from_=TWILIO_PHONE_NUMBER,
        to=phone
    )

def submit_form():
    # Retrieve the data from the form
    first_name = entry_first_name.get().strip()
    last_name = entry_last_name.get().strip()
    enrollment_number = entry_enrollment_number.get().strip()
    studying_year = entry_studying_year.get().strip()
    studying_sem = entry_studying_sem.get().strip()
    email_id = entry_email_id.get().strip()
    phone_number = entry_phone_number.get().strip()
    country_code = country_code_combobox.get()  # Get selected country code
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()

    # Combine country code with phone number
    full_phone_number = country_code + phone_number

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

    # Send OTP for email and phone verification
    send_otp_email(email_id)
    send_otp_phone(full_phone_number)

    # Ask for OTP verification
    otp_window(email_id, full_phone_number)

def otp_window(email, phone):
    """Create a new window for OTP verification."""
    otp_win = tk.Toplevel(root)
    otp_win.title("OTP Verification")

    tk.Label(otp_win, text="Enter OTP sent to your email:").grid(row=0, column=0, padx= 10, pady=10)
    entry_otp_email = tk.Entry(otp_win)
    entry_otp_email.grid(row=0, column=1)

    tk.Label(otp_win, text="Enter OTP sent to your phone:").grid(row=1, column=0, padx=10, pady=10)
    entry_otp_phone = tk.Entry(otp_win)
    entry_otp_phone.grid(row=1, column=1)

    def verify_otp():
        """Verify the entered OTPs."""
        email_otp = entry_otp_email.get()
        phone_otp = entry_otp_phone.get()

        if email_otp == str(otp_email) and phone_otp == str(otp_phone):
            messagebox.showinfo("Success", "Signup successful!")
            otp_win.destroy()  # Close OTP window
        else:
            messagebox.showerror("Error", "Invalid OTPs! Please try again.")

    submit_otp_button = tk.Button(otp_win, text="Verify OTP", command=verify_otp)
    submit_otp_button.grid(row=2, columnspan=2, pady=20)

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

tk.Label(root, text="Country Code").grid(row=6, column=0, padx=10, pady=10)
country_code_combobox = ttk.Combobox(root, values=[code[0] for code in COUNTRY_CODES])
country_code_combobox.grid(row=6, column=1)

tk.Label(root, text="Phone Number").grid(row=7, column=0, padx=10, pady=10)
entry_phone_number = tk.Entry(root)
entry_phone_number.grid(row=7, column=1)

tk.Label(root, text="Password").grid(row=8, column=0, padx=10, pady=10)
entry_password = tk.Entry(root, show='*')
entry_password.grid(row=8, column=1)

tk.Label(root, text="Confirm Password").grid(row=9, column=0, padx=10, pady=10)
entry_confirm_password = tk.Entry(root, show='*')
entry_confirm_password.grid(row=9, column=1)

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=10, columnspan=2, pady=20)

# Run the application
root.mainloop()