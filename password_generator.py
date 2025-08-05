import tkinter as tk
from tkinter import messagebox  'Ru\}5^MUsiQs{Ok6+n+dbz
import random
import string
import pyperclip
from PIL import Image, ImageTk  # 🖼️ Pillow for image support

def generate_password():
    length = length_var.get()
    if length <= 0:
        messagebox.showerror("Error", "Password length must be greater than 0")
        return

    charset = ""
    if letters_var.get():
        charset += string.ascii_letters
    if numbers_var.get():
        charset += string.digits
    if symbols_var.get():
        charset += string.punctuation

    if not charset:
        messagebox.showerror("Error", "Select at least one character type")
        return

    password = ''.join(random.choice(charset) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Empty", "No password to copy!")

# Main window
root = tk.Tk()
root.title("Password Generator with Background")
root.geometry("500x400")
root.resizable(False, False)

# Load background image
bg_img = Image.open("Background1.jpg")  # Replace with your image file
bg_img = bg_img.resize((500, 400))
bg_photo = ImageTk.PhotoImage(bg_img)

# Set background
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Overlay Frame (transparent background not supported, so we simulate layout)
frame = tk.Frame(root, bg="#ffffff", bd=2)
frame.place(relx=0.5, rely=0.5, anchor="center")

# UI inside the frame
tk.Label(frame, text="🔐 Password Generator", font=("Helvetica", 16, "bold"), bg="#ffffff").pack(pady=10)
tk.Label(frame, text="Password Length:", font=("Arial", 11), bg="#ffffff").pack()
length_var = tk.IntVar(value=12)
tk.Spinbox(frame, from_=4, to=64, textvariable=length_var, width=5, font=("Arial", 11)).pack()

letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=False)

tk.Checkbutton(frame, text="Include Letters", variable=letters_var, bg="#ffffff").pack()
tk.Checkbutton(frame, text="Include Numbers", variable=numbers_var, bg="#ffffff").pack()
tk.Checkbutton(frame, text="Include Symbols", variable=symbols_var, bg="#ffffff").pack()

tk.Button(frame, text="Generate", command=generate_password, bg="#28a745", fg="white").pack(pady=10)

password_entry = tk.Entry(frame, font=("Arial", 12), width=30, justify="center")
password_entry.pack()

tk.Button(frame, text="Copy", command=copy_to_clipboard, bg="#007bff", fg="white").pack(pady=10)

root.mainloop()
