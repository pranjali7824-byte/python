import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# ================= DATABASE =================

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    roll INTEGER PRIMARY KEY,
    name TEXT,
    maths INTEGER,
    science INTEGER,
    english INTEGER,
    total INTEGER,
    percentage REAL,
    grade TEXT
)
""")

conn.commit()

# ================= FUNCTIONS =================

def calculate_grade(per):
    if per >= 90:
        return "A+"
    elif per >= 80:
        return "A"
    elif per >= 70:
        return "B"
    elif per >= 60:
        return "C"
    elif per >= 50:
        return "D"
    else:
        return "F"

def add_student():
    try:
        roll = int(roll_entry.get())
        name = name_entry.get()

        maths = int(maths_entry.get())
        science = int(science_entry.get())
        english = int(english_entry.get())

        total = maths + science + english
        percentage = total / 3

        grade = calculate_grade(percentage)

        cursor.execute("""
        INSERT INTO students VALUES(?,?,?,?,?,?,?,?)
        """,
        (roll,name,maths,science,english,total,percentage,grade))

        conn.commit()

        messagebox.showinfo("Success","Student Added")

        clear_fields()
        show_students()

    except Exception as e:
        messagebox.showerror("Error",str(e))

def show_students():

    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("SELECT * FROM students")

    for data in cursor.fetchall():
        tree.insert("",tk.END,values=data)

def delete_student():

    selected = tree.focus()

    if not selected:
        return

    data = tree.item(selected)

    roll = data['values'][0]

    cursor.execute(
        "DELETE FROM students WHERE roll=?",
        (roll,)
    )

    conn.commit()

    show_students()

def search_student():

    roll = search_entry.get()

    cursor.execute(
        "SELECT * FROM students WHERE roll=?",
        (roll,)
    )

    record = cursor.fetchone()

    if record:
        messagebox.showinfo(
            "Student Found",
            f"Name: {record[1]}\n"
            f"Percentage: {record[6]:.2f}\n"
            f"Grade: {record[7]}"
        )
    else:
        messagebox.showerror(
            "Not Found",
            "Student not found"
        )

def clear_fields():
    roll_entry.delete(0,tk.END)
    name_entry.delete(0,tk.END)
    maths_entry.delete(0,tk.END)
    science_entry.delete(0,tk.END)
    english_entry.delete(0,tk.END)

# ================= GUI =================

root = tk.Tk()
root.title("Student Result Management System")
root.geometry("1000x600")

title = tk.Label(
    root,
    text="Student Result Management System",
    font=("Arial",18,"bold")
)

title.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

# Roll

tk.Label(frame,text="Roll No").grid(row=0,column=0,padx=10,pady=5)

roll_entry = tk.Entry(frame)
roll_entry.grid(row=0,column=1)

# Name

tk.Label(frame,text="Name").grid(row=1,column=0,padx=10,pady=5)

name_entry = tk.Entry(frame)
name_entry.grid(row=1,column=1)

# Maths

tk.Label(frame,text="Maths").grid(row=2,column=0,padx=10,pady=5)

maths_entry = tk.Entry(frame)
maths_entry.grid(row=2,column=1)

# Science

tk.Label(frame,text="Science").grid(row=3,column=0,padx=10,pady=5)

science_entry = tk.Entry(frame)
science_entry.grid(row=3,column=1)

# English

tk.Label(frame,text="English").grid(row=4,column=0,padx=10,pady=5)

english_entry = tk.Entry(frame)
english_entry.grid(row=4,column=1)

# Buttons

tk.Button(
    frame,
    text="Add Student",
    command=add_student,
    bg="green",
    fg="white"
).grid(row=5,column=0,pady=10)

tk.Button(
    frame,
    text="Delete Student",
    command=delete_student,
    bg="red",
    fg="white"
).grid(row=5,column=1)

# Search

search_frame = tk.Frame(root)
search_frame.pack(pady=10)

tk.Label(
    search_frame,
    text="Search Roll No"
).pack(side=tk.LEFT)

search_entry = tk.Entry(search_frame)
search_entry.pack(side=tk.LEFT,padx=5)

tk.Button(
    search_frame,
    text="Search",
    command=search_student
).pack(side=tk.LEFT)

# Table

columns = (
    "Roll",
    "Name",
    "Maths",
    "Science",
    "English",
    "Total",
    "Percentage",
    "Grade"
)

tree = ttk.Treeview(
    root,
    columns=columns,
    show="headings"
)

for col in columns:
    tree.heading(col,text=col)
    tree.column(col,width=110)

tree.pack(fill=tk.BOTH,expand=True,pady=10)

show_students()

root.mainloop()

conn.close()