from tkinter import *

window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width = 200, height = 100)


# 1 mil 1.609344 km
def calculator():
    ans =  int(input.get()) * 1.609344
    answer.config(text = ans)
# input alacak bir mile kutusu
input = Entry()
input.grid(column=1 , row=1)
# is equals to yanına sayı veyanına kilometers
label = Label(text = "miles")
label.grid(column=2 , row=1)
theis =Label(text = "is equals on kilometers to")
theis.grid(column=1 , row=2)
answer = Label(text = "0")
answer.grid(column=2 , row=2)
# calculate butonu.
button = Button(text = "Calculate", command = calculator)
button.grid(column=1 , row=4)






window.mainloop()