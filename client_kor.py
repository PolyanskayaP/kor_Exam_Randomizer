from tkinter import *
import kor_random
from random import randint

def clicked():  
    bilet_number = randint(1, 30)
    bilet = "Билет №" + str(bilet_number)
    window.title(bilet)
    
    list3 = kor_random.rand_kor()
    lbl1.configure(text=list3[0])  
    lbl2.configure(text=list3[1])  
    lbl3.configure(text=list3[2])      

window = Tk()
#window.geometry('700x400')

bilet_number = randint(1, 30)
bilet = "Билет №" + str(bilet_number)
window.title(bilet)

lbl1 = Label(window, text="", font=("Arial Bold", 10))
lbl1.grid(column=0, row=0)  

lbl2 = Label(window, text="", font=("Arial Bold", 10))
lbl2.grid(column=0, row=1)  

lbl3 = Label(window, text="", font=("Arial Bold", 10))
lbl3.grid(column=0, row=2)  

btn = Button(window, text="Нажми", bg="black", fg="blue", command=clicked)
btn.grid(column=0, row=3)

window.mainloop()