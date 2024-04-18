import math

# Main loop
def finance_loop():
    print('''
==============<//>==============
In this app, you are able to calculate
the Interest on your Investment and
monthly Repayment on your Bond.''')
    choice_loop()

# Calculator start loop || Point where user decides what to calculate
def choice_loop():
    while True:
        user_ans = input('''
==============<//>==============
Which one would you like to calculate?
1) Interest on Investment
2) Repayment of Bond
3) Return to main
''')
        if user_ans == '1' or user_ans.lower() in ['investment', 'interest']:
            invest_loop()
        elif user_ans == '2' or user_ans.lower() in ['bond', 'repayment']:
            bond_loop()
        elif user_ans == '3' or user_ans.lower() in ['return', 'main']:
            return
        else:
            print('''
==============<//>============== 
Please choose on of the options
displayed above''')     

# Investment loop || Calculates interest and total investment
def invest_loop():
    print('''
==============<//>==============''')
    # While loops check if the user inputs the correct data type
    while True:
            try:
                P = float(input('How much would you like to invest? (in rands): ' ))
                # If statement checks if the user inputs a value above zero
                if P > 0:
                    break
                else:
                    print("Invalid input. Please enter a number above zero.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    while True:
            try:
                t = float(input('How long is the investment? (in years): '))
                if t > 0:
                    break
                else:
                    print("Invalid input. Please enter a number above zero.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    while True:
            try:
                r = float(input('What is the interest rate? (in %): ')) / 100
                if r > 0:
                    break
                else:
                    print("Invalid input. Please enter a number above zero.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    # Gives the user an option to choose between simple or compund interest
    interest_type = input('''Which type of interest will it be?
Simple or Compound:
''')
    while True:
        try:
            if interest_type.lower() == 'simple' :
                A = round(P * (1 + r * t),2) # Simple interest calculation
                break
            elif interest_type.lower() == 'compound':
                A = round(P* math.pow((1+r),t),2) # Compound interest calculation
                break
            else: # Break point if user does not choose simple or compund
                print('''
==============<//>==============   
Please choose on of the options
displayed above''')
        except:
            print('''
==============<//>==============   
Please choose on of the options
displayed above''')
            
    interest = round(A - P, 2)
    print(f'''
==============<//>==============
You invested R{round(P,2)}, at the rate of {round((r)*100,2)}%, for {round(t,2)} years,
using the {interest_type} interest method.
Your intrest amounted to R{interest}.
Your total amounted to R{A}''')
    end_choice_loop()

# Bond loop || Calculates the monthly repayment of the bond
def bond_loop():
    print('''
==============<//>==============''')
    # While loops check if the user inputs the correct data type
    while True:
        try:
            P = float(input('How much is the bond? (in rands): '))
            # If statement checks if the user inputs a value above zero
            if P > 0:
                break
            else:
                print("Invalid input. Please enter a number above zero.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            n = float(input('How long is the repayment? (in months): '))
            if n > 0:
                break
            else:
                print("Invalid input. Please enter a number above zero.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            i = ((float(input('What is the interest rate? (in %): ')) / 100)/12)
            if i > 0:
                break
            else:
                print("Invalid input. Please enter a number above zero.")    
        except ValueError:
            print("Invalid input. Please enter a number.")

    repayment = round((i*P)/(1 - math.pow((1+i),(-n))), 2) # Repayment calculation

    print(f'''
==============<//>==============
For your bond of R{round(P,2)} at the rate of {round((i * 12) * 100,2)}% over {round(n,2)} months,
Your monthly repayment is R{repayment}''')
    end_choice_loop()

# End choice loop || Asks if user would like to calculate another investment or bond   
def end_choice_loop():
    user_ans = input('''
==============<//>==============
Would you like to do another calculation?
(y/n): ''').lower()
    if user_ans in ['y', 'yes']:
        choice_loop()
    elif user_ans in ['n', 'no']:
        return

if __name__ == "__main__":   
    finance_loop()