

'''
Exercise

You're working on a project to develop a login system for a website. The website requires the user to enter a username and password to log in. Write a Python program that checks whether the user entered the correct username and password.
Create two variables called username and password and set them to any valid string values.
Prompt the user to enter their username and password using the input() function.
Use conditionals and logical operators to check whether the username and password entered by the user match the username and password variables.
If they match, print “Login successful.” If they don't, print “Incorrect username or password.”
'''
''' Exercise solution '''

#Set values for Username and Password
Username = "Oleg"
Password = "CanCode"
#Enter Usename and Password by user
Username1 = input('Please, enter your Username')
Password1 = input('Please, enter your Password')
#Check if user entered right Username and Password
if Username1 == Username and Password1 == Password:
    print('Login successful')


else :
    print('Incorrect username or password.')





# Prompt the user to enter their username and password using the input() function.


# Create two variables called username and password and set them to any valid string values.


# Create your conditional