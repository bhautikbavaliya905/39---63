import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x250")

# Entry box
entry = tk.Entry(root, font=("Arial", 18), width=20)
entry.pack(pady=20)

def calculate(operator):
    num1 = float(entry.get())

    # Get second number
    entry.delete(0, tk.END)
    entry.insert(0, "")

    root.second_number = num1
    root.operator = operator

def result():
    num2 = float(entry.get())
    num1 = root.second_number
    op = root.operator

    if op == "+":
        ans = num1 + num2
    elif op == "-":
        ans = num1 - num2
    elif op == "*":
        ans = num1 * num2
    elif op == "/":
        ans = num1 / num2

    entry.delete(0, tk.END)
    entry.insert(0, str(ans))

# Buttons
tk.Button(root, text="+", width=8, command=lambda: calculate("+")).pack()
tk.Button(root, text="-", width=8, command=lambda: calculate("-")).pack()
tk.Button(root, text="*", width=8, command=lambda: calculate("*")).pack()
tk.Button(root, text="/", width=8, command=lambda: calculate("/")).pack()
tk.Button(root, text="=", width=8, command=result).pack()

root.mainloop()

