import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw
import webpage 

signup_username = ''
signup_password = ''

def signup_1(parent):
    global signup_username, signup_password
    scrn1 = tk.Toplevel(parent)
    scrn1.title("Kikis Treats(SIGN UP)")
    scrn1.geometry("1500x800")
    scrn1.configure(bg="#552800")
    scrn1.resizable(False,False)
    url = "C:\\Users\\DELL\\OneDrive\\Desktop\\proj\\proj 2\\logo1.png"
    img = Image.open(url)
    img = ImageTk.PhotoImage(img)
    scrn1.logo_image = img
    tk.Label(scrn1, image=img,width=500,height=500, bg='#552800',fg='black').place(x=90, y=160)
    frame1 = tk.Frame(scrn1, width=352, height=352, bg="#F2D3B7")
    frame1.place(x=850, y=210)
    
    frame = tk.Frame(frame1, width=350, height=350, bg="#552800")
    frame.place(x=1, y=1)
    signin = tk.Label(frame, text="Sign Up", fg="#F2D3B7", bg="#552800", font=("times", 27,'bold'))
    signin.place(x=130, y=20)

    def on_enter(e):
        user1.delete(0, 'end')

    def on_leave(e):
        name = user1.get()
        if name=='':
            user1.insert(0, 'Username')
    user1 = tk.Entry(frame, width=25, border=0, bg="#552800", fg="white", font=("times", 14))
    user1.place(x=50, y=105)
    user1.insert(0, 'Username')
    user1.bind('<FocusIn>',on_enter)
    user1.bind('<FocusOut>',on_leave) 

    tk.Frame(frame, width=300, height=2, bg="grey").place(x=30, y=127)

#---------------------------------------------------------------------------------------------------
    def on_enter(e):
        pswd1.delete(0, 'end')

    def on_leave(e):
        name = pswd1.get()
        if name=='':
            pswd1.insert(0, 'Password')

    pswd1 = tk.Entry(frame, width=25, border=0, bg="#552800", fg="white", font=("times", 14))
    pswd1.place(x=50, y=170)
    pswd1.insert(0, 'Password')
    pswd1.bind('<FocusIn>',on_enter)
    pswd1.bind('<FocusOut>',on_leave)
    tk.Frame(frame, width=300, height=2, bg="grey").place(x=30, y=190)

#-----------------------------------------------------------------------------------------
#                                 SIGN UP ENTRY
#----------------------------------------------------------------------------------------
    def save_signup_entry():
        global signup_username, signup_password
        signup_username = user1.get()
        signup_password = pswd1.get()
        close_signup_page()
    def close_signup_page():
        scrn1.destroy()
    def on_enter(e):
        user1.delete(0, 'end')

    def on_leave(e):
        name = user1.get()
        if name=='':
            user1.insert(0, 'Enter your name')
# -----------------------------------------------------------------------------------------------------------

    tk.Button(frame, width=42, pady=5, text="Signup", bg='#F2D3B7', fg='black', border=0,font=("Comic Sans MS",9),command=save_signup_entry).place(x=32, y=220)
    label = tk.Label(frame,text="Dont have an account?",fg='white',bg='#552800',font=("italy", 9))
    label.place(x=85,y=270)


    signup = tk.Button(frame, width=6, text='Login', border=0, bg='#552800', cursor='hand2', fg='red',command=close_signup_page)
    signup.place(x=215, y=270)
