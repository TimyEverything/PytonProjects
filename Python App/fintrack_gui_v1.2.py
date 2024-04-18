import customtkinter as ctk
import tkinter.messagebox as tkmb
import PIL.Image
import os
from tkinter import *
from tkinter import messagebox


def createPasswordGUI(name:str, surname:str, id:str):
    master = ctk.CTk()
    master.title("FinTrack")
    master.geometry("450x600+300+100")

    def submit():
        a = e1.get().strip()
        b = e2.get().strip()
        if not a == "" and not b == "":
            if a == b:
                c = createAccount(name, surname, id, b)
                tkmb.showinfo("Credentials:", "Account Number: "+c+"\nPassword: "+b)
                master.destroy()
                mainMenu()
            else:
                tkmb.showerror('Error', 'Invalid Input: Passwords do not match')
        else:
            tkmb.showerror('Error', 'Invalid Input: Entry fields cannot be left empty.')

    def back():
        master.destroy()
        signUp()

    def show_and_hide():
        if e2.cget('show') == '*':
            e2.configure(show='')
            e1.configure(show='')
        else:
            e2.configure(show='*')
            e1.configure(show='*')

    lblC = ctk.CTkLabel(master, text='CREATE PASSWORD', font=('Helvetica bold', 20))
    lblC.grid(row=0, padx=20, pady=20, columnspan=2)

    IMAGE_PATH = 'FinTrack.png'

    your_image = ctk.CTkImage(light_image=PIL.Image.open(os.path.join(IMAGE_PATH)), size=(200, 200))
    label = ctk.CTkLabel(master=master, image=your_image, text='').grid(row=1, columnspan=2, padx=10, pady=10)

    frmHug = ctk.CTkFrame(master)
    frmHug.grid(row=2, padx=20, pady=20, columnspan=2)

    frmPassword = ctk.CTkLabel(frmHug, text='Password')
    frmPassword.grid(row=0, column=0, padx=80, pady=20)

    e1 = ctk.CTkEntry(frmHug, show='*')
    e1.grid(row=0, padx=20, pady=20, column=1)

    frmConfirm = ctk.CTkLabel(frmHug, text='Confirm Password')
    frmConfirm.grid(row=1, padx=20, pady=20, column=0)

    e2 = ctk.CTkEntry(frmHug, show='*')
    e2.grid(row=1, padx=20, pady=20, column=1)

    cbxShowPassword = ctk.CTkCheckBox(frmHug, text="Show Password", fg_color='red', font=('verdana', 11), command=show_and_hide)
    cbxShowPassword.grid(column=1, row=2, padx=20, pady=10)

    btnBack = ctk.CTkButton(master, text="Cancel", command=back)
    btnBack.grid(column=0, row=3, padx=20, pady=20)

    btnSubmit = ctk.CTkButton(master, text="Submit", command=submit)
    btnSubmit.grid(column=1, row=3, padx=20, pady=20)

    master.mainloop()

def generatePasswordGUI(name: str, surname: str, id: str):
    master = ctk.CTk()
    master.title("FinTrack")
    master.geometry("450x250+300+100")



    def generate():
        a = id[slice(6, 10)]
        b = name[slice(0, 1)]
        c = surname[slice(0,3)]

        d = a+c+b

        lblG.configure(text=d, font=('Helvetica bold', 20))

        return d

    def submit():
        passW = generate()
        c = createAccount(name, surname, id, passW)
        tkmb.showinfo("Credentials:", "Account Number: " + c + "\nPassword: " + passW)
        master.destroy()
        mainMenu()

    def back():
        master.destroy()
        signUp()

    lblC = ctk.CTkLabel(master, text='GENERATED PASSWORD', font=('Helvetica bold', 20))
    lblC.grid(row=0, padx=20, pady=20, columnspan=2)

    frmConrain= ctk.CTkFrame(master)
    frmConrain.grid(row=1, columnspan=2, padx=20, pady=20)

    lblG = ctk.CTkLabel(frmConrain)
    lblG.grid(padx=20, pady=20)
    generate()

    btnBack = ctk.CTkButton(master, text="Cancel", command=back)
    btnBack.grid(column=0, row=2, padx=38, pady=20)

    btnSubmit = ctk.CTkButton(master, text="Submit", command=submit)
    btnSubmit.grid(column=1, row=2, padx=38, pady=20)



    master.mainloop()

