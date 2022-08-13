# ATM SYSTEM - (Automated Teller Machine)

This's a computer-based program, and it makes managing bank account funds very simple and conceivable. Through this, users would be able to check their account balances and make cash withdrawals or deposits.

This ATM program can run in console mode. It has a number of features, including Account Statement, Withdrawal, Depositing Amount. 
The link to the deployed program can be found here. : ![ATM Program]()


![header image](/readmefile/header.PNG)

## How To Use 

The user must first provide an existing username, and if the username matches, the system will proceed to the next step, which is to ask for a pin number. When a user completes all of these sign-in procedures, they will be able to utilize all of the capabilities. It’s far too simple to utilize; they can verify their own account statements. When the user enters the system, if they want to check their account balance, they must enter "1" If they want to withdraw money, they must enter "2" Following that, they can insert the amount they wish to withdraw. If the user wants to deposit money, they must end with "3" and, following that, they can type the amount they intend to add to their account. Finally, they can exit from the system by clicking "4".

## Existing Feature


# Testing

I have tested this project by doing the following :
- Passed the code through a PEP8 linter and confirmed there are no problems.
- I performed the tests by entering wrong inputs to check  the OK and the not OK paths.
- Tested in my Gitpod local terminal.

![Check Result](/readmefile/check2.PNG))

# Bugs

## Solved Bugs

1. When I tested the program, I realized that in the message requesting the responses from the user, I had set a character for each responses, which is not correct in terms of the user experience, because the ATM system uses responses to request the responses from the user. So, I have determined the numbers for the user's responses.

![User Responses](/readmefile/debug.PNG)

![Solved bug](/readmefile/solved.PNG)

2. When I ran the program, I noticed that the option for exiting the system was incomplete, so that the system closed without any message to the user. To solve this, I created a goodbye message using the pyfiglet library before exiting the program.

![Exiting System](/readmefile/bug_exit.PNG)

![Solved bug](/readmefile/solvedd.PNG)

# Language & Programs

- **Github** - to store my repository.
- **Gitpod** - to create my project files.
- **python** - to write ATM program.
- **Heroku** - to deploy the program.


# Python Libraries & Modules

I used these python libraries :

- **Pyfiglet** - to create a header.
- **OS** - to clear the system after user login.
- **Time** - To add the sleep() function to the delay the terminal for simulating Insert card.
- **String** - to capitalize the usernames.



# Deployment

The project was deployed using Code Institute's mock terminal for Heroku.

Steps for deployment:
- Fork or clone this repository.
- Create a new Heroku app.
- Set the buildbacks to python and NodeJS in that order.
- Link the Heroku app to the respository.
- Click on Deploy.

## Credits

- [Source Code Hero](https://sourcecodehero.com/atm-program-in-python-with-source-code/) - The code for multi-user login was taken from this site. When I decided to build an ATM program , at first my program had one user login, then I thought it would be better if it had a multi-user login. So, I searched on Google and found this site.
- [Learn Scratch Tutorials](https://www.youtube.com/watch?v=U1aUteSg2a4&list=WL&index=2&t=415s) - This YouTube video helps to learn how to use the **Pyfiglet** library for converting text to big ASCII text using Pyfiglet.
- [Programiz](https://www.programiz.com/python-programming/exception-handling) - Helped me to apply Exception Handling using a try-except statement.
- [Love Sandwiches](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode) - This project was a great starting point for me.








