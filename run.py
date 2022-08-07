# imprt libraries
import time

print("\n\nPlease Insert Your Card!\n\n")
time.sleep(2)

print("**********************************************")
print("*                                            *")
print("*            Welcome to ATM SYSTEM           *")
print("*                                            *")
print("**********************************************")

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

# in case of a valid pin- continuing, or exiting
    if count == 3:
        print('\n3 Unsuccesful PIN Attempts, EXITING')
        print('Your Card has been LOCKED!!\n')
        exit()

print('Login Succesful, CONTINUE\n')
print(str.capitalize(users[n]), 'Welcome to ATM!')
