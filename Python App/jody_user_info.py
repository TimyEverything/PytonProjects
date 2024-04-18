import os
from datetime import datetime
import hashlib
import random


uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "123456789"
symbols = ".?+*@#$"


class client:
    def __init__(self):
        self.name = ''
        self.surname = ''
        self.id = ''
        self.password = ''
        self.pass_hash = ''
        self.balance = 0

global user
user = client()

# Gets name from user
def set_user_name():
    
    while True:
        true_id = input("Please enter your name: ")
        
        for char in true_id.lower():
            if char.isalpha():
                user.name += char
            else:
                print('''Invalid input. Please enter a name
without numbers or special characters.''')
                user.name = ''
                break
        else:
            if user.name:  # Proceed if user_name is not empty
                break

                

    while True:
        true_id = input("Please enter your surname: ")
        user.surname = ''
        for char in true_id.lower():
            if char.isalpha():
                user.surname += char
            else:
                print('''Invalid input. Please enter a name
without numbers or special characters.''')
                user.surname = ''
                break
        else:
            if user.surname:  # Proceed if user_name is not empty
                break
    
    print((f'{user.name} {user.surname}').title())
    return user.name, user.surname

def set_user_id():
    
    user.id = f'{user.name[0:3]}{user.surname[0:3]}{random.randint(0,999)}'
    print(f'Your user ID is: {user.id}')
    return user.id

# If folder exists, get balance



def get_or_set_user_info(id):
    
    
    # Sees if user folder exists
    info_file_path = f"./Users/{id}/bank_info.txt"

    # if folder exists, get (user_id , user_password), export balance
    if os.path.exists(info_file_path):
        with open(info_file_path, "r") as file:
            lines = [line.strip() for line in file.readlines()]
            if len(lines) >=5 :
                while True:
                        user_ans = input("Please enter password : ")
                        user.password = hashlib.sha256(user_ans.encode()).hexdigest()
                        user.pass_hash = lines[3]
                        print(f'User input: {user_ans}, encoded: {user.password}, read from file: {user.pass_hash}')
                        # does user input password equal text password( line 2 of text)
                        if user.pass_hash == user.password :
                            user.name = lines[1]
                            user.name = lines[2]
                            user.balance = float(lines [4])
                            break
                        else:
                            print("Incorrect Password. Please enter correct passsword.")
            else:
                print('User data incomplete')
    # If folder doesn't, create it, set (user_id , user_password, opening balance) 
    else:
        while True:
            try:
                pass_loop()
                user.balance = float(input("Please enter your opening balance: "))
                if user.balance >= 0:
                    os.makedirs(f'./Users/{id}', exist_ok=True)
                    # Open Balance
                    with open(f"./Users/{id}/transaction_data.txt", "w") as file:
                        now = datetime.now()
                        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")  # dd/mm/YY H:M:S format
                        file.write(f'''{dt_string}
Transaction type: Opening Balance
Transaction amount: R{round(user.balance,2)}
''')
                    # Write user info
                   
                    os.makedirs(f'./Users/{id}', exist_ok=True)
                    with open(info_file_path, "w") as file:
                        file.write(f'''{id}
{user.name}
{user.surname}
{user.pass_hash}
{round(user.balance,2)}
{user.password}
''')
                    break
                else:
                    print("Invalid input. Please enter a number above zero.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    
    return user

def write_transaction_to_file(id, balance, amount, change):
    os.makedirs('./Users', exist_ok=True)
    with open(f"./Users/{id}/bank_info.txt", "w") as file:
        file.write(f'''{id}
{user.pass_hash}
{round(balance,2)}
''')
    with open(f"./Users/{id}/transaction_data.txt", "a") as file:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")  # dd/mm/YY H:M:S format
        file.write(f'''\n{dt_string}
Transaction type: {change}
Transaction amount: R{round(amount,2)}
Balance after transaction: R{round(balance,2)}
''')

def setup_password():
    # Prompt user to set a password and save it securely
    while not user.pass_hash:
        user.password = input("Please set a password: ")
        if user.password:
            # Generate hash of the password
            user.pass_hash = passGen()
        else:
            print("Password cannot be empty.")
    print("Password set successfully.")

# Clinton code
    
def pass_loop():
    while True:
        user_ans = input('''How would you like your password to be set?
1) Your own password
2) Generated password
>>>>''').lower()
        if user_ans in ['1', 'own']:
            setup_password()
            break
        elif user_ans in ['2', 'gen']:
            passGen()
            break
        else:
            print('Please Choose one of the options above')

def generate_password_hash():
    # Generate a hashed password using a secure hashing algorithm (e.g., bcrypt)
    return hashlib.sha256(user.password.encode()).hexdigest()

def passGen():
    all = ""
    all += uppercase_letters
    all += lowercase_letters
    all += digits
    all += symbols
    length = 16
    user.password = "".join(random.sample(all, length))
    print(f'''Your password is {user.password}''')
    
def setup_password():
    # Prompt user to set a password and save it securely
    user.pass_hash = None
    while not user.pass_hash:
        user.password = input("Please set a password: ")
        if  user.password:
            # Generate hash of the password
            user.pass_hash = generate_password_hash()
        else:
            print("Password cannot be empty.")
    print("Password set successfully.")
    return user.pass_hash, user.password


if __name__ == "__main__":
    set_user_name()
    set_user_id()
    get_or_set_user_info(user.id)

