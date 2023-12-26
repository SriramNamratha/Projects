from tkinter import *
import csv
import re
import pandas as pd
from PIL import Image 
import IPython
import recipie_desserts
import recipie_starters
import recipie_indiancusine
window=Tk()
window.geometry("1000x1000+100+100")
window.title("https:/THE RECIPE BOOK/home page.com")
window.attributes('-fullscreen', True)

back1=PhotoImage(file =r"C:\Users\namra\pp project\cooking background.png")
larger_image = back1.subsample(2, 2)
limg= Label(window,image=larger_image,bg="grey")
limg.pack()
label1=Label(text="THE RECIPE BOOK",font=("cooper black",50),fg="#F08080",bg="#252436")
label1.place(x=350,y=280)

def cusine():
    global small_image,img
    top=Toplevel(window)
    top.geometry("750x750+100+100")
    top.title("menu page.com")
    top.attributes('-fullscreen', True)
    gif(top)
    lbl=Label(top,text="MENU",font=("Britannic bold",50),fg="#252436",bg="lavender")
    lbl.place(x=150,y=60)
    def enter_desserts():
        recipie_desserts.desserts(top)
    def enter_starters():
        recipie_starters.starters(top)
    def enter_indiancusine():
        recipie_indiancusine.indiancusine(top)
    btn1=Button(top,text="Desserts",font=15,fg="#F08080",bg="#252436",bd=2,height=2,width=10,command=enter_desserts)
    btn1.place(x=200,y=250)
    btn3=Button(top,text="Indian Cusine",font=15,fg="#F08080",bg="#252436",bd=2,height=2,width=10,command=enter_indiancusine)
    btn3.place(x=200,y=320)
    btn5=Button(top,text="Starters",font=15,fg="#F08080",bg="#252436",bd=2,height=2,width=10,command=enter_starters)
    btn5.place(x=200,y=390)
    img=PhotoImage(file=r"C:\Users\namra\source\repos\now you can cook\now you can cook\cooking 2.png")
    small_image = img.subsample(2, 3)
    prtimg=Label(top,image=small_image,bg="grey")
    prtimg.place(x=100,y=530)
button1=Button(window,text="MENU",font=15,fg="#252436",bg="#F08080",bd=5,height=2,width=10,command=cusine)
button1.place(x=630,y=400)
    
def gif(top):
    frameCnt = 20
    frames = [PhotoImage(file=r"C:\Users\namra\pp project\cooking gif.gif",format = 'gif -index %i' %(i)) for i in range(frameCnt)]
    def update(ind):
        frame = frames[ind]
        ind += 1
        if ind == frameCnt:
            ind = 0
        label.configure(image=frame)
        top.after(100, update, ind)
    label = Label(top)
    label.place(x=450,y=50)
    top.after(0, update, 0)

    
window.mainloop()
