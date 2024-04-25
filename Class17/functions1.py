import math
#import pandas
#import name_module

'''
Exercise
Write a function that will loop through a string and print whether a character is or is not a vowel.
'''
#def isvowel(string):
#     pass
#   string = input('Please enter character', )
#vowels = range('e','u','i','o','a')
#for v in vowels:
#     if v in string:
#     print('This is a vowel')
#     else:
#     print('This is not a vowel')

#name_module.isvowels('America')

def greet(name):
    #name = input("Hello")
    return (f"Hello ", name)
print(greet('Sarah'))

#print(greet("Oleg"))

def double_me(value):
    result = value * 2
    print(result)
num=10
double_me(num)



'''
Example

Write a function that returns the surface area of a box (rectangular prism).
Surface Area = width*2 + length*2 + height*2

'''
#def surface_area(w,l,h):
#     pass
#w = int.input('Enter width')
#l = int.input('Enter length')
#h = int.input('Enter height')
#result = (w*2+l*2+h*2)
#print(result)

#name_module.surface_area()

#def s_a(w,l,h):
#     return 2*(w*l)+(h*l)+(w*h)
#     s_a(5,4,3)
#     print(s_a)


'''
Exercise
Write a function that returns the surface area of a sphere.
Surface Area = 4 * pi * radius^2

'''

#def s_a_sph(r):
#     r = input('Enter radius')
#     return 4*math.pi*r**2
#print(s_a_sph(r))
#s_a_sph(10)


''' Lets follow these functions through line by line and analyse the return statements'''

# def get_vowels(word):
#     out = ''
#     vowels = 'aeiou'
#     for w in word:
#         if w in vowels:
#             out += w
    
#     return out

# my_word = 'bananas'

# get_vowels(my_word)
# print(get_vowels(my_word))

# Return is none
# def get_vowels(word):
#     out = ''
#     vowels = 'aeiou'
#     for w in word:
#         if w in vowels:
#             out += w
    
#     print(out)

# my_word = 'bananas'

# get_vowels(my_word)
# print(get_vowels(my_word)) # Return None



'''
Exercise
Write a function that takes a list and a value, and removes the value until it no longer exists in the list.
Return how many times the value was removed.
'''

sample_list = [4,5,3,2,4,3,3,3,3,2,2,1,1,1,1,0,5]
value = 5
#def 


'''
Suppose you work for a bank, and you have a list of transactions with the following information for each one: customer ID, transaction amount, and transaction type (deposit or withdrawal).
Write a function that takes in the list of customer transactions and returns a dictionary where the keys are the customer IDs and the values are the total transaction amounts for each customer.
Example:
transactions = [{'id': 'a', 'amount': 500, 'type': 'deposit'},\
                {'id': 'b', 'amount': 350, 'type': 'deposit'},\
                {'id': 'a', 'amount': 450, 'type': 'withdrawal'}]
     Output: {'a': 50, 'b': 350}

'''

transactions = [{'id': 'a', 'amount': 500, 'type': 'deposit'},\
                {'id': 'b', 'amount': 350, 'type': 'deposit'},\
                {'id': 'a', 'amount': 450, 'type': 'withdrawal'},\
                {'id': 'c', 'amount': 545, 'type': 'deposit'},\
                {'id': 'c', 'amount': 225, 'type': 'withdrawal'},\
                {'id': 'b', 'amount': 45, 'type': 'withdrawal'},\
                {'id': 'e', 'amount': 150, 'type': 'deposit'}]




''' Create a python file called name_module.py. Inside this python file, you will create 3 functions. One called full_name, another called reverse_name, and a third called get_initials. Each function will take 2 strings. One string will be the first name, the second string will be the last name. full_name will concatenate and return the full name. For example if the first string is "Joseph" and the second string is "Simpson" This function will return the string, "Joseph Simpson". Reverse name will flip the name around. The name Diana Prince, would come back as Prince Diana. The third function will take the first and last name and return the initials. The name Tony Stark will return T.S. Now create a second python file, called name.py. Import the module you just created and call the function with the necessary arguments so it prints a full names, reverse names, and initials as needed in the terminal'''

