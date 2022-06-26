from hotel import *


ti=Tk()
ti.geometry()
ti.geometry("940x685+200+1")
ti.resizable(0,0)
ti.title("My Restaurant")


#============================================ Login page =======================================#
nametxt = StringVar()
passwordtxt = StringVar()
def loginadminpage():

    global usertxt
    global adminlabel
    # print(random.randrange(1 , 80 ))
    adminlabel = Label(ti, text="  User Login", padx=170, pady=15, fg="#e44134", font=("Sitka Text", 30, "bold"))
    adminlabel.grid(row=3, columnspan=5)
    # image_with()
    username9 = Label(ti, font=("Times New Roman", 15))
    username9.grid(row=2, column=0)
    # ===================================== Chef Restaurent======================================#
    chef_frame = Frame(ti, )
    chef_lbl = Label(chef_frame, image=chef_img, font=("Times New Roman", 15))
    chef_lbl.grid(row=3, column=0)
    chef_frame.place(x=0, y=140)
    chef_frame = Frame(ti, )
    chef_lbl = Label(chef_frame, image=chefr_img, font=("Times New Roman", 15))
    chef_lbl.grid(row=3, column=0)
    chef_frame.place(x=600, y=140)
    username = Label(ti, text="User Name:", padx=100, pady=20, font=("Times New Roman", 20))
    username.grid(row=4, column=1)
    usertxt = Entry(ti, textvariable=nametxt, width=20, font=("Arial", 18, "roman"))
    callback4 = ti.register(login_char_input)
    usertxt.configure(validate="key", validatecommand=(callback4, "%S"))
    usertxt.grid(row=4, column=2)
    username7 = Label(ti, text="Password:", padx=100, pady=20, font=("Times New Roman", 20))
    username7.grid(row=5, column=1)
    passtxt = Entry(ti, textvariable=passwordtxt, show="*", width=20, font=("Arial", 18, "roman"))
    passtxt.grid(row=5, column=2)
    buttonin = Button(ti, text="", image=signin_img, borderwidth=0, relief="solid", command=login)
    buttonin.grid(row=7, column=2, pady=10)
    buttonin = Button(ti, text="Create New Account?", image=signup_img, borderwidth=0, fg="red", compound=TOP,
    relief="solid", font=("Times New Roman", 12, "bold"), command=signup)
    buttonin.grid(row=7, column=1, pady=13)
    forget = Button(ti, text="Forgot your Password?", fg="red", borderwidth=0, relief="solid",
    font=("Times New Roman", 15, "roman"), command=forget_pass)
    forget.grid(row=8, column=2, )


loginadminpage()
mainloop()