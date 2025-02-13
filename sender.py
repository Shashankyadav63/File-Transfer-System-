import socket
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def send_file(file_path, conn):
    """Sends the selected file to the connected client."""
    try:
        if os.path.exists(file_path):
            file_size = os.path.getsize(file_path)
            conn.sendall(f"{file_size}".encode())  # Send file size to client
            
            with open(file_path, 'rb') as file:
                while (chunk := file.read(1024)):  # Read and send file in chunks
                    conn.sendall(chunk)
            print("File sent successfully.")
        else:
            conn.sendall(b"ERROR: File does not exist.")
            print("File does not exist.")
    except Exception as e:
        print(f"Error while sending file: {e}")

def server_program(file_path):
    """Starts the server, accepts a client, and sends the selected file."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind(('0.0.0.0', 5000))  # Bind to all available interfaces, port 5000
        server_socket.listen(1)
        print("Server is listening...")

        conn, addr = server_socket.accept()
        print(f"Connection from: {addr}")
        
        send_file(file_path, conn)
        
        conn.close()
        print("Connection closed.")
    except Exception as e:
        messagebox.showerror("Server Error", f"An error occurred: {e}")
    finally:
        server_socket.close()

def start_server():
    """Opens a file dialog, selects a file, and starts the server."""
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            server_program(file_path)
            messagebox.showinfo("Success", "File sent successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("Warning", "No file selected.")

# Tkinter GUI setup
root = tk.Tk()
root.title("File Sender")

# Get screen dimensions and set window size to half of the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{int(screen_width / 2)}x{int(screen_height)}+0+0")  # Half width, full height, aligned to the left

root.configure(bg="#2E2E2E")  # Dark modern background

# Create a frame to center the content
frame = tk.Frame(root, bg="#3B3B3B", padx=20, pady=20, relief="groove", bd=2)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Title label with enhanced font and color
title_label = tk.Label(frame, text="File Sender", font=("Helvetica", 20, "bold"), bg="#3B3B3B", fg="#FFFFFF")
title_label.pack(pady=10)

# Instruction label with more padding and modern font
instruction_label = tk.Label(frame, text="Select a file to send and start the server", font=("Helvetica", 14),
                             bg="#3B3B3B", fg="#FFFFFF")
instruction_label.pack(pady=10)

# Start button with a modern design
start_button = tk.Button(frame, text="Select File and Start Server", font=("Helvetica", 14, "bold"), 
                         bg="#61AFEF", fg="#282C34", relief="flat", 
                         command=start_server)
start_button.pack(pady=20, fill="x")

# Run the Tkinter main loop
root.mainloop()
