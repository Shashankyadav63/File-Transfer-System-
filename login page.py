import tkinter as tk
from tkinter import Button, Frame, Label, PhotoImage, messagebox, Entry
import re
import subprocess

# Dictionary to store multiple users and their passwords
users_credentials = {
    "shashank": "1234",
    "admin": "admin123"
}

# Function to verify login credentials
def verify_login(username, password):
    if username in users_credentials and users_credentials[username] == password:
        messagebox.showinfo("Login Success", f"Welcome {username}!")
        root.destroy()  # Close the login window
        # Launch the main application (replace the path with your actual script path)
        subprocess.run(["python", r"C:\Users\shashank yadav\OneDrive\Desktop\FileTransferSystem\main.py"])
    else:
        messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

# Function to handle login button click
def login():
    username = username_entry.get()
    password = password_entry.get()
    verify_login(username, password)

# Function to validate password
def validate_password(password):
    if re.fullmatch(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password):
        return True
    return False

# Function to handle user registration
def register():
    username = register_username_entry.get()
    password = register_password_entry.get()

    if username and password:
        if username in users_credentials:
            messagebox.showerror("Registration Failed", "Username already exists. Please choose a different username.")
        elif not validate_password(password):
            messagebox.showerror(
                "Invalid Password", 
                "Password must be at least 8 characters long and include a combination of letters, numbers, and special symbols."
            )
        else:
            users_credentials[username] = password
            messagebox.showinfo("Registration Success", f"User '{username}' registered successfully!")
            register_window.destroy()  # Close the registration window
    else:
        messagebox.showerror("Error", "Both fields are required!")

# Function to open registration window
def open_register_window():
    global register_window, register_username_entry, register_password_entry, show_register_password_btn

    register_window = tk.Toplevel(root)
    register_window.title("Register")
    register_window.geometry("400x300")
    register_window.configure(bg="#fff")

    # Registration form
    Label(register_window, text="Register New User", font=("Microsoft YaHei UI Light", 18), bg="white").place(x=90, y=30)

    # Username field
    Label(register_window, text="Username", font=("Microsoft YaHei UI Light", 12), bg="white").place(x=50, y=100)
    register_username_entry = Entry(register_window, width=30, fg="black", bg="white", font=("Microsoft YaHei UI Light", 11))
    register_username_entry.place(x=150, y=100)

    # Password field
    Label(register_window, text="Password", font=("Microsoft YaHei UI Light", 12), bg="white").place(x=50, y=150)
    register_password_entry = Entry(register_window, width=30, fg="black", bg="white", font=("Microsoft YaHei UI Light", 11), show='*')
    register_password_entry.place(x=150, y=150)

    # Register button
    Button(register_window, text="Register", width=15, pady=5, bg="#57a1f8", fg="white", border=0, command=register).place(x=150, y=200)

    # Show password checkbox for registration
    show_register_password_btn = Button(register_window, text="Show Password", bg="#fff", command=toggle_register_password)
    show_register_password_btn.place(x=260, y=150)

# Function to toggle password visibility in the registration window
def toggle_register_password():
    if register_password_entry.cget('show') == '':
        register_password_entry.config(show='*')
        show_register_password_btn.config(text="Show Password")
    else:
        register_password_entry.config(show='')
        show_register_password_btn.config(text="Hide Password")

# Tkinter setup for login
root = tk.Tk()
root.title("Login")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False, False)

img = PhotoImage(file=r"C:\Users\shashank yadav\OneDrive\Desktop\FileTransferSystem\Login.png")
Label(root, image=img, bg="white").place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text="Log in", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
heading.place(x=100, y=5)

# Username entry ------------------------------------------------------------------------------------------------------------
def on_enter_username(e):
    username_entry.delete(0, "end")

def on_leave_username(e):
    if username_entry.get() == "":
        username_entry.insert(0, "username")

username_entry = tk.Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
username_entry.place(x=30, y=80)
username_entry.insert(0, "username")
username_entry.bind("<FocusIn>", on_enter_username)
username_entry.bind("<FocusOut>", on_leave_username)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

# Password entry ------------------------------------------------------------------------------------------------------------
def on_enter_password(e):
    password_entry.delete(0, "end")

def on_leave_password(e):
    if password_entry.get() == "":
        password_entry.insert(0, "password")

password_entry = tk.Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11), show='*')
password_entry.place(x=30, y=150)
password_entry.insert(0, "password")
password_entry.bind("<FocusIn>", on_enter_password)
password_entry.bind("<FocusOut>", on_leave_password)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

# Show password checkbox for login
def toggle_password():
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        show_password_btn.config(text="Show Password")
    else:
        password_entry.config(show='')
        show_password_btn.config(text="Hide Password")

show_password_btn = Button(frame, text="Show Password", bg="#fff", command=toggle_password)
show_password_btn.place(x=260, y=150)

# Log in button
Button(frame, width=39, pady=7, text="Log in", bg="#57a1f8", fg="white", border=0, command=login).place(x=35, y=204)

# Register button
Button(frame, width=15, pady=7, text="Register", bg="#57a1f8", fg="white", border=0, command=open_register_window).place(x=120, y=270)

# Run the Tkinter main loop
root.mainloop()
