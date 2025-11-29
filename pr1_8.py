import tkinter as tk

root = tk.Tk()
root.title("Задача 8: Цвет для Марка")
root.geometry("420x320")

def update_color(val=None):
    r = r_scale.get()
    g = g_scale.get()
    b = b_scale.get()
    hex_color = f"#{r:02x}{g:02x}{b:02x}"
    preview_canvas.config(bg=hex_color)
    code_label.config(text=f"Марк выбрал: RGB({r}, {g}, {b})")

tk.Label(root, text="Марк, настрой свой цвет!", font=("Arial", 12, "bold")).pack(pady=10)

tk.Label(root, text="Красный:").pack()
r_scale = tk.Scale(root, from_=0, to=255, orient='horizontal', command=update_color)
r_scale.set(52)
r_scale.pack()

tk.Label(root, text="Зелёный:").pack()
g_scale = tk.Scale(root, from_=0, to=255, orient='horizontal', command=update_color)
g_scale.set(52)
g_scale.pack()

tk.Label(root, text="Синий:").pack()
b_scale = tk.Scale(root, from_=0, to=255, orient='horizontal', command=update_color)
b_scale.set(52)
b_scale.pack()

preview_canvas = tk.Canvas(root, width=160, height=90, bg="white", relief="solid")
preview_canvas.pack(pady=15)

code_label = tk.Label(root, text="Марк ещё не выбрал цвет", font=("Courier", 11))
code_label.pack(pady=5)

update_color()

root.mainloop()
