import socket
import tkinter as tk
from tkinter import messagebox
import os

def receive_file(file_name, conn):
    try:
        # Receive file size from server
        file_size = int(conn.recv(1024).decode())

        # Notify user that the file is being received
        print(f"Receiving file: {file_name} ({file_size} bytes)")

        # Open file for writing in binary mode
        with open(file_name, 'wb') as file:
            bytes_received = 0
            buffer_size = 8192  # Increased buffer size
            while bytes_received < file_size:
                data = conn.recv(buffer_size)
                if not data:
                    break
                file.write(data)
                bytes_received += len(data)

        # Check if the entire file was received
        if bytes_received == file_size:
            print("File received successfully.")
            return True
        else:
            print(f"File transfer incomplete: {bytes_received}/{file_size} bytes received.")
            return False
    except Exception as e:
        print(f"Error receiving file: {e}")
        return False


def client_program(server_ip, file_name):
    try:
        # Create a socket connection to the server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, 5000))  # Connect to the server's IP

        # Receive the file
        if receive_file(file_name, client_socket):
            messagebox.showinfo("Success", f"File '{file_name}' received successfully!")
        else:
            messagebox.showerror("Error", "Failed to receive the complete file.")

        # Close the socket connection
        client_socket.close()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def start_client(ip_entry, file_name_entry):
    # Get the values from the input fields
    server_ip = ip_entry.get()
    file_name = file_name_entry.get()

    if server_ip:
        if file_name:
            # Ensure the user provides a valid file extension
            if '.' in file_name and len(os.path.splitext(file_name)[1]) > 1:
                client_program(server_ip, file_name)
            else:
                messagebox.showwarning("Warning", "Please provide a valid file name with extension.")
        else:
            messagebox.showwarning("Warning", "File name cannot be empty.")
    else:
        messagebox.showwarning("Warning", "Server IP cannot be empty.")


# Tkinter GUI setup
root = tk.Tk()
root.title("File Receiver")

# Get screen width and height, and set the window to half screen width
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{int(screen_width / 2)}x{int(screen_height / 2)}+{int(screen_width / 4)}+{int(screen_height / 4)}")

root.configure(bg="#282C34")  # Dark modern background

# Create a frame to center the content
frame = tk.Frame(root, bg="#3C4043", padx=20, pady=20, relief="groove", bd=2)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Title label with enhanced font and color
title_label = tk.Label(frame, text="File Receiver", font=("Helvetica", 20, "bold"), bg="#3C4043", fg="#FFFFFF")
title_label.pack(pady=10)

# Instruction label with more padding and modern font
instruction_label = tk.Label(frame, text="Enter server IP and file name below", font=("Helvetica", 14),
                             bg="#3C4043", fg="#FFFFFF")
instruction_label.pack(pady=10)

# Server IP label and entry
ip_label = tk.Label(frame, text="Server IP Address:", font=("Helvetica", 12), bg="#3C4043", fg="#FFFFFF")
ip_label.pack(pady=5)
ip_entry = tk.Entry(frame, font=("Helvetica", 12), bg="#FFFFFF", fg="#000000", width=30)
ip_entry.pack(pady=5)

# File name label and entry
file_name_label = tk.Label(frame, text="File Name to Save:", font=("Helvetica", 12), bg="#3C4043", fg="#FFFFFF")
file_name_label.pack(pady=5)
file_name_entry = tk.Entry(frame, font=("Helvetica", 12), bg="#FFFFFF", fg="#000000", width=30)
file_name_entry.pack(pady=5)

# Start button with rounded corners and improved design
start_button = tk.Button(frame, text="Connect to Server and Receive File", font=("Helvetica", 14, "bold"),
                         bg="#61AFEF", fg="#282C34", relief="flat",
                         command=lambda: start_client(ip_entry, file_name_entry))
start_button.pack(pady=20, fill="x")

# Set rounded button style
start_button.config(highlightthickness=0, bd=0, overrelief="flat")

# Run the Tkinter main loop
root.mainloop()
