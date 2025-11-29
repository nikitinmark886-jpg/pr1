import tkinter as tk

root = tk.Tk()
root.title("Задача 2: Кнопка → Memo")
root.geometry("300x200")

def add_greeting():
    name = entry.get() or "друг"
    memo.insert(tk.END, f"Привет, {name}!")

entry = tk.Entry(root, width=20)
entry.insert(0, "Mark")
entry.pack(pady=5)

btn = tk.Button(root, text="Добавить в Memo", command=add_greeting)
btn.pack(pady=5)

memo = tk.Listbox(root, height=6)
memo.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

root.mainloop()
