from tkinter import *
import csv
import re
import pandas as pd
import IPython 
import urllib
from PIL import Image,ImageTk

def indiancusine(top):
    indiancusine=Toplevel(top)
    indiancusine.geometry("750x750+100+100")
    indiancusine.title("THE RECIPE BOOK/menu/indiancusine/indiancusine menu")
    indiancusine.attributes('-fullscreen',True)
    i=PhotoImage(file=r"C:\Users\namra\source\repos\now you can cook\now you can cook\brown bg.png")
    x=i.zoom(3,3)
    lbli=Label(indiancusine,image=x,bg="#FFE5B4")
    lbli.place(x=0,y=0)
    def lunches():
        lunches=Toplevel(indiancusine)
        lunches.geometry("750x750+100+100")
        lunches.title("lunch Recipies/THE RECIPE BOOK.com")
        lunches.attributes('-fullscreen',True)
        a=PhotoImage(file=r"C:\Users\namra\source\repos\now you can cook\now you can cook\brown bg.png")
        x=a.zoom(3,3)
        lbli=Label(lunches,image=x,bg="#FFE5B4")
        lbli.place(x=0,y=0)
        file_obj=open(r'C:\Users\namra\source\repos\now you can cook\now you can cook\Asian Indian Cusine - webautomation_data_allrecipes.com_70424_282615_2023-07-28-15-21-08.csv','r') 
        df = pd.read_csv(file_obj)
        dish_name=df['title'].tolist()

        lbl1=Label(lunches,text="Recipies made ready for you : ",font=("britannic bold",30),fg="#F27348",bg="#FFE5B4")
        lbl1.place(x=15,y=10)
            
        cw=400
        ch=50
        for i, item in enumerate(dish_name):
            x = (i % 3) * cw  
            y = (i // 3) * ch
            button =Button(lunches, text=item,bd=2,fg='white',bg='#F27348',command=lambda name=item: on_button_click(name))
            button.place(x=x+40, y=y+100, width=cw, height=ch)
                
            def on_button_click(button_name):
                string=''
                toplevel=Toplevel(lunches)
                toplevel.geometry('1000x1000+10+10')
                toplevel.title(button_name)
                toplevel.attributes('-fullscreen',True)
                selected_row = df[df['title'] == button_name]
                row = selected_row.iloc[0].to_dict()
                string+="RECIPIE : "+row['title']+"\n"+"COOKING TIME : "+row['cook']+"\n"+"DESCRIPTION : "+ dot(row['description'])+"\n"+"INGREDIENTS : "+"\n"+comma(row['ingredients'])+"\n"+"DIRECTIONS : "+"\n"+dot(row['directions'])
                a=PhotoImage(file=r"C:\Users\namra\source\repos\now you can cook\now you can cook\brown bg.png")
                x=a.zoom(3,3)
                lbli=Label(toplevel,image=x,bg="#FFE5B4")
                lbli.place(x=0,y=0)   
                recipieLabel=Label(toplevel,text=row['title'],font=("Britannic bold",30),fg="#F27348",bg="#FFE5B4")
                recipieLabel.place(x=0,y=10)
                def open_img():
                        img_button(row['images'])
                btn=Button(toplevel,text="View The Final result",fg="white",bg="#F27348",command=open_img,height=5,width=30)
                btn.place(x=1000,y=10)
                lbl=Label(toplevel,text=string,font=("cascadian code",10),bg="#F27348",fg="white")
                lbl.place(x=100,y=100)

#FFE5B4 --->peach
#F27348 --->dark green
#button fg --->white
    def breads():
        breads=Toplevel(indiancusine)
        breads.geometry("750x750+100+100")
        breads.title("breads recipies/THE RECIPE BOOK.com") 
        breads.attributes('-fullscreen',True)
        a=PhotoImage(file=r"C:\Users\namra\source\repos\now you can cook\now you can cook\brown bg.png")
        x=a.zoom(3,3)
        lbli=Label(breads,image=x,bg="#FFE5B4")
        lbli.place(x=0,y=0)  
        file_obj=open(r'C:\Users\namra\source\repos\now you can cook\now you can cook\Indian Breads - webautomation_data_allrecipes.com_70429_282620_2023-07-28-16-25-51.csv','r') 
        df = pd.read_csv(file_obj)
        dish_name=df['title'].tolist()

        lbl1=Label(breads,text="Recipies made ready for you : ",font=("britannic bold",30),bg="#FFE5B4",fg="#F27348")
        lbl1.place(x=10,y=10)
            
        cw=400
        ch=50
        for i, item in enumerate(dish_name):
            x = (i % 3) * cw  
            y = (i // 3) * ch
            button =Button(breads, text=item,fg='white',bg='#F27348',command=lambda name=item: on_button_click(name))
            button.place(x=x+100, y=y+100, width=cw, height=ch)

            def on_button_click(button_name):
                string=''
                toplevel=Toplevel(breads)
                toplevel.geometry('1000x1000+10+10')
                toplevel.title(button_name)
                toplevel.attributes('-fullscreen',True)
                selected_row = df[df['title'] == button_name]
                row = selected_row.iloc[0].to_dict()
                string+="RECIPIE : "+row['title']+"\n"+"COOKING TIME : "+row['cook']+"\n"+"DESCRIPTION : "+ dot(row['description'])+"\n"+"INGREDIENTS : "+"\n"+comma(row['ingredients'])+"\n"+"DIRECTIONS : "+"\n"+dot(row['directions'])
                a=PhotoImage(file=r"C:\Users\namra\source\repos\now you can cook\now you can cook\brown bg.png")
                x=a.zoom(3,3)
                lbli=Label(toplevel,image=x,bg="#FFE5B4")
                lbli.place(x=0,y=0)
                recipieLabel=Label(toplevel,text=row['title'],font=("Britannic bold",30),fg="#F27348",bg="#FFE5B4")
                recipieLabel.place(x=0,y=10)
                lbl=Label(toplevel,text=string,font=("cascadian code",10),bg="#F27348",fg="white")
                lbl.place(x=100,y=100)
                def open_img():
                        img_button(row['images'])
                btn=Button(toplevel,text="View The Final result",fg="white",bg="#F27348",command=open_img,height=5,width=30)
                btn.place(x=1000,y=10)


    def drinks():
        drinks=Toplevel(indiancusine)
        drinks.geometry("750x750+100+100")
        drinks.title("drinks recipies/THE RECIPE BOOK.com") 
        drinks.attributes('-fullscreen',True)
        a=PhotoImage(file=r"C:\Users\namra\source\repos\now you can cook\now you can cook\brown bg.png")
        x=a.zoom(3,3)
        lbli=Label(drinks,image=x,bg="#FFE5B4")
        lbli.place(x=0,y=0)    
        file_obj=open(r'C:\Users\namra\source\repos\now you can cook\now you can cook\Indian Drinks - Indian Drinks.csv','r') 
        df = pd.read_csv(file_obj)
        dish_name=df['title'].tolist()

        lbl1=Label(drinks,text="Recipies made ready for you : ",font=("britannic bold",30),fg="#F27348",bg="#FFE5B4")
        lbl1.place(x=10,y=10)
            
        cw=400
        ch=50
        for i, item in enumerate(dish_name):
            x = (i % 3) * cw  
            y = (i // 3) * ch
            button =Button(drinks, text=item,fg='white',bg='#F27348',command=lambda name=item: on_button_click(name))
            button.place(x=x+100, y=y+100, width=cw, height=ch)

            def on_button_click(button_name):
                string=''
                toplevel=Toplevel(drinks)
                toplevel.geometry('1000x1000+10+10')
                toplevel.title(button_name)
                toplevel.attributes('-fullscreen',True)
                selected_row = df[df['title'] == button_name]
                row = selected_row.iloc[0].to_dict()
                    
                string+="RECIPIE : "+row['title']+"\n"+"COOKING TIME : "+row['cook']+"\n"+"DESCRIPTION : "+ dot(row['description'])+"\n"+"INGREDIENTS : "+"\n"+comma(row['ingredients'])+"\n"+"DIRECTIONS : "+"\n"+dot(row['directions'])
                a=PhotoImage(file=r"C:\Users\namra\source\repos\now you can cook\now you can cook\brown bg.png")
                x=a.zoom(3,3)
                lbli=Label(toplevel,image=x,bg="#FFE5B4")
                lbli.place(x=0,y=0)
                recipieLabel=Label(toplevel,text=row['title'],font=("Britannic bold",30),fg="#F27348",bg="#FFE5B4")
                recipieLabel.place(x=0,y=10)
                def open_img():
                        img_button(row['images'])
                btn=Button(toplevel,text="View The Final result",fg="white",bg="#F27348",command=open_img,height=5,width=30)
                btn.place(x=1000,y=10)
                lbl=Label(toplevel,text=string,font=("cascadian code",10),bg="#F27348",fg="white")
                lbl.place(x=100,y=100)


    def snacks():
        snacks=Toplevel(indiancusine)
        snacks.geometry("750x750+100+100")
        snacks.title("snacks recipies/THE RECIPE BOOK.com") 
        snacks.attributes('-fullscreen',True)
        a=PhotoImage(file=r"C:\Users\namra\source\repos\now you can cook\now you can cook\brown bg.png")
        x=a.zoom(3,3)
        lbli=Label(snacks,image=x,bg="#FFE5B4")
        lbli.place(x=0,y=0)   
        file_obj=open(r'C:\Users\namra\source\repos\now you can cook\now you can cook\snacks - webautomation_data_allrecipes.com_70619_283226_2023-08-01-16-10-25.csv','r') 
        df = pd.read_csv(file_obj)
        dish_name=df['title'].tolist()

        lbl1=Label(snacks,text="Recipies made ready for you : ",font=("britannic bold",30),fg="#F27348",bg="#FFE5B4")
        lbl1.place(x=10,y=10)
            
        cw=400
        ch=50
        for i, item in enumerate(dish_name):
            x = (i % 3) * cw  
            y = (i // 3) * ch
            button =Button(snacks, text=item,fg='white',bg='#FFE5B4',command=lambda name=item: on_button_click(name))
            button.place(x=x+100, y=y+100, width=cw, height=ch)

            def on_button_click(button_name):
                string=''
                toplevel=Toplevel(snacks)
                toplevel.geometry('1000x1000+10+10')
                toplevel.title(button_name)
                toplevel.attributes('-fullscreen',True)
                selected_row = df[df['title'] == button_name]
                row = selected_row.iloc[0].to_dict()
                    
                string+="RECIPIE : "+row['title']+"\n"+"COOKING TIME : "+row['cook']+"\n"+"DESCRIPTION : "+ dot(row['description'])+"\n"+"INGREDIENTS : "+"\n"+comma(row['ingredients'])+"\n"+"DIRECTIONS : "+"\n"+dot(row['directions'])
                a=PhotoImage(file=r"C:\Users\namra\source\repos\now you can cook\now you can cook\brown bg.png")
                x=a.zoom(3,3)
                lbli=Label(toplevel,image=x,bg="#FFE5B4")
                lbli.place(x=0,y=0)
                recipieLabel=Label(toplevel,text=row['title'],font=("Britannic bold",30),fg="#F27348",bg="#FFE5B4")
                recipieLabel.place(x=0,y=10)
                def open_img():
                        img_button(row['images'])
                btn=Button(toplevel,text="View The Final result",fg="white",bg="#F27348",command=open_img,height=5,width=30)
                btn.place(x=1000,y=10)
                lbl=Label(toplevel,text=string,font=("cascadian code",10),bg="#F27348",fg="white")
                lbl.place(x=100,y=100)


    def img_button(url):
            urllib.request.urlretrieve(url,"img.png")
            org_img = Image.open("img.png")
            org_img.show()

    menu=Label(indiancusine,text="INDIAN CUSINE MENU",font=("britannic bold",50),fg="#F27348",bg="#FFE5B4")
    menu.place(x=400,y=10)
    b1 = Button(indiancusine,text="ASIAN LUNCHES",fg="white",bg="#F27348",font=("britannic bold",15),bd=2,height=10,width=50,command=lunches)
    b1.place(x=100,y=100)
    b2 = Button(indiancusine,text="BREADS",fg="white",bg="#F27348",font=("britannic bold",15),bd=2,height=10,width=50,command=breads)
    b2.place(x=700,y=100)
    b3 = Button(indiancusine,text="INDIAN DRINKS",fg="white",bg="#F27348",font=("britannic bold",15),bd=2,height=10,width=50,command=drinks)
    b3.place(x=100,y=400)
    b4 = Button(indiancusine,text="SNACKS",fg="white",bg="#F27348",font=("britannic bold",15),bd=2,height=10,width=50,command=snacks)
    b4.place(x=700,y=400)
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