def signUp():
    master = ctk.CTk()
    master.title("FinTrack")
    # master.geometry("500x600")
    master.geometry("450x600+300+100")

    def submitCreate():
        a = e1.get()
        b = e2.get()
        c = e3.get()
        if a.strip() == "" or b.strip() == "" or c.strip() == "":
            tkmb.showerror("Error", "Invalid Input: Entry fields cannot be left empty.")
        else:
            if containsNumber(a) or containsNumber(b) or not c.isnumeric():
                tkmb.showerror("Error", "Invalid Input: Name and Surname fields need to be in words. ID number must be numeric.")
            else:
                if not len(c) == 13:
                    tkmb.showerror("Error", "Invalid Input: ID number is 13 numbers.")
                else:
                    master.destroy()
                    createPasswordGUI(a, b, c)

    def submitGenerate():
        a = e1.get().strip()
        b = e2.get().strip()
        c = e3.get().strip()
        if a == "" or b == "" or c == "":
            tkmb.showerror("Error", "Invalid Input: Entry fields cannot be left empty.")
        else:
            if containsNumber(a) or containsNumber(b) or not c.isnumeric():
                tkmb.showerror("Error", "Invalid Input: Name and Surname fields need to be in words. ID number must be numeric.")
            else:
                if not len(c) == 13:
                    tkmb.showerror("Error", "Invalid Input: ID number is 13 numbers.")
                else:
                    master.destroy()
                    generatePasswordGUI(a, b, c)

    def submitBack():
        master.destroy()
        welcomeScreen()

    lblC = ctk.CTkLabel(master, text='REGISTER', font=('Helvetica bold', 20))
    # lblC.config(font=('Helvetica bold', 20))
    lblC.grid(row=0, padx=20, pady=20, columnspan=3)

    IMAGE_PATH = 'FinTrack.png'

    your_image = ctk.CTkImage(light_image=PIL.Image.open(os.path.join(IMAGE_PATH)), size=(200, 200))
    label = ctk.CTkLabel(master=master, image=your_image, text='').grid(row=1, columnspan=3, padx=10, pady=10)

    frmContain = ctk.CTkFrame(master)
    frmContain.grid(row=2, padx=20, pady=20, columnspan=3)

    lblname = ctk.CTkLabel(frmContain, text='Name')
    lblname.grid(row=0, column=0, padx=20, pady=20)

    e1 = ctk.CTkEntry(frmContain)
    e1.grid(row=0, column=1, padx=20, pady=20)

    lblSurname = ctk.CTkLabel(frmContain, text='Surname')
    lblSurname.grid(column=0, row=1, padx=20, pady=20)

    e2 = ctk.CTkEntry(frmContain)
    e2.grid(column=1, row=1, padx=20, pady=20)

    lblID = ctk.CTkLabel(frmContain, text='ID Number')
    lblID.grid(row=2, column=0, padx=20, pady=20)

    e3 = ctk.CTkEntry(frmContain)
    e3.grid(row=2, column=1, padx=20, pady=20)

    b1 = ctk.CTkButton(master, text="Generate Password",command=submitGenerate)
    b1.grid(column=1, row=3, padx=5, pady=15)

    b2 = ctk.CTkButton(master, text="Create Password", command=submitCreate)
    b2.grid(column=2, row=3, padx=5, pady=15)

    b1 = ctk.CTkButton(master, text="Back", command=submitBack)
    b1.grid(column=0, row=3, padx=5, pady=15)

    master.mainloop()

def welcomeScreen():
    master = ctk.CTk()
    master.title("FinTrack")
    master.geometry("450x510+300+100")
    #master.geometry("500x600")

    def submitLog():
        master.destroy()
        logIn()

    def submitReg():
        master.destroy()
        signUp()

    def submitExit():
        master.destroy()

    def changeMode(a):
        if a == "Dark":
            ctk.set_appearance_mode('dark')
        else:
            ctk.set_appearance_mode('light')

    lblC = ctk.CTkLabel(master=master, text='FinTrack', font=('Helvetica bold', 20))
    lblC.pack( padx=20, pady=20)

    #frImage = ctk.CTkFrame(master).pack(pady=20)
    IMAGE_PATH = 'FinTrack.png'

    your_image = ctk.CTkImage(light_image=PIL.Image.open(os.path.join(IMAGE_PATH)), size=(200, 200))
    label = ctk.CTkLabel(master=master, image=your_image, text='').pack(padx=20, pady=20)

    drpMode = ctk.CTkComboBox(master, values=['Light', 'Dark'], command=changeMode).pack(padx=20, pady=10)

    b1 = ctk.CTkButton(master=master, text="Log In", command= submitLog)
    b1.pack(padx=20, pady=10)

    b2 = ctk.CTkButton(master=master, text="Register", command=submitReg)
    b2.pack(padx=20, pady=10)

    b2 = ctk.CTkButton(master=master, text="Exit", command=submitExit)
    b2.pack(padx=20, pady=10)

    master.mainloop()

