import tkinter as tk
from tkinter import messagebox
import string
import random
import pyperclip

#parol yaradır
def generate_password():
    try:
        length = int(length_var.get())
    except:
        messagebox.showwarning("Error", "Write length of pass as a number!")
        return

    chars = ""
    if use_upper.get():
        chars += string.ascii_uppercase
    if use_lower.get():
        chars += string.ascii_lowercase
    if use_digits.get():
        chars += string.digits
    if use_symbols.get():
        chars += "!@#$%&?"

    # hecne secilmeyibse
    if chars == "":
        messagebox.showwarning("Error", "Please choose something!")
        return

    password = "".join(random.choice(chars) for _ in range(length))
    password_var.set(password)
    strength_check(password)

# Parol gucun yoxlamaq
def strength_check(pwd):
    score = 0
    if any(c.isupper() for c in pwd): score += 1
    if any(c.islower() for c in pwd): score += 1
    if any(c.isdigit() for c in pwd): score += 1
    if any(c in "!@#$%&?" for c in pwd): score += 1
    if len(pwd) >= 12: score += 1

    
    if score <= 2:
        strength_label.config(text="Weak", fg="red")
    elif score == 3:
        strength_label.config(text="Medium", fg="yellow")
    else:
        strength_label.config(text="Strong", fg="lime")

# copy etmek
def copy_password():
    if password_var.get() != "":
        pyperclip.copy(password_var.get())
        messagebox.showinfo("Kamran muellim", "Password was copied!")

# esas sehife
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x300")
root.configure(bg="black") 

password_var = tk.StringVar()
length_var = tk.StringVar(value="12")

# heading 
tk.Label(root, text="PASSWORD GENERATOR", fg="lime", bg="black", font=("Consolas", 12, "bold")).pack(pady=10)

# lenght
tk.Label(root, text="Length:", fg="lime", bg="black").pack()
tk.Entry(root, textvariable=length_var, width=5, bg="black", fg="lime").pack()

# secimler
use_upper = tk.BooleanVar(value=True)
use_lower = tk.BooleanVar(value=True)
use_digits = tk.BooleanVar(value=True)
use_symbols = tk.BooleanVar(value=False)

tk.Checkbutton(root, text="Uppercase (A-Z)", variable=use_upper, bg="black", fg="lime", selectcolor="black").pack(anchor="w", padx=40)
tk.Checkbutton(root, text="Lowercase (a-z)", variable=use_lower, bg="black", fg="lime", selectcolor="black").pack(anchor="w", padx=40)
tk.Checkbutton(root, text="Digits (0-9)", variable=use_digits, bg="black", fg="lime", selectcolor="black").pack(anchor="w", padx=40)
tk.Checkbutton(root, text="Symbols (!@#$%&?)", variable=use_symbols, bg="black", fg="lime", selectcolor="black").pack(anchor="w", padx=40)

# Parol out
tk.Entry(root, textvariable=password_var, width=30, fg="lime", bg="black", font=("Consolas", 10)).pack(pady=10)


strength_label = tk.Label(root, text="Strength: -", fg="lime", bg="black")
strength_label.pack()

# buttonlar
tk.Button(root, text="Generate", command=generate_password, fg="black", bg="lime").pack(pady=5)
tk.Button(root, text="Copy", command=copy_password, fg="black", bg="lime").pack()

root.mainloop()
