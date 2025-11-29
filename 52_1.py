import tkinter as tk

root = tk.Tk()
root.title("Задача 1: Кнопка → Label")
root.geometry("300x150")

def greet():
    name = entry.get() or "друг"
    label.config(text=f"Привет, {name}!")

entry = tk.Entry(root, width=20)
entry.insert(0, "Mark")
entry.pack(pady=10)

btn = tk.Button(root, text="Показать приветствие", command=greet)
btn.pack(pady=5)

label = tk.Label(root, text="", fg="blue", font=("Arial", 12))
label.pack(pady=10)

root.mainloop()
