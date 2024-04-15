import tkinter as tk

def on_click(event):
    # Отримуємо координати клітинки, на яку натиснули
    row = event.widget.rowcget(event.widget.index("@%d,%d" % (event.x, event.y)))
    col = event.widget.columncget(event.widget.index("@%d,%d" % (event.x, event.y)))
    print("Ви обрали клітинку: ({}, {})".format(row, col))

# Створюємо головне вікно
root = tk.Tk()

# Створюємо таблицю
table = tk.Canvas(root)
table.pack(expand=True, fill='both')

# Додаємо клітинки до таблиці
for i in range(10):
    for j in range(10):
        table.create_rectangle(i*50, j*50, (i+1)*50, (j+1)*50, fill="white")
        table.create_text((i*50+50//2, j*50+50//2), text="({}, {})".format(i, j))

# Прив'язуємо подію кліку до функції on_click
table.bind("<Button-1>", on_click)

# Запускаємо головне вікно
root.mainloop()