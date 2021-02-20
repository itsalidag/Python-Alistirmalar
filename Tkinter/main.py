from tkinter import *

window = Tk()
window.title("My first GUI")
window.minsize(width = 500, height = 300)



def button_clicked():
    print("bclick")
    my_label.config(text = input.get())
my_label = Label(text = "hello", font = ("Arial",24,"bold"))
my_label.pack()


button = Button(text = "Clik Me", command = button_clicked)

button.pack()
input = Entry(width = 10)
input.pack()

window.mainloop()