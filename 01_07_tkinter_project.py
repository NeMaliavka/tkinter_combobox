from tkinter import *
from tkinter import ttk


def selected(event):
    # получаем выделенный элемент
    selection = combobox.get()
    print(selection)
    label = ttk.Label(root, text=f"Составляю отчет: {selection}")
    label.pack(anchor=NW, padx=6, pady=6)


root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

period = ["За день", "За неделю", "За месяц", "За год"]

text_label = StringVar(value='Отчёт')

combobox = ttk.Combobox(textvariable=text_label, values=period)
combobox.pack(anchor=NW, padx=6, pady=6)
combobox.bind("<<ComboboxSelected>>", selected)
root.mainloop()
