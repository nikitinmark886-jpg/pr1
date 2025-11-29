import tkinter as tk

root = tk.Tk()
root.title("Задача 5: Для Марка")
root.geometry("180x280")

def update_progress(val):
    percent = int(val)
    canvas.delete("fill")
    h = 200
    w = 50
    fill_h = (percent / 100) * h
    y0 = h - fill_h
    canvas.create_rectangle(5, y0, w-5, h-5, fill="green", outline="", tags="fill")

tk.Label(root, text="Уровень для Марка:", font=("Arial", 10)).pack(pady=5)

trackbar = tk.Scale(root, from_=0, to=100, orient='horizontal', command=update_progress)
trackbar.set(52)
trackbar.pack(pady=5)

canvas = tk.Canvas(root, width=50, height=200, bg="lightgray", relief="sunken")
canvas.pack(pady=10)
update_progress(60)

tk.Label(root, text="Марк управляет уровнем!", fg="darkgreen").pack(pady=5)

root.mainloop()
