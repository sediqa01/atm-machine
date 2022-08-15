# ATM SYSTEM - (Automated Teller Machine)


This's a computer-based program, and it makes managing bank account funds very simple and conceivable. Through this program, users would be able to check their account balances, make cash withdrawals, and make deposits. This ATM program can run in console mode. It has a number of features, including Account Statement, Withdrawal, and Depositing Amount. The link to the deployed program can be found here: [ATM Program](https://atm-system.herokuapp.com/)


![image](/readmefile/run_program.PNG)


**Note:**  Due to the nature of the programme, it is not suitable for mobile phones and smaller devices.

![image](/readmefile/responsive.PNG)


## How To Use 

The user must first provide an existing username, and if the username matches, the system will proceed to the next step, which asks for a pin number. When a user completes all of these sign-in procedures, they will be able to utilize all of the capabilities. It’s far too simple to utilize; they can verify their own account statements. When the user enters the system, if they want to check their account balance, they must enter "1". If they want to withdraw money, they must enter "2." Following that, they can insert the amount they wish to withdraw. If the user wants to deposit money, they must end with "3" and, following that, they can type the amount they intend to add to their account. Finally, they can exit from the system by clicking "4".



## Features

### Existing Feature


1. **Welcome Message**

![messge](/readmefile/header.PNG)

______

2. **User Login** 
 Users can conduct transactions by verifying their own account statements; all user inputs are validated, and errors allow for multiple attempts to enter a valid username and password.


**User 1**

![login](/readmefile/sediqalogin.PNG)


**User 2**

![login](/readmefile/hadid.PNG)


**Successful Login**

![login](/readmefile/successful_login.PNG)



**Invalid UserName & Password**

![login](/readmefile/invalid_username.PNG)
![login](/readmefile/invalid_password.PNG)



**Failed Login**

![login](/readmefile/failedlogin.PNG)

______

3. **Transaction Menu** 
 This feature allows users to choose from the menu which transaction they would like to carry out. Users must be able to check their A/C balance and withdraw or deposit money into a certain account.

![login](/readmefile/successful_login.PNG)



**Invalid User Input** 

![login](/readmefile/wrong_response.PNG)
![login](/readmefile/wrong_response2.PNG)


______

4. **Check A/C balance**

 This feature allows users to check the amount of balance they have on their account so they can make a valid transaction.

![balance](/readmefile/balance.PNG)

____________

5. **Withdraw**
 This feature allows users to withdraw the amount they wish. Here also, all user inputs are validated, and errors allow repeat opportunities to input a valid amount. For withdrawal, the user must enter an integer amount. This program does not accept float numbers for cash withdrawal. Furthermore, users cannot withdraw more than their balance.


**Case1: Successful withdrawal**

![withdraw](/readmefile/withdraw.PNG)



**Case2: Float numbers inputs**

![withdraw](/readmefile/float_withdraw.PNG)



**Case3: Invalid User Input**

![withdraw](/readmefile/grater_withdraw.PNG)

___________________

6. **Deposit**
 This feature allows users to deposit the amount they wish. Here also, all user inputs are validated, and errors allow repeat opportunities to input a valid amount. Users can make deposits of more than ten dollars. This program does not accept float numbers for cash deposit.


**Case1: Successful Deposit**

![Deposit](/readmefile/deposit.PNG)


**Case2: Float numbers inputs**

![Deposit](/readmefile/float_deposit.PNG)


**Case3: Invalid User Input**

![Deposit](/readmefile/small_deposit.PNG)

_______________________


4. **System Exit**
 If a user finishes a transaction, he/she can exit the system by clicking 4.

![exit](/readmefile/exit.PNG)



## Testing

I have tested this project by doing the following :
- Passed the code through a PEP8 linter and confirmed there is no problems.
- I performed the tests by entering wrong inputs to check  the OK and the not OK paths.
- Tested in my Gitpod local terminal.

![Check Result](/readmefile/check2.PNG)


## Bugs

### Solved Bugs

1. When I tested the program, I realized that in the message requesting the response from the user, I had set a character for each responses, which is not correct in terms of the user experience, because the ATM system uses responses to request the responses from the user. So, I have determined the numbers for the user's responses.

![User Responses](/readmefile/debug.PNG)

![Solved bug](/readmefile/solved.PNG)


2. When I ran the program, I noticed that the option for exiting the system was incomplete, so that the system closed without any message to the user. To solve this, I created a goodbye message using the pyfiglet library before exiting the program.

![Exiting System](/readmefile/bug_exit.PNG)

![Solved bug](/readmefile/solvedd.PNG)

### Remaining Bugs
    
- No bugs remaining

## Language & Programs

- **Github** - To store my repository.
- **Gitpod** - To create my project files.
- **python** - To write ATM program.
- **Heroku** - To deploy the program.
- **Snipping Tool** - A screenshot tool is built into Windows. I used it to take screenshots of different parts of the ATM program.


## Python Libraries & Modules

I used these python libraries :

- **Pyfiglet** - To create a header & Goodbye Message.
- **OS** - to clear the system after user login.
- **String** - To capitalize the usernames.
- **Time** - To add the sleep() function to make a delay in the terminal for simulating the insert card.

**Note:** I have installed the termcolor library and imported it into my program to color the code in the terminal , but when I applied I noticed that there was no sign that text has color , so I changed my mind and deleted the import library.


## Deployment

The project was deployed using Code Institute's mock terminal for Heroku.

Steps for deployment:
- Fork or clone this repository.
- Create a new Heroku app.
- Set the buildbacks to python and NodeJS in that order.
- Link the Heroku app to the respository.
- Click on Deploy.

### Credits

- [Source Code Hero](https://sourcecodehero.com/atm-program-in-python-with-source-code/) - The code for multi-user login was taken from this site. When I decided to build an ATM program , at first my program had one user login, then I thought it would be better if it had a multi-user login. So, I searched on Google and found this site.
- [Learn Scratch Tutorials](https://www.youtube.com/watch?v=U1aUteSg2a4&list=WL&index=2&t=415s) - This YouTube video helps to learn how to use the **Pyfiglet** library for converting text to big ASCII text using Pyfiglet.
- [Programiz](https://www.programiz.com/python-programming/exception-handling) - Helped me to apply Exception Handling using a try-except statement.
- [Love Sandwiches](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode) - This project was a great starting point for me.








