import tkinter as tk

# Create root
root = tk.Tk()
root.title("Simple GUI")
root.geometry("300x200")

# Label
label = tk.Label(root, text="Enter your name:")
label.pack()

# Entry field
entry = tk.Entry(root)
entry.pack()

# Button function
def show_message():
    name = entry.get()
    result.config(text="Hello " + name)

# Button
button = tk.Button(root, text="Click Me", command=show_message)
button.pack()

# Result label
result = tk.Label(root, text="")
result.pack()

# Run GUI
root.mainloop()

