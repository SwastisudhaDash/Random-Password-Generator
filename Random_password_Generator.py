import tkinter as tk
from tkinter import ttk
import pyperclip
import random
import string

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Random Password Generator")

        self.length_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.lower_var = tk.BooleanVar()
        self.upper_var = tk.BooleanVar()
        self.digit_var = tk.BooleanVar()
        self.special_var = tk.BooleanVar()

        self.create_widgets()

    def create_widgets(self):
        
        ttk.Label(self.master, text="Length of Password:").grid(row=0, column=0, padx=30, pady=30, sticky="e")

        length_entry = ttk.Entry(self.master, textvariable=self.length_var)
        length_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        length_entry.insert(0, "8")

        ttk.Checkbutton(self.master, text="Lowcase", variable=self.lower_var).grid(row=1, column=0, padx=10, pady=5, sticky="w")
        ttk.Checkbutton(self.master, text="Upcase", variable=self.upper_var).grid(row=2, column=0, padx=10, pady=5, sticky="w")
        ttk.Checkbutton(self.master, text="Number", variable=self.digit_var).grid(row=3, column=0, padx=10, pady=5, sticky="w")
        ttk.Checkbutton(self.master, text="Special Char", variable=self.special_var).grid(row=4, column=0, padx=10, pady=5, sticky="w")

        ttk.Button(self.master, text="Generate", command=self.generate_password).grid(row=5, column=0, columnspan=2, pady=10)

        ttk.Entry(self.master, textvariable=self.password_var, state="readonly").grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="we")

        ttk.Button(self.master, text="Copy", command=self.copy_to_clipboard).grid(row=7, column=0, columnspan=2, pady=10)

    def generate_password(self):
        length = int(self.length_var.get())
        lowercase = string.ascii_lowercase if self.lower_var.get() else ''
        uppercase = string.ascii_uppercase if self.upper_var.get() else ''
        digits = string.digits if self.digit_var.get() else ''
        special_chars = string.punctuation if self.special_var.get() else ''

        all_chars = lowercase + uppercase + digits + special_chars

        if not all_chars:
            tk.messagebox.showerror("Error", " select one character.")
            return

        generated_password = ''.join(random.choice(all_chars) for _ in range(length))
        self.password_var.set(generated_password)

    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            pyperclip.copy(password)
            tk.messagebox.showinfo("Copied", "Password copied to clipboard.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
