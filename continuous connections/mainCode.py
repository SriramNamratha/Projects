from tkinter import *
import folium
from geopy.geocoders import Nominatim
import time
import webbrowser
from threading import Thread
from time import sleep
from folium.plugins import AntPath
from tkvideo import tkvideo
import pygame
splash_screen = Tk()
splash_screen.geometry('1000x1000+10+10')
splash_screen.title('continuous_connection')
splash_screen.attributes("-fullscreen",True)
pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)
def second_window():
    pygame.mixer.music.stop()
    splash_screen.destroy()
    root=Tk()
    root.geometry('1000x1000+10+10')
    root.title('continuous_connections')
    root.attributes("-fullscreen",True)
    
    bg=PhotoImage(file="solid background wise.png")
    bgl=bg.zoom(3,3)
    imb=Label(root,image=bgl)
    imb.place(x=0,y=0)
    
    back = PhotoImage(file = "second window.png")
    imglbl = Label(root,image=back,bg="grey")
    imglbl.pack()

    
    def combined_function():
        create_text_boxes()
        third_window()
        
    def create_text_boxes():
        global num_computers,counter,originator
        originator=originator_entry.get()
        num_computers=int(num_computers_entry.get())
        num_computers_entry.config(state="disabled")
        create_button.config(state="disabled")
        originator_entry.config(state='disabled')
    def third_window():
        root1=Toplevel(root)
        root1.geometry('1000x1000+10+10')
        root1.title('continuous_connections')
        root1.attributes("-fullscreen",True)
        
        bg=PhotoImage(file="solid background wise.png")
        bgl=bg.zoom(3,3)
        imb=Label(root1,image=bgl)
        imb.place(x=0,y=0)
        
        back = PhotoImage(file = "second window.png")
        imglbl = Label(root1,image=back,bg="grey")
        imglbl.pack()
        
        def create_location_text_box():
            global location_label,connections_label,location_entry,connections_entry
            #global location_label,connections_label,location_entry,connections_entry
            
            if counter <=num_computers:
                location_label=Label(root1,text=f"Computer {counter} location:",bg="#010B50",fg="#02FFD0",font=("britannic bold",20))
                location_label.place(x=400,y=100)
        
                location_entry=Entry(root1,font=("britannic bold",20),bg="#02FFD0",fg="#010B50")
                location_entry.place(x=800,y=100)
        
                connections_label=Label(root1,text=f"Computer {counter} connections:",bg="#010B50",fg="#02FFD0",font=("britannic bold",20))
                connections_label.place(x=400,y=200)
        
                connections_entry=Entry(root1,font=("britannic bold",20),bg="#02FFD0",fg="#010B50")
                connections_entry.place(x=800,y=200)
        
                submit_button.config(command=get_computer_data,state="normal")

                
            else:
                get_computer_data()
        def get_computer_data():
            global counter
        
            computer_location=location_entry.get()
            computer_connections_list=connections_entry.get().split()
            computer_connections=[int(computer) for computer in computer_connections_list]
        
            computer_data[counter]={
                "location":computer_location,
                "connections":computer_connections
            }
        
            print(f"Computer {counter} Location:", computer_location)
            print(f"Computer {counter} Connections:", computer_connections)
        
            location_label.pack_forget()
            location_entry.destroy()
            connections_label.pack_forget()
            connections_entry.destroy()
        
            counter+=1
        
            if counter <=num_computers:
                create_location_text_box()
            else:
                submit_button.config(state="disabled")
                counter = 1
                create_network_dict()
        def create_network_dict():
            global computer_data, network,originator
            print(originator)
            network = {}
            for computer_num, data in computer_data.items():
                network[computer_data[computer_num]["location"]]=[computer_data[conn]["location"] for conn in computer_data[computer_num]["connections"]]
        
            print("Network Dictionary:",network)
        def map_view():
            class TreeNode:
                def _init_(self, value):
                    self.value = value
                    self.children = []
                    self.children_count = 0
                def add_child(self, child_value):
                    child_node = TreeNode(child_value)
                    self.children.append(child_node)
                    self.children_count += 1  # Increment the children count when adding a child.
                    return child_node
            
            
            def create_tree(root_value, connections):
                root = TreeNode(root_value)
                
                stack = [root]
                visited = set()
            
                while stack:
                    current_node = stack.pop()
                    current_node_value = current_node.value
                    visited.add(current_node_value)
            
                    for neighbor in connections[current_node_value]:
                        if neighbor not in visited:
                            child_node = current_node.add_child(neighbor)  # Use the add_child method to add child nodes.
                            stack.append(child_node)
            
                return root
            
            
            def visualize_connections_on_map(root, connections):
                geolocator = Nominatim(user_agent="city_locator")
                
                def get_coordinates(city_name):
                    location = geolocator.geocode(city_name)
                    return location.latitude, location.longitude
            
                my_map1 = folium.Map(location=[17.385044, 78.486671], zoom_start=5)
                #my_map1.save(" my_map1.html " )
                def add_markers_and_connections(node):
                    global button_name
                    
                    for child in node.children:
            
                        
                        src_latitude, src_longitude = get_coordinates(node.value)
                        dest_latitude, dest_longitude = get_coordinates(child.value)
            
                        folium.Marker([src_latitude, src_longitude], popup=node.value,tooltip=node.value,radius=0.5, weight=0.5, border_width=5).add_to(my_map1)
                        folium.Marker([dest_latitude, dest_longitude], popup=child.value,tooltip=child.value,icon_size=(40, 40)).add_to(my_map1)
                        folium.PolyLine([(src_latitude, src_longitude), (dest_latitude, dest_longitude)], color="blue",weight=1).add_to(my_map1)
                        add_markers_and_connections(child)
                    if node==root:
                            button_lat,button_long=get_coordinates(node.value)
                            button_location=[button_lat,button_long]
                            button_marker = folium.Marker(location=button_location,icon=folium.Icon(icon='fa-laptop',color='red',angle=0,prefix='fa'), popup=node.value,tooltip=node.value).add_to(my_map1)
                            folium.CircleMarker(location=button_location,radius=25, fill_color='red').add_to(my_map1)
                            my_map1.save("mapin.html")
                            webbrowser.open("mapin.html")
                            send_messages(root)
                
                def mySort(e):
                    return e.children_count

                message_colors = [ "blue", "green", "purple", "orange", "pink", "brown", "gray", "cyan", "magenta"]
                originator_colors = {}
                #message_colors = ["red", "blue", "green", "purple", "orange", "pink", "brown", "gray", "cyan", "magenta"]
                #global color1
                #color1 = "red"
                def send_messages(root):
                    global color1
                    if root is None:
                        return
                    root.children.sort(reverse=True, key=mySort)
                    threads = []
                    for i in range(len(root.children)):
                        
                        print(f"Message: {root.value} --> {root.children[i].value}")
                        ini_lat,ini_long=get_coordinates(root.value)
                        fin_lat,fin_long=get_coordinates(root.children[i].value)
                       
                        
                        AntPath([(ini_lat,ini_long),(fin_lat,fin_long)], delay=400, dash_array=[30,15], color=color1, weight=3).add_to(my_map1)
                        
                        marker2=folium.Marker([fin_lat,fin_long],icon=folium.Icon(icon='fa-laptop',color='green',angle=0, prefix='fa'),popup=root.children[i].value,tooltip=root.children[i].value).add_to(my_map1)
                        sleep(5)
                        my_map1.save("map.html")
                        webbrowser.open("map.html")
                        color1 = message_colors.pop(0)
                        #print("")
                        thread = Thread(target=send_messages, args=(root.children[i],))
                        threads.append(thread)
                        thread.start()
                        
                    for thread in threads:
                        thread.join()          

                color1 = "red"
                add_markers_and_connections(root)
                return my_map1
               
            tree_root = create_tree(originator, network)
            
            # Visualize connections on map
            connections_map = visualize_connections_on_map(tree_root, network)
            connections_map.save("mapsfin.html")
            webbrowser.open("mapsfin.html")
    
        
        submit_button=Button(root1, text="Submit",state="disabled",bg="#02FFD0",fg="#010B50")
        submit_button.place(x=500,y=300)
        map_button=Button(root1,text='View Map',command=map_view,state='normal',bg="#02FFD0",fg="#010B50")
        map_button.place(x=800,y=300)
        create_location_text_box()
        root1.mainloop()








    num_computers_label=Label(root, text="Number of Computers:",font=("britannic bold",25),bg="#010B50",fg="#02FFD0")
    num_computers_label.place(x=400,y=100)
    num_computers_entry=Entry(root,font=("britannic bold",20),bg="#02FFD0",fg="#010B50")
    num_computers_entry.place(x=800,y=110)
    originator_label=Label(root,text="Enter the Originator location:",font=("britannic bold",25),fg="#02FFD0",bg="#010B50")
    originator_label.place(x=400,y=200)
    originator_entry=Entry(root,font=("britannic bold",20),bg="#02FFD0",fg="#010B50")
    originator_entry.place(x=900,y=210)
    create_button=Button(root, text="Enter",bg="#02FFD0",fg="#010B50",width=15,height=4, command=combined_function)
    create_button.place(x=700,y=300)
    root.mainloop()    
num_computers=0
counter=1
network={}
computer_data={}
global counter,num_computers,network,computer_data
bglbl = Label(splash_screen,bg="#151B54",height=70,width=1000)
bglbl.place(x=0,y=0)
lblvideo = Label(splash_screen)
lblvideo.pack()

player = tkvideo("Starting video.mp4",lblvideo,loop=2,size=(1500,800))
player.play()
splash_screen.after(15000 , second_window)
splash_screen.mainloop()