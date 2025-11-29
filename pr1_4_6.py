import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Задача 4+6: Для Марка")
root.geometry("400x200")

def update(val):
    value = int(val)
    progress['value'] = value
    value_label.config(text=f"Значение для Марка: {value}")

tk.Label(root, text="Управляй, Марк!").pack(pady=5)

trackbar = tk.Scale(root, from_=0, to=100, orient='horizontal', command=update)
trackbar.set(52)
trackbar.pack(pady=10)

progress = ttk.Progressbar(root, orient='horizontal', length=300, mode='determinate')
progress.pack(pady=10)
progress['value'] = 52

value_label = tk.Label(root, text="Значение для Марка: 50", font=("Arial", 11))
value_label.pack(pady=5)

root.mainloop()