#---------------------------------------design down---------------------------------------------------------------
    rsideframe = tk.Frame(scrn1, width=990, height=680,bg="#552800")
    rsideframe.place(x=550,y=600)

    cake = "C:\\Users\\DELL\\OneDrive\\Desktop\\proj\\proj 2\\choc1.png"
    cakeimg = Image.open(cake)
    cakeimg = ImageTk.PhotoImage(cakeimg)
    scrn1.logo_image1 = cakeimg
    tk.Label(rsideframe, image=cakeimg, width=66, height=59,bg='#552800',fg='#552800').place(x=80,y=10)
    
    cakee = tk.Label(rsideframe, text="Chocolate cake",width=15,bg="#552800",fg="#F2D3B7",font=("Italy",9)).place(x=60,y=80)
    cakee1 = tk.Label(rsideframe, text="Chocolate,Sprinkles,Strawbery,Waffers",width=30,bg="#552800",fg="white",font=("Italy",7)).place(x=27,y=100)

    desert = "C:\\Users\\DELL\\OneDrive\\Desktop\\proj\\proj 2\\desert1.png"    
    desertimg = Image.open(desert)
    desertimg = ImageTk.PhotoImage(desertimg)
    scrn1.logo_image2 = desertimg
    tk.Label(rsideframe, image=desertimg, width=66, height=59,bg='#552800',fg='#552800').place(x=300,y=10)

    desertt = tk.Label(rsideframe, text="Desert",width=15,bg="#552800",fg="#F2D3B7",font=("Italy",9)).place(x=280,y=80)
    desertt1 = tk.Label(rsideframe, text="Chocolate,Sprinkles,Strawbery,Waffers",width=30,bg="#552800",fg="white",font=("Italy",7)).place(x=250,y=100)

    donut = "C:\\Users\\DELL\\OneDrive\\Desktop\\proj\\proj 2\\donut1.png"
    donutimg = Image.open(donut)
    donutimg = ImageTk.PhotoImage(donutimg)
    scrn1.logo_image3 = donutimg
    tk.Label(rsideframe, image=donutimg, width=66, height=59,bg='#552800',fg='#552800').place(x=550,y=10)

    donut = tk.Label(rsideframe, text="Donuts",width=15,bg="#552800",fg="#F2D3B7",font=("Italy",9)).place(x=530,y=80)
    donutt1 = tk.Label(rsideframe, text="Chocolate,Sprinkles,Strawbery,Waffers",width=30,bg="#552800",fg="white",font=("Italy",7)).place(x=490,y=100)

    pastry = "C:\\Users\\DELL\\OneDrive\\Desktop\\proj\\proj 2\\pastry1.png"
    pastryimg = Image.open(pastry)
    pastryimg = ImageTk.PhotoImage(pastryimg)
    scrn1.logo_image4 = pastryimg
    tk.Label(rsideframe, image=pastryimg, width=66, height=59,bg='#552800',fg='#552800').place(x=770,y=10)

    pastryy = tk.Label(rsideframe, text="Pastry",width=15,bg="#552800",fg="#F2D3B7",font=("Italy",9)).place(x=750,y=80)
    pastryy1 = tk.Label(rsideframe, text="Chocolate,Sprinkles,Strawbery,Waffers",width=30,bg="#552800",fg="white",font=("Italy",7)).place(x=710,y=100)


#------------------------------------------design up--------------------------------------------------------------------------------

    sideframe = tk.Frame(scrn1, width=790,height=150,bg="#552800")
    sideframe.place(x=850,y=60) 

    home = tk.Button(sideframe,width=0,height=0, text="Home", fg="#F2D3B7",bg="#552800",border=0,font=('italy',13)).place(x=60,y=20)
    aboutus = tk.Button(sideframe,width=0,height=0, text="About us", fg="#F2D3B7",bg="#552800",border=0,font=('italy',13)).place(x=150,y=20)
    review = tk.Button(sideframe,width=0,height=0, text="Review", fg="#F2D3B7",bg="#552800",border=0,font=('italy',13)).place(x=260,y=20)
    chef = tk.Button(sideframe,width=0,height=0, text="Chef", fg="#F2D3B7",bg="#552800",border=0,font=('italy',13)).place(x=370,y=20)

    url1 = "C:\\Users\\DELL\\OneDrive\\Desktop\\proj\\proj 2\\logo3.png"
    urlimg = Image.open(url1)
    urlimg = ImageTk.PhotoImage(urlimg)
    scrn1.logo_image5 = urlimg

    tk.Label(sideframe, image=urlimg,width=50,height=50, bg='black',fg='black').place(x=480, y=5)

#-----------------------------------------------------------------------------------------------------------------


  


