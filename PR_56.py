import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Dialog Box")
root.geometry("300x200")

def show_dialog():
    messagebox.showinfo("Alert", "Hello! This is an alert.")

def confirm():
    messagebox.askyesno("Confirmation", "Do you want to continue?")

button1 = tk.Button(root, text="Show Alert", command=show_dialog)
button1.pack(pady=20)

button2 = tk.Button(root, text="Confirmation", command=confirm)
button2.pack()

root.mainloop()

