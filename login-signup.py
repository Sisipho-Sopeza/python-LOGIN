from tkinter import *
from tkinter import messagebox

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1199x688+100+50")
        self.root.resizable(False, False)


        #Login Frame
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=330, y=150, width=500, height=400)


        #Ttle &Subtitle
        tittle= Label(Frame_login, text="Login Here", font=("Impact", 35,"bold"), fg="#6162ff", bg="white").place(x=90, y=30)
        subtittle = Label(Frame_login, text="Members login Area", font=("Goudy old style  ", 15, "bold"), fg="#1d1d1d", bg="white").place(x=90, y=100)


        #Username
        lbl_user = Label(Frame_login, text="Username", font=("Goudy old style  ", 15, "bold"), fg="grey",  bg="white").place(x=90, y=140)
        self.username = Entry(Frame_login,  font=("Goudy old style  ", 15), bg="#E7E6E6")
        self.username.place(x=90, y=170, width=320, height=35)


        #Password
        lbl_user = Label(Frame_login, text="Password", font=("Goudy old style  ", 15, "bold"), fg="grey",  bg="white").place(x=90, y=210)
        self.password = Entry(Frame_login, font=("Goudy old style  ", 15), bg="#E7E6E6")
        self.password.place(x=90, y=240, width=320, height=35)

        #Button
        forget = Button(Frame_login, text="forgot password?", cursor="hand2", bd=0, font=("Goudy old style ", 12), fg="grey",  bg="white").place(x=90, y=280)
        forget = Button(Frame_login,command=self.check_function,cursor="hand2", text="submit", bd=0, font=("Goudy old style ", 15), bg="#6162ff",fg="white").place(x=90, y=320, width=180, height=40)


    def check_function(self):
            if self.username.get()=="" or self.password.get()=="":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            elif self.username.get()!="Sisipho" or self.password.get()!="12345678":
                    messagebox.showerror("Error", "Invalid Username or Password", parent=self.root)
            else:
                messagebox.showInfo("welcome", f"welcome {self.username.get()}")





root=Tk()
obj = Login(root)
root.mainloop()