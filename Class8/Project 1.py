import re


''' What are some of the things we may come across while building this project'''

'''Initialization and prompt (and testing)'''


first_input, second_input = '', ''  #initialization
#F_I=input('')
sample_list = ['admin', 'admin123', 'superuser', 'superuser123']
print('Hello. Please create your Username and Password and be sure that Username must start with a lowercase letter and only contain letters, numbers and underscores ')


while True:
    first_input = input("Create your Username")
    second_input =  input("Create your Password")

    a = ' '
    b = 'q w e r t y u i o p a s d f g h j k l z x c v b n m Q W E R T Y U I O P A S D F G H J K L Z X C V B N M '
    c = '0 1 2 3 4 5 6 7 8 9'

    if not any(x in first_input for x in b)  and not any(x in first_input for x in c) and not any(x in first_input for x in a) and not first_input[0].islower() :
        print('Username doesn`t meet requirements')
    #    continue

    #if not first_input[0].islower()
    #print('Username must start wiyn lowercase')
    #break



#     #first_input.isnumeric() and first_input.isalpha()
#     is_digit_present = any(character.isdigit() for character in first_input) or
#     is_letter_present = any(character.isalpha() for character in first_input) or
#     is_underscore_present = any(character = '_' for character in first_input)
  #   and 
 #    first_input not in sample_list
    # and 
   #  len(second_input)=>8 
  #   and 

 #    for i in first_input:
         
       

#     print(first_input, second_input)
#     break
#else:
#continue





'''Handling error messages with a list (and testing)'''

error_messages = ['Your Username doesn`t meet the requirements, please, try again', 'Your Password doesn`t meet the requirements, please, try again', 'This is my new message']


# if 5 > 7:
#     print(error_messages[0])
# else:
#     print(error_messages[2])


'''Testing a string'''

# Example of string testing (testing for lowercase letter)

# test_string = 'Popeye1989'

# Testing for uppercase as first letter
# first_letter = test_string[0]
# lower_case_test = first_letter.islower()

# if lower_case_test:
#     print("This string failed lowercase testing")
# else:
#     print("This string passed lowercase testing")



''' Taken usernames '''
#sample_word = 'black'
#sample_list = ['admin', 'admin123', 'superuser', 'superuser123']

# if sample_word in sample_list:
#     print("USERNAME IS TAKEN, PLEASE, TRY AGAIN")
# else:
#     print("Word does not exist in list")


''' Using Break and Continue to control the flow of loop'''

# If input is a number we will go through this while loop and continue through, if not, we will send the user back to the beginning

# while True:
#     userinput = input("What is your test string? ")

#     if userinput.isnumeric():
#         print("This is a number, we will stay in the loop")
#     else:
#         print("Not a number, have the user try again")
#         continue

#     print("if you see this line of code, we are still in the loop")
#     break


''' Password requirements '''

test_string = 'c1234567'
# At least 8 characters long

# Contains at least one uppercase letter
#one_uppercase = False
#for t in test_string:
#    if t.isupper():
#        one_uppercase = True

# print('Contains at least one uppercase letter? ', one_uppercase)


# Even better, is the any function! Tests if any of items in iterable is true
# any_uppercase = any(u.isupper() for u in test_string)
# print('Contains at least one uppercase letter? ', any_uppercase)
        

# Or Regular Expressions match method

# uppercase_test_regex = bool(re.match(r'\w*[A-Z]\w*', test_string))
# print('Contains at least one uppercase letter? ', uppercase_test_regex)
        



''' Logging in and handling the loop'''

# These can represent the user id and password the user created
sys_username = 'simonsays123'
sys_password = 'fido1950'


# These can represent the re-authentication
username = 'simonsays'
password = 'fido1950'

# Lets check for a match

#while True:
#    if sys_username == username and sys_password == password:
#        print("Login Successful")
#        break
#    else:
#        print("Incorrect username and password")