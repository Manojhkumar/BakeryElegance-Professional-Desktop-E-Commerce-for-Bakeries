import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw
import login

win1 = tk.Tk()
win1.title("Kikis Treats")
win1.geometry("1500x800")
win1.configure(bg="#552800")
win1.resizable(False, False)

#---------------------------------------------------OPENING PAGE-------------------------------------------------------

url = "C:\\Users\\DELL\\OneDrive\\Desktop\\proj\\proj 2\\logo1.png"
img = tk.PhotoImage(file=url) 
tk.Label(win1, image=img,width=500,height=500, bg='black',fg='black').place(x=100, y=160)

sideframe = tk.Frame(win1, width=790,height=150,bg="#552800")
sideframe.place(x=850,y=60) 

home = tk.Button(sideframe,width=0,height=0, text="Home", fg="#F2D3B7",bg="#552800",border=0,font=('italy',13)).place(x=60,y=20)
aboutus = tk.Button(sideframe,width=0,height=0, text="About us", fg="#F2D3B7",bg="#552800",border=0,font=('italy',13)).place(x=150,y=20)
review = tk.Button(sideframe,width=0,height=0, text="Review", fg="#F2D3B7",bg="#552800",border=0,font=('italy',13)).place(x=260,y=20)
chef = tk.Button(sideframe,width=0,height=0, text="Chef", fg="#F2D3B7",bg="#552800",border=0,font=('italy',13)).place(x=370,y=20)

order = tk.Button(win1,width=15,height=3, text="Order a cake", fg="#F2D3B7",bg="#552800",border=1,cursor='hand2',font=('italy',13),command=login.login)
order.place(x=700,y=390)

url1 = "C:\\Users\\DELL\\OneDrive\\Desktop\\proj\\proj 2\\logo3.png"
img1 = tk.PhotoImage(file=url1) 
tk.Label(sideframe, image=img1,width=50,height=50, bg='black',fg='black').place(x=480, y=5)


rsideframe = tk.Frame(win1, width=990, height=680,bg="#552800")
rsideframe.place(x=550,y=600)

cake = "C:\\Users\\DELL\\OneDrive\\Desktop\\proj\\proj 2\\choc1.png"
cakeimg = tk.PhotoImage(file=cake)
tk.Label(rsideframe, image=cakeimg, width=66, height=59,bg='#552800',fg='#552800').place(x=80,y=10)

cakee = tk.Label(rsideframe, text="Chocolate cake",width=15,bg="#552800",fg="#F2D3B7",font=("Italy",9)).place(x=60,y=80)
cakee1 = tk.Label(rsideframe, text="Chocolate,Sprinkles,Strawbery,Waffers",width=30,bg="#552800",fg="white",font=("Italy",7)).place(x=27,y=100)

desert = "C:\\Users\\DELL\\OneDrive\\Desktop\\proj\\proj 2\\desert1.png"    
cakeimg1 = tk.PhotoImage(file=desert)
tk.Label(rsideframe, image=cakeimg1, width=66, height=59,bg='#552800',fg='#552800').place(x=300,y=10)

desertt = tk.Label(rsideframe, text="Desert",width=15,bg="#552800",fg="#F2D3B7",font=("Italy",9)).place(x=280,y=80)
desertt1 = tk.Label(rsideframe, text="Chocolate,Sprinkles,Strawbery,Waffers",width=30,bg="#552800",fg="white",font=("Italy",7)).place(x=250,y=100)

donut = "C:\\Users\\DELL\\OneDrive\\Desktop\\proj\\proj 2\\donut1.png"
cakeimg2 = tk.PhotoImage(file=donut)
tk.Label(rsideframe, image=cakeimg2, width=66, height=59,bg='#552800',fg='#552800').place(x=550,y=10)

donut = tk.Label(rsideframe, text="Donuts",width=15,bg="#552800",fg="#F2D3B7",font=("Italy",9)).place(x=530,y=80)
donutt1 = tk.Label(rsideframe, text="Chocolate,Sprinkles,Strawbery,Waffers",width=30,bg="#552800",fg="white",font=("Italy",7)).place(x=490,y=100)

pastry = "C:\\Users\\DELL\\OneDrive\\Desktop\\proj\\proj 2\\pastry1.png"
cakeimg3 = tk.PhotoImage(file=pastry)
tk.Label(rsideframe, image=cakeimg3, width=66, height=59,bg='#552800',fg='#552800').place(x=770,y=10)

pastryy = tk.Label(rsideframe, text="Pastry",width=15,bg="#552800",fg="#F2D3B7",font=("Italy",9)).place(x=750,y=80)
pastryy1 = tk.Label(rsideframe, text="Chocolate,Sprinkles,Strawbery,Waffers",width=30,bg="#552800",fg="white",font=("Italy",7)).place(x=710,y=100)


#--------------------------------------------------------------------------------------------------------------------------
























win1.mainloop()















