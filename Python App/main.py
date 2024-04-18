from user_info import write_transaction_to_file, user, sign_loop
from financial_code import finance_loop

# Increase Balance function
def increaseBalance(amount):
    
    #print('+Bal2')
    user.balance += amount
    write_transaction_to_file(amount, 'Deposit')
    displayBalance()

# Decrease Balance function
def decreaseBalance(amount):
    
    #print('-Bal2')
    if user.balance > amount:
        user.balance -= amount
        write_transaction_to_file(amount, 'Withdrawal')
        displayBalance()
    else:
        print('''You have insufficient funds for
this transaction.

==============<//>==============
Please check your current balance
before withdrawing''')

# Display balance function
def displayBalance():
    #print('CurrBal')
    print(f'The current balance for {user.name.title()} is R{round(user.balance,2)}')

# Transaction Block function
def transactionBlock():
    user_ans = input()
    #print('TransBlock - start')
    if user_ans == '1':
        #print('+Bal1')
        # While loops check if the user inputs the correct data type
        while True:
            try:
                user_amount = float(input('Please insert amount to be deposited: '))
                if user_amount > 0:
                    increaseBalance(user_amount)
                    break
                else:
                    print("Invalid input. Please enter a number above zero.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        

    elif user_ans == '2':
        #print('-Bal1')
        while True:
            try:
                user_amount = float(input('Please insert amount to be withdrawn: '))
                if user_amount > 0:
                    decreaseBalance(user_amount)
                    break
                else:
                    print("Invalid input. Please enter a number above zero.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        

    elif user_ans == '3':
        #print('Fin1')
        finance_loop()

    elif user_ans == '4':
        displayBalance()
    else:
        print('''Please choose one of the options
displayed above.''')
        transactionBlock()
    #print('TransBlock - end')
    
    trans_loop()

# Transaction Loop function
def trans_loop():

    while True:
        user_ans = input('''
==============<//>==============
Would you like to make a
transaction? (y/n) 
>>> ''').lower()
        if user_ans in ['y', 'yes']:
            print('''
==============<//>==============
Please select one of the
options below:
==============<//>==============

1) Deposit into your account
2) Withdraw from your account
3) Financial Calculator
4) Display current balance''')
            transactionBlock()
        elif user_ans in ['no', 'n']: 
            while True:
                user_ans = input('''Would you like to log out? (y/n)
>>> ''').lower()
                if user_ans in ['y', 'yes']:
                    print('Logging you out...')
                    welcome()
                elif user_ans in ['no', 'n']:
                    mainCode()
                else: # Break point if the user inputs the wrong option
                    print('Please choose one of the options above.')
        else: # Break point if the user inputs the wrong option
            print('Please choose one of the options above.')

# Main code function
def mainCode():
    
    #print('Main')
    print(f'''==============<//>==============
Hi🖐, {user.name.title()}!
==============<//>==============
How can we help you today? ''')
    trans_loop()

# Welcom function
def welcome():
    print(f'''==============<//>==============
---------Welcome to the---------
------------FinTrack------------
----------Banking App.----------
==============<//>==============
''')
    sign_loop()
    print(f"The current balance of {user.name.title()} is: R{user.balance}")
    mainCode()

if __name__ == "__main__":   
    welcome()