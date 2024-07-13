import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        # Frame for the listbox and scrollbar
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        # Listbox for tasks
        self.task_list = tk.Listbox(frame, width=50, height=15, bd=0, selectmode=tk.SINGLE)
        self.task_list.pack(side=tk.LEFT, fill=tk.BOTH)

        # Scrollbar for the listbox
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.task_list.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_list.yview)

        # Entry box for new tasks
        self.task_entry = tk.Entry(self.root, width=50)
        self.task_entry.pack(pady=10)

        # Button to add task
        add_task_btn = tk.Button(self.root, text="Add Task", command=self.add_task)
        add_task_btn.pack(pady=5)

        # Button to delete task
        delete_task_btn = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        delete_task_btn.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.task_list.curselection()[0]
            self.task_list.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()