import tkinter as tk
from tkinter import messagebox
import MySQLdb

# Database connection
db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="",
    db="college"
)

cursor = db.cursor()


# Insert
def insert():
    name = name_entry.get()
    stream = stream_entry.get()
    college = college_entry.get()
    contact = contact_entry.get()

    sql = """INSERT INTO student
             (name, stream, college, contact)
             VALUES (%s, %s, %s, %s)"""

    cursor.execute(sql, (name, stream, college, contact))
    db.commit()

    messagebox.showinfo("Success", "Student inserted successfully!")


# Update
def update():
    sid = id_entry.get()
    name = name_entry.get()
    stream = stream_entry.get()
    college = college_entry.get()
    contact = contact_entry.get()

    sql = """UPDATE student
             SET name=%s, stream=%s, college=%s, contact=%s
             WHERE id=%s"""

    cursor.execute(sql, (name, stream, college, contact, sid))
    db.commit()

    messagebox.showinfo("Success", "Student updated successfully!")


# Delete
def delete():
    sid = id_entry.get()

    cursor.execute(
        "DELETE FROM student WHERE id=%s",
        (sid,)
    )

    db.commit()

    messagebox.showinfo("Success", "Student deleted successfully!")


# View
def view():
    cursor.execute("SELECT * FROM student")

    records = cursor.fetchall()

    output.delete("1.0", tk.END)

    for row in records:
        output.insert(tk.END, str(row) + "\n")


# GUI
root = tk.Tk()
root.title("Student Management System")
root.geometry("500x500")

tk.Label(root, text="Student Management System",
         font=("Arial", 18)).pack(pady=10)

tk.Label(root, text="Student ID").pack()
id_entry = tk.Entry(root)
id_entry.pack()

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Stream").pack()
stream_entry = tk.Entry(root)
stream_entry.pack()

tk.Label(root, text="College").pack()
college_entry = tk.Entry(root)
college_entry.pack()

tk.Label(root, text="Contact").pack()
contact_entry = tk.Entry(root)
contact_entry.pack()

tk.Button(root, text="Insert", command=insert).pack(pady=5)
tk.Button(root, text="Update", command=update).pack(pady=5)
tk.Button(root, text="Delete", command=delete).pack(pady=5)
tk.Button(root, text="View", command=view).pack(pady=5)

output = tk.Text(root, height=8, width=50)
output.pack(pady=10)

root.mainloop()