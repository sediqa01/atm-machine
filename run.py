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

