from tkinter import *


def calculate():
    m = float(entry.get())
    km = m*1.609
    label3.config(text="{:.2f}".format(km))


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=15)

entry = Entry(width=10)
entry.insert(END, string="0")
entry.grid(row=0, column=1)

label1 = Label(text="Miles")
label1.grid(row=0, column=2)

label2 = Label(text="is equal to")
label2.grid(row=1, column=0)

label3 = Label(text="0.00")
label3.grid(row=1, column=1)

label4 = Label(text="Km")
label4.grid(row=1, column=2)

button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)


window.mainloop()
