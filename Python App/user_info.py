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

# Sign in or Sign up | checks if user name exists
    # set_user_name() || set_user_id() || get_or_set_user_info(user.id)
def sign_loop():
    while True:
        user_ans = input(f'''Please choose one of the
options below:
1) Sign in
2) Sign up

>>>''')
        if user_ans in ['1', 'Sign in', 'sign in', 'SIGN IN', 'Sign In']:
            get_user_info()
            break
        elif user_ans in ['2', 'Sign up', 'sign up', 'SIGN UP', 'Sign Up']:
            set_user_info()
            break
        else:
            print('Please choose one of the options provided')

# Sign up Function | creates new user
def set_user_info():
    
    # Get user's name
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
    
    # Get user's surname
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
    # User name + surname check
    print((f'{user.name} {user.surname}').title())
    
    # Create user.id
    user.id = f'{user.name[0:3]}{user.surname[0:3]}{random.randint(0,999)}'
    print(f'Your user ID is: {user.id}')

    # Set password
    pass_loop()

    # Set Basic info
    info_file_path = f"./Users/{user.id}/bank_info.txt"
    while True:
        try:
            user.balance = float(input('''==============<//>==============
Please enter your opening balance: '''))
            if user.balance >= 0:
                os.makedirs(f'./Users/{user.id}', exist_ok=True)
                # Open Balance
                with open(f"./Users/{user.id}/transaction_data.txt", "w") as file:
                    now = datetime.now()
                    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")  # dd/mm/YY H:M:S format
                    file.write(f'''{dt_string}
Transaction type: Opening Balance
Transaction amount: R{round(user.balance,2)}
''')
                # Write user info
                os.makedirs(f'./Users/{user.id}', exist_ok=True)
                with open(info_file_path, "w") as file:
                    file.write(f'''{user.id}
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

# Password Function | Lets user decide to enter or gen password  
def pass_loop():
    while True:
        user_ans = input('''How would you like your password to be set?
1) Your own password
2) Generated password
>>> ''').lower()
        if user_ans in ['1', 'own']:
            setup_password()
            break
        elif user_ans in ['2', 'gen']:
            passGen()
            break
        else:
            print('Please Choose one of the options above')

# Set up password
def setup_password():
    # Prompt user to set a password and save it securely
    user.pass_hash = None
    while not user.pass_hash:
        user.password = input("Please set a password: ")
        if  user.password:
            # Generate hash of the password
            generate_password_hash()
        else:
            print("Password cannot be empty.")
    print("Password set successfully.")
    return user.pass_hash, user.password

# Generates password
def passGen():
    all = ""
    all += uppercase_letters
    all += lowercase_letters
    all += digits
    all += symbols
    length = 16
    user.password = "".join(random.sample(all, length))
    print(f'''==============<//>==============
Your password is {user.password}''')
    generate_password_hash()

# Encripts password
def generate_password_hash():
    # Generate a hashed password using a secure hashing algorithm (e.g., bcrypt)
    user.pass_hash =  hashlib.sha256(user.password.encode()).hexdigest()
    return user.pass_hash

# Sign in Function | Checks if user password is true | When password is correct, get user info
def get_user_info():
    
    user.id = input('''==============<//>==============
Please enter your user id
>>> ''')
    info_file_path = f"./Users/{user.id}/bank_info.txt"
    # Sees if user folder exists
    if os.path.exists(info_file_path):
        # if folder exists, get (user_id , user_password), export balance
        with open(info_file_path, "r") as file:
            lines = [line.strip() for line in file.readlines()]
            if len(lines) >=5 :
                while True:
                        user_ans = input('''==============<//>==============
Please enter password
>>> ''')
                        user.password = hashlib.sha256(user_ans.encode()).hexdigest()
                        user.pass_hash = lines[3]
                        print(f'User input: {user_ans}, encoded: {user.password}, read from file: {user.pass_hash}')
                        # does user input password equal text password( line 2 of text)
                        if user.pass_hash == user.password :
                            user.name = lines[1]
                            user.surname = lines[2]
                            user.balance = float(lines [4])
                            return user
                        else:
                            print("Incorrect Password.")
            else:
                print('User data incomplete')
    # If folder doesn't, create it, set (user_id , user_password, opening balance) 
    else:
        print('''==============<//>==============
User does not exist.
Please sign up
''')
        set_user_info()
    
# Writes transactions to file
def write_transaction_to_file(amount, change):
    os.makedirs('./Users', exist_ok=True)
    with open(f"./Users/{user.id}/bank_info.txt", "w") as file:
        file.write(f'''{user.id}
{user.name}
{user.surname}
{user.pass_hash}
{round(user.balance,2)}
''')
    with open(f"./Users/{user.id}/transaction_data.txt", "a") as file:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")  # dd/mm/YY H:M:S format
        file.write(f'''\n{dt_string}
Transaction type: {change}
Transaction amount: R{round(amount,2)}
Balance after transaction: R{round(user.balance,2)}
''')
