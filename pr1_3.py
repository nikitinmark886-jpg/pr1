import tkinter as tk

root = tk.Tk()
root.title("Задача 3: Счётчик нажатий")
root.geometry("250x120")

count = 0

def increment():
    global count
    count += 1
    label.config(text=f"Нажатий: {count} (Марк)")

btn = tk.Button(root, text="Нажми, Марк!", command=increment)
btn.pack(pady=10)

label = tk.Label(root, text="Нажатий: 0 (Марк)", font=("Arial", 12))
label.pack()

root.mainloop()