#----------------------------------------------Login-------------------------------------------------------------------


    
def login():    
    scrn0 = tk.Toplevel()
    scrn0.title("Kikis Treats(LOGIN)")
    scrn0.geometry("1500x800")
    scrn0.configure(bg="#552800")
    scrn0.resizable(False,False)

    
    url = "C:\\Users\\DELL\\OneDrive\\Desktop\\proj\\proj 2\\logo1.png"
    img = tk.PhotoImage(file=url) 
    tk.Label(scrn0, image=img,width=500,height=500, bg='#552800',fg='black').place(x=90, y=160)
    frame1 = tk.Frame(scrn0, width=352, height=352, bg="#F2D3B7")
    frame1.place(x=850, y=210)
    
    frame = tk.Frame(frame1, width=350, height=350, bg="#552800")
    frame.place(x=1, y=1)
    
    signin = tk.Label(frame, text="Sign in", fg="#F2D3B7", bg="#552800", font=("times", 27,'bold'))
    signin.place(x=130, y=20)

    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name = user.get()
        if name=='':
            user.insert(0, 'Username')
    user = tk.Entry(frame, width=25, border=0, bg="#552800", fg="white", font=("times", 14))
    user.place(x=50, y=105)
    user.insert(0, 'Username')
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave) 

    tk.Frame(frame, width=300, height=2, bg="grey").place(x=30, y=127)

#---------------------------------------------------------------------------------------------------
    def on_enter(e):
        pswd.delete(0, 'end')

    def on_leave(e):
        name = pswd.get()
        if name=='':
            pswd.insert(0, 'Password')

    pswd = tk.Entry(frame, width=25, border=0, bg="#552800", fg="white", font=("times", 14))
    pswd.place(x=50, y=170)
    pswd.insert(0, 'Password')
    pswd.bind('<FocusIn>',on_enter)
    pswd.bind('<FocusOut>',on_leave)
    tk.Frame(frame, width=300, height=2, bg="grey").place(x=30, y=190)
#--------------------------------------next face -------------------------------------------------------------
    def nextpage():
        if user.get()==signup_username and pswd.get()==signup_password:
            print("Login Successful")
            webpage.home()


#---------------------------------------------------------------------------------------------------
    tk.Button(frame, width=42, pady=5, text="Login", bg='#F2D3B7', fg='black', border=0,font=("Comic Sans MS",9),command=nextpage).place(x=32, y=220)
    label = tk.Label(frame,text="Dont have an account?",fg='white',bg='#552800',font=("italy", 9))
    label.place(x=85,y=270)


    signup = tk.Button(frame, width=6, text='Sign Up', border=0, bg='#552800', cursor='hand2', fg='red',command=lambda: signup_1(scrn0))
    signup.place(x=215, y=270)

#---------------------------------------design down---------------------------------------------------------------
    rsideframe = tk.Frame(scrn0, width=990, height=680,bg="#552800")
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


#------------------------------------------design up--------------------------------------------------------------------------------

    sideframe = tk.Frame(scrn0, width=790,height=150,bg="#552800")
    sideframe.place(x=850,y=60) 

    home = tk.Button(sideframe,width=0,height=0, text="Home", fg="#F2D3B7",bg="#552800",border=0,font=('italy',13)).place(x=60,y=20)
    aboutus = tk.Button(sideframe,width=0,height=0, text="About us", fg="#F2D3B7",bg="#552800",border=0,font=('italy',13)).place(x=150,y=20)
    review = tk.Button(sideframe,width=0,height=0, text="Review", fg="#F2D3B7",bg="#552800",border=0,font=('italy',13)).place(x=260,y=20)
    chef = tk.Button(sideframe,width=0,height=0, text="Chef", fg="#F2D3B7",bg="#552800",border=0,font=('italy',13)).place(x=370,y=20)

    url1 = "C:\\Users\\DELL\\OneDrive\\Desktop\\proj\\proj 2\\logo3.png"
    img1 = tk.PhotoImage(file=url1) 
    tk.Label(sideframe, image=img1,width=50,height=50, bg='black',fg='black').place(x=480, y=5)

#-----------------------------------------------------------------------------------------------------------------






















    scrn0.mainloop()




    
    

