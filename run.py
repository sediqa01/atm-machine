# imprt libraries
import time
import string
import os
import pyfiglet


print("\n\nPlease Insert Your Card!\n\n")
time.sleep(2)

header = pyfiglet.figlet_format("ATM SYSTEM",
                                justify="center")
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
while True:

    response = input("""
        Select From Following Options: 
        1. Statement__(S) 
        2. Withdraw__(W) 
        3. Lodgement__(L) 
        4. Quit__(Q)
        \nType the Letter of Your Choices: """).lower()

    valid_responses = ['s', 'w', 'l', 'p', 'q']
    response = response.lower()

    if response == 's':
        print()
        print(str.capitalize(users[n]), 'You have ',
              amounts[n], '$ on Your Account.\n')

    elif response == 'w':
        cash_out = int(input('Enter Amount you Would Like to Withdraw: '))

        if cash_out > amounts[n]:
            print('\nYou have entered INSUFFICIENT Balance')
        else:
            amounts[n] = amounts[n] - cash_out
            print()
            print(f"{cash_out} Dollars successfully widthdrawn! ")
            print('Your Remaining Balance is', amounts[n], '$')

    elif response == 'l':
        cash_in = int(input('\n\nEnter Amount you want to Lodge: '))
        print()

        if cash_in <= 10:
            print('Amount You Want to Lodge must be more 10$ ')
        else:
            amounts[n] = amounts[n] + cash_in
            print('Your new Balance is: ', amounts[n], '$')

    elif response == 'q':
        exit()

    else:

        print('Response not Valid')

