import math
import customtkinter as ctk
import tkinter.messagebox as tkmb
from tkinter import *
from tkinter import messagebox

global P, r, t, i, A

def mainMenu():
    def valueGet():
        P = entAmount.get().strip()
        r = entRate.get().strip()
        t = entTime.get().strip()
        if  P != "" and r != "" and t != "":
            if P.isnumeric() and r.isnumeric() and t.isnumeric():
                if float(P) > 0 and float(r) > 0 and float(t) > 0:
                    P = float(entAmount.get().strip())
                    r = float(entRate.get().strip())/100
                    t = float(entTime.get().strip())
                    i = r/12
                    return P, r, t, i
                else:
                    b = "Invalid input. Please enter a number above zero."
                    msgError.configure(text=b)
            else:
                b = "Invalid input. Please enter a value."
                msgError.configure(text=b)
        else:
            b = "Invalid input. Please enter a value."
            msgError.configure(text=b)


    def changeMode(a):
        if a == "Dark":
            ctk.set_appearance_mode('dark')
        else:
            ctk.set_appearance_mode('light')

    def calculateSimple():
        P, r, t, i = valueGet()
        interest_type = "simple"
        A = round(P * (1 + r * t),2)
        printOut(interest_type, A, P, r, t, i)
    
    def calculateCompound():
        P, r, t, i = valueGet()
        interest_type = "compound"
        A = round(P* math.pow((1+r),t),2)
        printOut(interest_type, A, P, r, t, i)
    
    def calculateBond():
        P, r, t, i = valueGet()
        interest_type = "bond"
        A = round((i*P)/(1 - math.pow((1+i),(-t))), 2)
        printOut(interest_type, A, P, r, t, i)

    def printOut(interest_type, A, P, r, t, i):
        if interest_type == "bond":
            message = (f'''===========<//>===========
For your bond of
R{round(P,2)},
at the rate of {round((i * 12) * 100,2)}%
over {round(t,2)} months,
Your monthly repayment is
R{A}
===========<//>===========''')
        else:
            interest = round(A - P, 2)
            message = (f'''===========<//>===========
You invested R{round(P,2)},
at the rate of {round((r)*100,2)}%,
for {round(t,2)} years,
using the {interest_type}
interest method.
Your intrest amounted to
R{interest}.
Your total amounted to
R{A}
===========<//>===========''')
        txtBalance.delete("1.0","end")
        txtBalance.insert(INSERT ,message)

    master = ctk.CTk()
    master.title('FinTrack')
    master.geometry("610x750")

    frmHugAll = ctk.CTkFrame(master)
    frmHugAll.grid(row=3, columnspan=2, padx=20, pady=20)
    
    lblTitle = ctk.CTkLabel(master, text='FinTrack', font=('Arial Bold', 20))
    lblTitle.grid(row=0, column=0, pady=10, padx=10)


    # Intrest
    frmHugDepo = ctk.CTkFrame(frmHugAll)
    frmHugDepo.grid(padx=20, pady=20, row=0, column=0)

    frmDeposit = ctk.CTkLabel(frmHugDepo, text='Insert values here', font=('Arial Bold', 15))
    frmDeposit.grid(padx=10, pady=5, row=0, column=0)

    lblAmount = ctk.CTkLabel(frmHugDepo, text='Amount')
    lblAmount.grid(row=1, column=0, padx=10, pady=5)
    entAmount = ctk.CTkEntry(frmHugDepo)
    entAmount.grid(row=1, column=1, padx=10, pady=5)
    lblAmount2 = ctk.CTkLabel(frmHugDepo, text='Amount')
    lblAmount2.grid(row=1, column=2, padx=10, pady=5)
    
    lblRate = ctk.CTkLabel(frmHugDepo, text='Rate')
    lblRate.grid(row=2, column=0, padx=10, pady=5)
    entRate = ctk.CTkEntry(frmHugDepo)
    entRate.grid(row=2, column=1, padx=10, pady=5)
    lblRate2 = ctk.CTkLabel(frmHugDepo, text='Rate')
    lblRate2.grid(row=2, column=2, padx=10, pady=5)

    lblTime = ctk.CTkLabel(frmHugDepo, text='Time (years)')
    lblTime.grid(row=3, column=0, padx=10, pady=5)
    entTime = ctk.CTkEntry(frmHugDepo)
    entTime.grid(row=3, column=1, padx=10, pady=5)
    lblTime2 = ctk.CTkLabel(frmHugDepo, text='Time (months)')
    lblTime2.grid(row=3, column=2, padx=10, pady=5)

    msgError = ctk.CTkLabel(master, text=' ')
    msgError.grid(row=1, column=1, pady=20, padx=20)

    btnDeposit = ctk.CTkButton(frmHugDepo, text='Simple', command=lambda: calculateSimple())
    btnDeposit.grid(row=4, column=0, padx=10, pady=10)
    btnDeposit = ctk.CTkButton(frmHugDepo, text='Compund', command=lambda: calculateCompound())
    btnDeposit.grid(row=4, column=1, padx=10, pady=10)
    btnDeposit = ctk.CTkButton(frmHugDepo, text='Bond', command=lambda: calculateBond())
    btnDeposit.grid(row=4, column=2, padx=10, pady=10)


    # Balance
    frmHugBal = ctk.CTkFrame(frmHugAll)
    frmHugBal.grid(padx=20, pady=20, row=1, column=0, rowspan=3)

    txtBalance = ctk.CTkTextbox(frmHugBal)
    txtBalance.grid(row=2, columnspan=3, padx=10, pady=10)

    drpMode = ctk.CTkComboBox(master, values=['Light','Dark'], command=changeMode)
    drpMode.grid(row=0, column=1, pady=20, padx=20)


    master.mainloop()


if __name__ == "__main__":
    mainMenu()