def logIn():
    master = ctk.CTk()
    master.title("FinTrack")
    master.geometry("450x600+300+100")


    def back():
        master.destroy()
        welcomeScreen()

    def show_and_hide():
        if entPassword.cget('show') == '*':
            entPassword.configure(show='')
        else:
            entPassword.configure(show='*')

    def submit():
        if entAccount.get() == '' or entPassword.get() == '':
            tkmb.showerror("Error", "Invalid Input: Entry fields cannot be left empty")
        else:
            account = entAccount.get()
            password = entPassword.get()
            check = validateLogIns(account, password)
            if check:
                global accountNr
                accountNr = str(account)
                global path
                path = "TransactionLogs/" + accountNr + TRANSINFO
                master.destroy()
                mainMenu()
            else:
                tkmb.showerror("Error", "Invalid Details: Please enter correct details")


    lblC = ctk.CTkLabel(master, text='LOG IN', font=('Helvetica bold', 20))
    lblC.grid(row=0, padx=20, pady=20, columnspan=2, sticky=W + E)

    IMAGE_PATH = 'FinTrack.png'

    your_image = ctk.CTkImage(light_image=PIL.Image.open(os.path.join(IMAGE_PATH)), size=(200, 200))
    label = ctk.CTkLabel(master=master, image=your_image, text='').grid(padx=20, pady=20, row=1, columnspan=2)

    frHug = ctk.CTkFrame(master)
    frHug.grid(row=2, columnspan=2, padx=50)

    lblPasswordC = ctk.CTkLabel(frHug, text='Account Number')
    lblPasswordC.grid(row=1, column=0, padx=20, pady=20)

    entAccount = ctk.CTkEntry(frHug)
    entAccount.grid(row=1, column=1, padx=20, pady=20)

    lblPasswordC = ctk.CTkLabel(frHug, text='Password')
    lblPasswordC.grid(column=0, row=2, padx=20, pady=20)

    entPassword = ctk.CTkEntry(frHug, show="*")
    entPassword.grid(column=1, row=2, padx=20, pady=20)

    cbxShowPassword = ctk.CTkCheckBox(frHug, text="Show Password", fg_color='red',font=('verdana', 11), command=show_and_hide)
    cbxShowPassword.grid(column=1, row=3, padx=60, pady=10)

    b1 = ctk.CTkButton(master, text="Back", command=back)
    b1.grid(column=0, row=3, padx=20, pady=20)

    b2 = ctk.CTkButton(master, text="Submit", command=submit)
    b2.grid(column=1, row=3, padx=10, pady=20)

    master.mainloop()


def withdrawal(amount:str):
    balance = getBalance()
    if (float(amount) > float(balance)):
        a = ["red","************************\nAmount you wish to withdraw exceeds\n your balance. Please \nCheck your balance?\n************************"]
        return a
    else:
        withdrawlAmount(amount)
        a = ["green", "************************\nWITHDRAWAL SUCCESSFUL\n************************"]
        return a

def deposit(amount: str):
    if float(amount) < 10:
        a = ["red", "************************\nDeposit R10 or More!!!\n************************"]
        return a
    else:
        depositSet(amount)
        a = ["green", "***********************\nDEPOSIT SUCCESSFUL\n***********************"]
        return a

