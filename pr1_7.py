import tkinter as tk
from tkinter import ttk
import random

root = tk.Tk()
root.title("Задача 7: Случайное число для Марка")
root.geometry("380x200")

def generate_random():
    max_val = trackbar.get()
    rand = random.randint(0, max_val) if max_val > 0 else 0
    progress['value'] = rand
    result_label.config(text=f"Марк, твоё число: {rand}")

tk.Label(root, text="Марк, задай максимум и жми!", font=("Arial", 10)).pack(pady=5)

trackbar = tk.Scale(root, from_=0, to=100, orient='horizontal', label="Макс. для Марка")
trackbar.set(50)
trackbar.pack(pady=10)

btn = tk.Button(root, text="Сгенерировать для Марка", command=generate_random)
btn.pack(pady=5)

progress = ttk.Progressbar(root, orient='horizontal', length=280, mode='determinate')
progress.pack(pady=10)

result_label = tk.Label(root, text="Жми, Марк!", font=("Arial", 11))
result_label.pack(pady=5)

root.mainloop()
