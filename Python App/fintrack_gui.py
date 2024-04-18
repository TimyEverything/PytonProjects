from customtkinter import *
from PIL import Image


app = CTk()
app.title('FinTrack App')
app.geometry('500x500')
app._apply_appearance_mode(set_default_color_theme(color_string="blue"))

#bank_logo = CTkImage(dark_image=Image.open('./images/logo.png'),size= (100,100))
#logo_label = CTkLabel(master= app, image=bank_logo,text= None)
#logo_label.pack(ipadx = 10, ipady= 10)

#sign_in_btn = CTkButton(master=app, corner_radius=100, text='Sign in')
#sign_in_btn.pack(padx = 10, pady = 10)

#dark_mode_btn = CTkSwitch(master=app, text='Dark mode')
#dark_mode_btn.pack(padx = 10, pady = 10)


class App(CTk()):
    def __init__(self, title, size):
        self.title('FinTrack App')
        self.geometry('500x500')

        self.mainLoop()


App()