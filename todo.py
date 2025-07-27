import tkinter as tk
from tkinter import messagebox

todos = []

def add_todo():
    todo = entry.get()
    if todo:
        todos.append(todo)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a todo.")

def remove_todo():
    selected = listbox.curselection()
    if selected:
        idx = selected[0]
        removed = todos.pop(idx)
        update_listbox()
        messagebox.showinfo("Removed", f"Removed: {removed}")
    else:
        messagebox.showwarning("Selection Error", "Please select a todo to remove.")

def update_listbox():
    listbox.delete(0, tk.END)
    for todo in todos:
        listbox.insert(tk.END, todo)

root = tk.Tk()
root.title("Simple Todo App")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

entry = tk.Entry(frame, width=40)
entry.pack(side=tk.LEFT, padx=(0, 10))

add_btn = tk.Button(frame, text="Add Todo", command=add_todo)
add_btn.pack(side=tk.LEFT)

listbox = tk.Listbox(root, width=50)
listbox.pack(padx=10, pady=10)

remove_btn = tk.Button(root, text="Remove Selected", command=remove_todo)
remove_btn.pack(pady=(0, 10))

root.mainloop()
