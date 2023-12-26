from tkinter import *
import csv
import re
import pandas as pd
import IPython 
import urllib
from PIL import Image,ImageTk
#FFE5B4 --->peach
#218B82 --->dark green
#button fg --->white  
def starters(top):
    start=Toplevel(top)
    start.geometry("750x750+100+100")
    start.title("THE RECIPE BOOK/menu/starters/starters menu")
    start.attributes('-fullscreen',True)
    i=PhotoImage(file=r"C:\Users\namra\source\repos\now you can cook\now you can cook\brown bg.png")
    x=i.zoom(3,3)
    lbli=Label(start,image=x,bg="#FFE5B4")
    lbli.place(x=0,y=0)
    def side_dishes():
        side_dishes=Toplevel(start)
        side_dishes.geometry("750x750+100+100")
        side_dishes.title("side dishes Recipies/THE RECIPE BOOK.com")
        side_dishes.attributes('-fullscreen',True)
        a=PhotoImage(file=r"C:\Users\namra\source\repos\now you can cook\now you can cook\brown bg.png")
        x=a.zoom(3,3)
        lbli=Label(side_dishes,image=x,bg="#FFE5B4")
        lbli.place(x=0,y=0)
        file_obj=open(r'C:\Users\namra\source\repos\now you can cook\now you can cook\side.csv','r') 
        df = pd.read_csv(file_obj)
        dish_name=df['title'].tolist()

        lbl1=Label(side_dishes,text="Recipies made ready for you : ",font=("britannic bold",30),fg="#218B82",bg="#FFE5B4")
        lbl1.place(x=15,y=10)
            
        cw=400
        ch=50
        for i, item in enumerate(dish_name):
            x = (i % 3) * cw  
            y = (i // 3) * ch
            button =Button(side_dishes, text=item,bd=2,fg='white',bg='#218B82',command=lambda name=item: on_button_click(name))
            button.place(x=x+40, y=y+100, width=cw, height=ch)
                
            def on_button_click(button_name):
                string=''
                toplevel=Toplevel(side_dishes)
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
                recipieLabel=Label(toplevel,text=row['title'],font=("Britannic bold",30),fg="#218B82",bg="#FFE5B4")
                recipieLabel.place(x=0,y=10)
                def open_img():
                        img_button(row['images'])
                btn=Button(toplevel,text="View The Final result",fg="white",bg="#218B82",command=open_img,height=5,width=30)
                btn.place(x=1000,y=10)
                lbl=Label(toplevel,text=string,font=("cascadian code",10),bg="#218B82",fg="white")
                lbl.place(x=100,y=100)

#FFE5B4 --->peach
#218B82 --->dark green
#button fg --->white
    def soups():
        soup=Toplevel(start)
        soup.geometry("750x750+100+100")
        soup.title("soups recipies/THE RECIPE BOOK.com") 
        soup.attributes('-fullscreen',True)
        a=PhotoImage(file=r"C:\Users\namra\source\repos\now you can cook\now you can cook\brown bg.png")
        x=a.zoom(3,3)
        lbli=Label(soups,image=x,bg="#FFE5B4")
        lbli.place(x=0,y=0)  
        file_obj=open(r'C:\Users\namra\source\repos\now you can cook\now you can cook\soups.csv','r') 
        df = pd.read_csv(file_obj)
        dish_name=df['title'].tolist()

        lbl1=Label(soup,text="Recipies made ready for you : ",font=("britannic bold",30),fg="#218B82",bg="#FFE5B4")
        lbl1.place(x=10,y=10)
            
        cw=400
        ch=30
        for i, item in enumerate(dish_name):
            x = (i % 3) * cw  
            y = (i // 3) * ch
            button =Button(soup, text=item,fg='white',bg='#218B82',command=lambda name=item: on_button_click(name))
            button.place(x=x+100, y=y+100, width=cw, height=ch)

            def on_button_click(button_name):
                string=''
                toplevel=Toplevel(soup)
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
                recipieLabel=Label(toplevel,text=row['title'],font=("Britannic bold",30),fg="#218B82",bg="#FFE5B4")
                recipieLabel.place(x=0,y=10)
                def open_img():
                        img_button(row['images'])
                btn=Button(toplevel,text="View The Final result",fg="white",bg="#218B82",command=open_img,height=5,width=30)
                btn.place(x=1000,y=10)
                lbl=Label(toplevel,text=string,font=("cascadian code",10),bg="#218B82",fg="white")
                lbl.place(x=100,y=100)


    def salads():
        salad=Toplevel(start)
        salad.geometry("750x750+100+100")
        salad.title("salads recipies/THE RECIPE BOOK.com") 
        salad.attributes('-fullscreen',True)
        a=PhotoImage(file=r"C:\Users\namra\source\repos\now you can cook\now you can cook\brown bg.png")
        x=a.zoom(3,3)
        lbli=Label(salads,image=x,bg="#FFE5B4")
        lbli.place(x=0,y=0)    
        file_obj=open(r'C:\Users\namra\source\repos\now you can cook\now you can cook\salads.csv','r') 
        df = pd.read_csv(file_obj)
        dish_name=df['title'].tolist()

        lbl1=Label(salad,text="Recipies made ready for you : ",font=("britannic bold",30),fg="#218B82",bg="#FFE5B4")
        lbl1.place(x=10,y=10)
            
        cw=400
        ch=50
        for i, item in enumerate(dish_name):
            x = (i % 3) * cw  
            y = (i // 3) * ch
            button =Button(salad, text=item,fg='white',bg='#218B82',command=lambda name=item: on_button_click(name))
            button.place(x=x+100, y=y+100, width=cw, height=ch)

            def on_button_click(button_name):
                string=''
                toplevel=Toplevel(salad)
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
                recipieLabel=Label(toplevel,text=row['title'],font=("Britannic bold",30),fg="#218B82",bg="#FFE5B4")
                recipieLabel.place(x=0,y=10)
                def open_img():
                        img_button(row['images'])
                btn=Button(toplevel,text="View The Final result",fg="white",bg="#218B82",command=open_img,height=5,width=30)
                btn.place(x=1000,y=10)
                lbl=Label(toplevel,text=string,font=("cascadian code",10),bg="#218B82",fg="white")
                lbl.place(x=100,y=100)


    def drinks():
        drink=Toplevel(start)
        drink.geometry("750x750+100+100")
        drink.title("drinks recipies/THE RECIPE BOOK.com") 
        drink.attributes('-fullscreen',True)
        a=PhotoImage(file=r"C:\Users\namra\source\repos\now you can cook\now you can cook\brown bg.png")
        x=a.zoom(3,3)
        lbli=Label(drinks,image=x,bg="#FFE5B4")
        lbli.place(x=0,y=0)   
        file_obj=open(r'C:\Users\namra\source\repos\now you can cook\now you can cook\drinks.csv','r') 
        df = pd.read_csv(file_obj)
        dish_name=df['title'].tolist()

        lbl1=Label(drink,text="Recipies made ready for you : ",font=("britannic bold",30),fg="#218B82",bg="#FFE5B4")
        lbl1.place(x=10,y=10)
            
        cw=400
        ch=50
        for i, item in enumerate(dish_name):
            x = (i % 3) * cw  
            y = (i // 3) * ch
            button =Button(drink, text=item,fg='white',bg='#FFE5B4',command=lambda name=item: on_button_click(name))
            button.place(x=x+100, y=y+100, width=cw, height=ch)

            def on_button_click(button_name):
                string=''
                toplevel=Toplevel(drink)
                toplevel.geometry('1000x1000+10+10')
                toplevel.title(button_name)
                toplevel.attributes('-fullscreen',True)
                selected_row = df[df['title'] == button_name]
                row = selected_row.iloc[0].to_dict()
                    
                string+="RECIPIE : "+row['title']+"\n"+"COOKING TIME : "+row['cook']+"\n"+"DESCRIPTION : "+ dot(row['description'])+"\n"+"INGREDIENTS : "+"\n"+comma(row['ingredients'])+"\n"+"DIRECTIONS : "+"\n"+dot(row['directions'])
                a=PhotoImage(file=r"C:\Users\namra\source\repos\now you can cook\now you can cook\brown bg.png")
                x=a.zoom(3,3)
                lbli=Label(toplevel,image=x,bg="grey")
                lbli.place(x=0,y=0)
                recipieLabel=Label(toplevel,text=row['title'],font=("Britannic bold",30),fg="#218B82",bg="#FFE5B4")
                recipieLabel.place(x=0,y=10)
                def open_img():
                        img_button(row['images'])
                btn=Button(toplevel,text="View The Final result",fg="white",bg="#218B82",command=open_img,height=5,width=30)
                btn.place(x=1000,y=10)
                lbl=Label(toplevel,text=string,font=("cascadian code",10),bg="#218B82",fg="white")
                lbl.place(x=100,y=100)

    menu=Label(start,text="STARTERS MENU",font=("britannic bold",50),fg="#218B82",bg="#FFE5B4")
    menu.place(x=400,y=10)
    b1 = Button(start,text="SIDE DISHES",fg="white",bg="#218B82",font=("britannic bold",15),bd=2,height=10,width=50,command=side_dishes)
    b1.place(x=100,y=100)
    b2 = Button(start,text="SOUPS",fg="white",bg="#218B82",font=("britannic bold",15),bd=2,height=10,width=50,command=soups)
    b2.place(x=700,y=100)
    b3 = Button(start,text="SALADS",fg="white",bg="#218B82",font=("britannic bold",15),bd=2,height=10,width=50,command=salads)
    b3.place(x=100,y=400)
    b4 = Button(start,text="DRINKS",fg="white",bg="#218B82",font=("britannic bold",15),bd=2,height=10,width=50,command=drinks)
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