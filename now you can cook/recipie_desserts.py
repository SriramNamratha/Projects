from tkinter import *
import csv
import re
import pandas as pd
import IPython 
import urllib
from PIL import Image,ImageTk
def desserts(top):
        start=Toplevel(top)
        start.geometry("750x750+100+100")
        start.title("THE RECIPE BOOK/menu/Desserts/Desserts menu")
        start.attributes('-fullscreen' , True)
        
        i=PhotoImage(file=r"C:\Users\namra\source\repos\now you can cook\now you can cook\brown bg.png")
        x=i.zoom(3,3)
        lbli=Label(start,image=x,bg="#FFE5B4")
        lbli.place(x=0,y=0)


        def cake():
            cakes=Toplevel(start)
            cakes.geometry("750x750+100+100")
            cakes.title("cakes Recipies/THE RECIPE BOOK.com")
            cakes.attributes('-fullscreen',True)
            s="CAKES"
            a=PhotoImage(file=r"C:\Users\namra\source\repos\now you can cook\now you can cook\brown bg.png")
            x=a.zoom(3,3)
            lbli=Label(cakes,image=x,bg="#FFE5B4")
            lbli.place(x=0,y=0)
            file_obj=open(r'C:\Users\namra\pp project\chocolates.csv','r') 
            df = pd.read_csv(file_obj)
            lbl1=Label(cakes,text="Recipies made ready for you : ",font=("britannic bold",30),bg="#FFE5B4",fg="#5784BA")
            lbl1.place(x=10,y=10)
            dish_name=df['title'].tolist()
            cw=400
            ch=50
            for i, item in enumerate(dish_name):
                x = (i % 3) * cw  # Calculate x coordinate based on the column number
                y = (i // 3) * ch
                button =Button(cakes, text=item,fg='White',bg='#5784BA',command=lambda name=item: on_button_click(name))
                button.place(x=x+100, y=y+100, width=cw, height=ch)
                def on_button_click(button_name):
                    string=''
                    toplevel=Toplevel(cakes)
                    toplevel.geometry('1000x1000+10+10')
                    toplevel.title(button_name)
                    toplevel.attributes('-fullscreen',True)
                    selected_row = df[df['title'] == button_name]
                    row = selected_row.iloc[0].to_dict()
                    string+="RECIPIE : "+row['title']+"\n"+"COOKING TIME : "+row['cook']+"\n"+"DESCRIPTION : "+ dot(row['description'])+"\n"+"INGREDIENTS : "+"\n"+comma(row['ingredients'])+"\n"+"DIRECTIONS : "+"\n"+dot(row['directions'])
                    url=str(row['images'])
                    i=PhotoImage(file=r"C:\Users\namra\source\repos\now you can cook\now you can cook\brown bg.png")
                    x=i.zoom(3,3)
                    lbli=Label(toplevel,image=x,bg="#FFE5B4")
                    lbli.place(x=0,y=0)
                    recipieLabel=Label(toplevel,text=row['title'],font=("Britannic bold",30),fg="#5784BA",bg="#FFE5B4")
                    recipieLabel.place(x=0,y=10)
                    def open_img():
                        img_button(row['images'])
                    btn=Button(toplevel,text="View The Final result",fg="white",bg="#5784BA",command=open_img,height=5,width=30)
                    btn.place(x=1000,y=10)
                    lbl=Label(toplevel,text=string,bg="#5784BA",fg="white",font=("cascadia code",10))
                    lbl.place(x=0,y=100)
                    
                    

#FFE5B4
#5784BA
        def caramels():#FFE5B4--peach
            caramel=Toplevel(start)
            caramel.geometry("750x750+100+100")
            caramel.title("caramel Recipies/THE RECIPE BOOK.com") 
            caramel.attributes('-fullscreen',True)
            s="CARAMEL"
            a=PhotoImage(file=r"C:\Users\namra\source\repos\now you can cook\now you can cook\brown bg.png")
            x=a.zoom(3,3)
            lbli=Label(caramel,image=x,bg="#FFE5B4")
            lbli.place(x=0,y=0)
            file_obj=open(r'C:\Users\namra\source\repos\now you can cook\now you can cook\caramel desserts.csv','r') 
            df = pd.read_csv(file_obj)
            lbl1=Label(caramel,text="Recipies made ready for you : ",font=("britannic bold",30),fg="#5784BA",bg="#FFE5B4")
            lbl1.place(x=10,y=10)
            dish_name=df['title'].tolist()
            cw=400
            ch=50
            for i, item in enumerate(dish_name):
                x = (i % 3) * cw  # Calculate x coordinate based on the column number
                y = (i // 3) * ch
                button =Button(caramel, text=item,fg='white',bg='#5784BA',command=lambda name=item: on_button_click(name))
                button.place(x=x+100, y=y+100, width=cw, height=ch)
                def on_button_click(button_name):
                    string=''
                    toplevel=Toplevel(caramel)
                    toplevel.geometry('1000x1000+10+10')
                    toplevel.title(button_name)
                    toplevel.attributes('-fullscreen',True)
                    selected_row = df[df['title'] == button_name]
                    row = selected_row.iloc[0].to_dict()
                    string+="RECIPIE : "+row['title']+"\n"+"COOKING TIME : "+row['cook']+"\n"+"DESCRIPTION : "+ dot(row['description'])+"\n"+"INGREDIENTS : "+"\n"+comma(row['ingredients'])+"\n"+"DIRECTIONS : "+"\n"+dot(row['directions'])
                    url=str(row['images'])
                    i=PhotoImage(file=r"C:\Users\namra\source\repos\now you can cook\now you can cook\brown bg.png")
                    x=i.zoom(3,3)
                    lbli=Label(toplevel,image=x,bg="#FFE5B4")
                    lbli.place(x=0,y=0)
                    recipieLabel=Label(toplevel,text=row['title'],font=("Britannic bold",30),fg="#5784BA",bg="#FFE5B4")
                    recipieLabel.place(x=0,y=10)
                    def open_img():
                        img_button(row['images'])
                    btn=Button(toplevel,text="View The Final result",fg="white",bg="#5784BA",command=open_img,height=5,width=30)
                    btn.place(x=1000,y=10)
                    lbl=Label(toplevel,text=string,bg="#5784BA",fg="white",font=("cascadia code",10))
                    lbl.place(x=0,y=100)
#FFE5B4
#5784BA          
        def puddings():
            pudding=Toplevel(start)
            pudding.geometry("750x750+100+100")
            pudding.title("Pudding Recipies/THE RECIPE BOOK.com") 
            pudding.attributes('-fullscreen',True)
            s="PUDDING"
            a=PhotoImage(file=r"C:\Users\namra\source\repos\now you can cook\now you can cook\brown bg.png")
            x=a.zoom(3,3)
            lbli=Label(pudding,image=x,bg="#FFE5B4")
            lbli.place(x=0,y=0)
            file_obj=open(r'C:\Users\namra\source\repos\now you can cook\now you can cook\Puddings_desserts.csv','r') 
            df = pd.read_csv(file_obj)
            lbl1=Label(pudding,text="Recipies made ready for you : ",font=("britannic bold",30),bg="#FFE5B4",fg="#5784BA")
            lbl1.place(x=10,y=10)
            dish_name=df['title'].tolist()
            cw=400
            ch=50
            for i, item in enumerate(dish_name):
                x = (i % 3) * cw  # Calculate x coordinate based on the column number
                y = (i // 3) * ch
                button =Button(pudding, text=item,fg='white',bg='#5784BA',command=lambda name=item: on_button_click(name))
                button.place(x=x+100, y=y+100, width=cw, height=ch)
                def on_button_click(button_name):
                    string=''
                    toplevel=Toplevel(pudding)
                    toplevel.geometry('1000x1000+10+10')
                    toplevel.title(button_name)
                    toplevel.attributes('-fullscreen',True)
                    selected_row = df[df['title'] == button_name]
                    row = selected_row.iloc[0].to_dict()
                    string+="RECIPIE : "+row['title']+"\n"+"COOKING TIME : "+row['cook']+"\n"+"DESCRIPTION : "+ dot(row['description'])+"\n"+"INGREDIENTS : "+"\n"+comma(row['ingredients'])+"\n"+"DIRECTIONS : "+"\n"+dot(row['directions'])
                    url=str(row['images'])
                    i=PhotoImage(file=r"C:\Users\namra\source\repos\now you can cook\now you can cook\brown bg.png")
                    x=i.zoom(3,3)
                    lbli=Label(toplevel,image=x,bg="#FFE5B4")
                    lbli.place(x=0,y=0)
                    recipieLabel=Label(toplevel,text=row['title'],font=("Britannic bold",30),fg="#5784BA",bg="#FFE5B4")
                    recipieLabel.place(x=0,y=10)
                    def open_img():
                        img_button(row['images'])
                    btn=Button(toplevel,text="View The Final result",fg="white",bg="#5784BA",command=open_img,height=5,width=30)
                    btn.place(x=1000,y=10)
                    lbl=Label(toplevel,text=string,bg="#5784BA",fg="white",font=("cascadia code",10))
                    lbl.place(x=0,y=100)

        def cookie():
            cookies=Toplevel(start)
            cookies.geometry("750x750+100+100")
            cookies.title("cookies Recipies/THE RECIPE BOOK.com") 
            cookies.attributes('-fullscreen',True)
            s="COOKIES"
            a=PhotoImage(file=r"C:\Users\namra\source\repos\now you can cook\now you can cook\brown bg.png")
            x=a.zoom(3,3)
            lbli=Label(cookies,image=x,bg="#FFE5B4")
            lbli.place(x=0,y=0)
            file_obj=open(r'C:\Users\namra\source\repos\now you can cook\now you can cook\cookies desserts.csv','r') 
            df = pd.read_csv(file_obj)
            lbl1=Label(cookies,text="Recipies made ready for you : ",font=("britannic bold",30),fg="#5784BA",bg="#FFE5B4")
            lbl1.place(x=10,y=10)
            dish_name=df['title'].tolist()
            cw=400
            ch=50
            for i, item in enumerate(dish_name):
                x = (i % 3) * cw  # Calculate x coordinate based on the column number
                y = (i // 3) * ch
                button =Button(cookies, text=item,fg='white',bg='#5784BA',command=lambda name=item: on_button_click(name))
                button.place(x=x+100, y=y+100, width=cw, height=ch)
                def on_button_click(button_name):
                    string=''
                    toplevel=Toplevel(cookies)
                    toplevel.geometry('1000x1000+10+10')
                    toplevel.title(button_name)
                    toplevel.attributes('-fullscreen',True)
                    selected_row = df[df['title'] == button_name]
                    row = selected_row.iloc[0].to_dict()
                    string+="RECIPIE : "+row['title']+"\n"+"COOKING TIME : "+row['cook']+"\n"+"DESCRIPTION : "+ dot(row['description'])+"\n"+"INGREDIENTS : "+"\n"+comma(row['ingredients'])+"\n"+"DIRECTIONS : "+"\n"+dot(row['directions'])
                    url=str(row['images'])
                    i=PhotoImage(file=r"C:\Users\namra\source\repos\now you can cook\now you can cook\brown bg.png")
                    x=i.zoom(3,3)
                    lbli=Label(toplevel,image=x,bg="#FFE5B4")
                    lbli.place(x=0,y=0)
                    recipieLabel=Label(toplevel,text=row['title'],font=("Britannic bold",30),fg="#5784BA",bg="#FFE5B4")
                    recipieLabel.place(x=0,y=10)
                    def open_img():
                        img_button(row['images'])
                    btn=Button(toplevel,text="View The Final result",fg="white",bg="#5784BA",command=open_img,height=5,width=30)
                    btn.place(x=1000,y=10)
                    lbl=Label(toplevel,text=string,bg="#5784BA",fg="white",font=("cascadia code",10))
                    lbl.place(x=0,y=100)

        def pies():
            pie=Toplevel(start)
            pie.geometry("750x750+100+100")
            pie.title("Pies Recipies/THE RECIPE BOOK.com") 
            pie.attributes('-fullscreen',True)
            s="PIES"
            a=PhotoImage(file=r"C:\Users\namra\source\repos\now you can cook\now you can cook\brown bg.png")
            x=a.zoom(3,3)
            lbli=Label(pie,image=x,bg="#FFE5B4")
            lbli.place(x=0,y=0)
            file_obj=open(r'C:\Users\namra\source\repos\now you can cook\now you can cook\pies_desserts.csv','r') 
            df = pd.read_csv(file_obj)
            lbl1=Label(pie,text="Recipies made ready for you : ",font=("britannic bold",30),bg="#FFE5B4",fg="#5784BA")
            lbl1.place(x=10,y=10)
            dish_name=df['title'].tolist()
            cw=400
            ch=50
            for i, item in enumerate(dish_name):
                x = (i % 3) * cw  # Calculate x coordinate based on the column number
                y = (i // 3) * ch
                button =Button(pie, text=item,fg='white',bg='#5784BA',command=lambda name=item: on_button_click(name))
                button.place(x=x+100, y=y+100, width=400, height=50)
                def on_button_click(button_name):
                    string=''
                    toplevel=Toplevel(pie)
                    toplevel.geometry('1000x1000+10+10')
                    toplevel.title(button_name)
                    toplevel.attributes('-fullscreen',True)
                    selected_row = df[df['title'] == button_name]
                    row = selected_row.iloc[0].to_dict()
                    string+="RECIPIE : "+row['title']+"\n"+"COOKING TIME : "+row['cook']+"\n"+"DESCRIPTION : "+ dot(row['description'])+"\n"+"INGREDIENTS : "+"\n"+comma(row['ingredients'])+"\n"+"DIRECTIONS : "+"\n"+dot(row['directions'])
                    url=str(row['images'])
                    i=PhotoImage(file=r"C:\Users\namra\source\repos\now you can cook\now you can cook\brown bg.png")
                    x=i.zoom(3,3)
                    lbli=Label(toplevel,image=x,bg="#FFE5B4")
                    lbli.place(x=0,y=0)
                    recipieLabel=Label(toplevel,text=row['title'],font=("Britannic bold",30),fg="#5784BA",bg="#FFE5B4")
                    recipieLabel.place(x=0,y=10)
                    def open_img():
                        img_button(row['images'])
                    btn=Button(toplevel,text="View The Final result",fg="white",bg="#5784BA",command=open_img,height=5,width=30)
                    btn.place(x=1000,y=10)
                    lbl=Label(toplevel,text=string,bg="#5784BA",fg="white",font=("cascadia code",10))
                    lbl.place(x=0,y=100)
        def comma(i:str):
                res , a ="" , i.split(",")
                for item in a:
                    res+=item+"\n"
                return res

        def dot(i:str):
                res , a ="" , i.split(".")
                for item in a:
                    res+=item+"\n"
                return res

        def img_button(url):
            urllib.request.urlretrieve(url,"img.png")
            org_img = Image.open("img.png")
            org_img.show()


        menu=Label(start,text="DESSERTS MENU",font=("britannic bold",50),fg="#5784BA",bg="#FFE5B4")
        menu.place(x=400,y=10)
        b1 = Button(start,text="CAKES",fg="white",bg="#5784BA",font=("britannic bold",15),bd=2,height=7,width=50,command=cake)
        b1.place(x=50,y=100)
        b2 = Button(start,text="CARAMEL DESSERTS",fg="white",bg="#5784BA",font=("britannic bold",15),bd=2,height=7,width=50,command=caramels)
        b2.place(x=700,y=100)
        b3 = Button(start,text="PUDDINGS",fg="white",bg="#5784BA",font=("britannic bold",15),bd=2,height=7,width=50,command=puddings)
        b3.place(x=50,y=300)
        b4 = Button(start,text="COOKIES",fg="white",bg="#5784BA",font=("britannic bold",15),bd=2,height=7,width=50,command=cookie)
        b4.place(x=700,y=300)
        b5 = Button(start,text="PIES",fg="white",bg="#5784BA",font=("britannic bold",15),bd=2,height=7,width=50,command=pies)
        b5.place(x=400,y=500)
        