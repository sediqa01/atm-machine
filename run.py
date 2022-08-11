# imprt libraries
import time
import string
import os
import pyfiglet


print("\n\nPlease Insert Your Card!\n\n")
time.sleep(2)

# ATM (Automated Teller Machine)
header = pyfiglet.figlet_format(" Wlecome to ATM ")
print(header)


# Creating lists of users, their PINs and bank statements.
users = ['sediqa', 'hadid', 'sadat']
pins = ['0001', '0002', '0003']
amounts = [10000, 20000, 30000]
count = 0


# while loop checks existance of the enterd username
while True:
    user = input('\nPlease Enter Your  Username: ')
    user = user.lower()

    if user in users:
        if user == users[0]:
            n = 0
        elif user == users[1]:
            n = 1
        else:
            n = 2
        break
    else:
        print('\n\n     Invalid Username!!')

# comparing pin
while count <= 3:
    pin = input('Please Enter Your PIN: ')

    if pin.isdigit():
        if user == 'sediqa':
            if pin == pins[0]:
                break
            else:
                count += 1
                print('\n\n     Invalid PIN!!')
                print()

        if user == 'hadid':
            if pin == pins[1]:
                break
            else:
                count += 1
                print('\n\n     Invalid PIN!!')
                print()

        if user == 'sadat':
            if pin == pins[2]:
                break
            else:
                count += 1
                print('\n\n     Invalid PIN!!')
                print()         
    else:
        print('\n     PIN must Consists of 4 Digits.\n')
        count += 1

# in case of a valid pin continuing or exiting
    if count == 3:
        print('\n3 Unsuccesful PIN Attempts, EXITING')
        print('Your Card has been LOCKED!!\n')
        exit()

os.system('clear')

print(str.capitalize(users[n]), 'Welcome to ATM!')


# Main menu

def display_balance():  
    """
    Disply the user's A/C Balance
    """
    global amounts
    print()
    print(str.capitalize(users[n]), 'You have ',
                                    amounts[n], '$ on Your Account.\n')


def cash_withdraw(withdrawal_amount):
    """
    cash_withdraw
    """
    global amounts

    if withdrawal_amount > amounts[n]:
        print('\nThe Amount is not AVAILABLE!')
    else:
        amounts[n] = amounts[n] - withdrawal_amount
        print(f"{withdrawal_amount} Dollars successfully widthdrawn! ")
        print('Your Remaining Balance is', amounts[n], '$')


def cash_deposit(deposit_amount):
    """
    deposit_amount
    """
    global amounts

    if deposit_amount <= 10:
        print('The Amount You Want to Deposit must be more than 10$ ')
    else:
        amounts[n] = amounts[n] + deposit_amount
        print('Your new Balance is: ', amounts[n], '$')


def exit_system():
    """
    Exit System
    """
    exit()


response = None
amount = None

while True:

    try:
        response = input("""
            Select From Following Options: 
            1. Check A/C Balance (B)
            2. Cash Withdraw (W)
            3. Cash Deposit (D)
            4. Exit (E)
            \nType the Letter of Your Choices: """).lower()

        valid_responses = ['b', 'w', 'd', 'e']
        response = response.lower()

        if response == 'b':
            display_balance()

        elif response == 'w':
            amount = int(input("Enter Withdrawal Amount: "))
            cash_withdraw(amount)

        elif response == 'd':
            amount = int(input("Enter Deposit Amount: "))
            cash_deposit(amount)

        elif response == 'e':
            exit_system()
        
        else:
            raise ValueError('Response is not Valid!')

    except ValueError:
        print('Response is not Valid!')