# imprt libraries
import time
import string
import os
import pyfiglet


print("\n\nPlease Insert Your Card!\n\n\n")
time.sleep(2)

# ATM (Automated Teller Machine)
header = pyfiglet.figlet_format(" Welcome  to ATM ")
print(header)

# Creating user's information for login
"""
The code for multi-user login was taken from this site [Source Code Hero]
(https://sourcecodehero.com/atm-program-in-python-with-source-code/)
"""

usernames = ['user1', 'user2', 'user3', 'user4']
passwords = ['0001', '0002', '0003', '0004']
amounts = [10000, 20000, 30000, 4000]
count = 0


# Checks users' information for verifying account statements.

while True:
    user = input('\nPlease Enter Your  Username: ')
    user = user.lower()

    if user in usernames:
        if user == usernames[0]:
            n = 0
        elif user == usernames[1]:
            n = 1
        else:
            n = 2
        break
    else:
        print('\n\n     Invalid Username!!')

# While loops will confirm the passwords to verify the user's login
while count <= 3:
    pin = input('Please Enter Your PIN: ')

    if pin.isdigit():
        if user == 'user1':
            if pin == passwords[0]:
                break
            else:
                count += 1
                print('\n\n     Invalid PIN!!')
                print()

        if user == 'user2':
            if pin == passwords[1]:
                break
            else:
                count += 1
                print('\n\n     Invalid PIN!!')
                print()

        if user == 'user3':
            if pin == passwords[2]:
                break
            else:
                count += 1
                print('\n\n     Invalid PIN!!')
                print()
    else:
        print('\nPIN must Consists of 4 Digits.\n')
        count += 1

# If a user types an invalid password three times , the program will exit.
    if count == 3:
        print('\n 3 failed PIN attempts. EXITING ....')
        print()
        exit()

os.system('clear')

print(str.capitalize(usernames[n]), ', Welcome to ATM!!')


# Main menu

def display_balance():
    """
    This function will show the user's account balance.
    """
    global amounts
    print()
    print(str.capitalize(usernames[n]), 'You have ',
                                        amounts[n], '$ on Your Account.\n')


def cash_withdraw(withdrawal_amount):
    """
    This function will process the withdrawal cash amount
    and check if the withdrawal amount was greater than the entered amount,
    It will show a message that the entered amount is not valid.
    """
    global amounts

    if withdrawal_amount > amounts[n]:
        print('\nThe Amount is not AVAILABLE!')
    else:
        amounts[n] = amounts[n] - withdrawal_amount
        print()
        print()
        print(f"{withdrawal_amount} Dollars successfully widthdrawn! ")
        print('Your Remaining Balance is', amounts[n], '$')


def cash_deposit(deposit_amount):
    """
    This function will process the deposit cash amount and
    check if the deposit amount was less than 10$..
    It will show a message that the deposit amount must be greater than 10$
    """
    global amounts

    if deposit_amount <= 10:
        print('\n\n The Amount You Want to Deposit must be more than 10$ ')
    else:
        amounts[n] = amounts[n] + deposit_amount
        print('\n\nYour new Balance is: ', amounts[n], '$')


def exit_system():
    """
    This function will show a Goodbye message and exit the system.
    """
    goodbye_message = pyfiglet.figlet_format('Thank You, Bye!')
    print(goodbye_message)
    exit()


# The while loop will process the user's responses for transaction processing.
response = None
amount = None

while True:

    try:
        response = int(input("""
            Select From Following Options:
            1. Check A/C Balance
            2. Cash Withdraw
            3. Cash Deposit
            4. Exit
            \nType the Number of Your Choices: """))

        if response == 1:
            display_balance()

        elif response == 2:
            try:
                amount = int(input("Enter Withdrawal Amount: "))
            except ValueError:
                print("\n\nPlease Insert a valid Withdrawal Amount!\n\n")
            else:
                cash_withdraw(amount)

        elif response == 3:
            try:
                amount = int(input("Enter Deposit Amount: "))
            except ValueError:
                print("\n\nPlease Insert a valid Deposit Amount!\n\n")
            else:
                cash_deposit(amount)
        elif response == 4:
            exit_system()
        else:
            raise ValueError('\n\n     Response is not Valid!\n')

    except ValueError:
        print('\n\n     Response is not Valid!\n')