def mainMenu():
    master = ctk.CTk()
    master.title('FinTrack')
    master.geometry("610x750+300+100")

    def submitDeposit():
        a = entDeposit.get().strip()
        if not a == "":
            if a.isnumeric():
                if int(a) % 10 == 0:
                    message = deposit(a)
                    msgError.configure(text=message[1])
                    if message[0] == "green":
                        entDeposit.delete(0 ,'end')
                else:
                    b = "************************\nDeposit 200s, 100s, \n50s, 20s or 10s only.\nNo Coins Allowed!!!\n************************"
                    msgError.configure(text=b)
            else:
                b = "*****************\nEnter numbers only!\n*****************"
                msgError.configure(text=b)
        else:
            b = "************************\nDeposit field empty!!!\n*************************"
            msgError.configure(text=b)

    def submitWithdrawal():
        a = entWithdraw.get().strip()
        if not a == "":
            if a.isnumeric():
                if int(a) % 10 == 0 and int(a) >= 10:
                    message = withdrawal(a)
                    msgError.configure(text=message[1])
                    if message[0] == "green":
                        entWithdraw.delete(0 ,'end')
                else:
                    b = "************************\nWithdraw 200s, 100s, \n50s, 20s or 10s only.\nNo Coins Can Be \nWithdrawn!\n************************"
                    msgError.configure(text=b)
            else:
                b = "*****************\nEnter numbers only!\n*****************"
                msgError.configure(text=b)
        else:
            b = "************************\nWithdrawal field empty!!!\n************************"
            msgError.configure(text=b)

    def submitBalance():
        balance = balanceW()
        txtBalance.delete("1.0","end")
        txtBalance.insert(INSERT ,balance)

    def logUit():
        messagebox.showinfo("Alert", "Logging Out!!!")
        master.destroy()
        welcomeScreen()

    def changeMode(a):
        if a == "Dark":
            ctk.set_appearance_mode('dark')
        else:
            ctk.set_appearance_mode('light')


    #frmTitle = ctk.CTkFrame(master).grid(row=0, columnspan=2, pady=20)

    lblTitle = ctk.CTkLabel(master, text='FinTrack', font=('Arial Bold', 20))
    lblTitle.grid(row=0, column=0, pady=20, padx=10)

    IMAGE_PATH = 'FinTrack.png'

    your_image = ctk.CTkImage(light_image=PIL.Image.open(os.path.join(IMAGE_PATH)), size=(200, 200))
    label = ctk.CTkLabel(master=master, image=your_image, text='').grid(padx=20, pady=20, row=1, column=0)

    frmHugAll = ctk.CTkFrame(master)
    frmHugAll.grid(row=2, columnspan=2, padx=20, pady=20)

    # Deposit
    frmHugDepo = ctk.CTkFrame(frmHugAll)
    frmHugDepo.grid(padx=20, pady=20, row=1, column=0)

    frmDeposit = ctk.CTkLabel(frmHugDepo, text='Deposit', font=('Arial Bold', 15))
    frmDeposit.grid(padx=10, pady=5, row=0, column=0)

    lblDeposit = ctk.CTkLabel(frmHugDepo, text='Amount')
    lblDeposit.grid(row=1, column=0, padx=10, pady=5)

    entDeposit = ctk.CTkEntry(frmHugDepo)
    entDeposit.grid(row=1, column=1, padx=10, pady=5)

    btnDeposit = ctk.CTkButton(frmHugDepo, text='Submit', command=submitDeposit)
    btnDeposit.grid(row=2, column=1, padx=10, pady=10)

    # Withdrawal
    frmHugWith = ctk.CTkFrame(frmHugAll)
    frmHugWith.grid(padx=20, pady=20, row=0, column=0)

    frmWithdraw = ctk.CTkLabel(frmHugWith, text='Withdrawal', font=('Arial Bold', 15))
    frmWithdraw.grid(padx=10, pady=5, row=0, column=0)

    lblWithdraw = ctk.CTkLabel(frmHugWith, text='Amount')
    lblWithdraw.grid(row=1, column=0, padx=10, pady=5)

    entWithdraw = ctk.CTkEntry(frmHugWith)
    entWithdraw.grid(row=1, column=1, padx=10, pady=5)

    btnWithdraw = ctk.CTkButton(frmHugWith, text='Submit', command=submitWithdrawal)
    btnWithdraw.grid(row=2, column=1, pady=10, padx=10)

    # Balance
    frmHugBal = ctk.CTkFrame(frmHugAll)
    frmHugBal.grid(padx=20, pady=20, row=0, column=1, rowspan=2)

    frmBalance = ctk.CTkLabel(frmHugBal, text='Balance', font=('Arial Bold', 15))
    frmBalance.grid(row=0, column=0, padx=10, pady=5)

    btnRefresh = ctk.CTkButton(frmHugBal, text='Display Balance', command=submitBalance)
    btnRefresh.grid(row=1, padx=10, pady=5)

    txtBalance = ctk.CTkTextbox(frmHugBal)
    txtBalance.grid(row=2, columnspan=2, padx=10, pady=10)

    btnLogOut = ctk.CTkButton(master, text='Log Out', command=logUit)
    btnLogOut.grid(row=3, columnspan=2, pady=20, padx=20)

    drpMode = ctk.CTkComboBox(master, values=['Light','Dark'], command=changeMode)
    drpMode.grid(row=0, column=1, pady=20, padx=20)

    msgError = ctk.CTkLabel(master, text=' ')
    msgError.grid(row=1, column=1, pady=20, padx=20)

    master.mainloop()


mainMenu()