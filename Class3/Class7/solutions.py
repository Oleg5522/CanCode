#new_string = 'I am a double quote with a '@' single quote"

'''
You have a variable called hours which equals 24, the number of hours in a day.
Print There are 24 hours in a day. Make sure to use your variable.
First, print using commas. Remember that using commas automatically adds spaces!
Now, print using string concatenation. Remember to cast hours to a string and manually add the spaces!
'''



'''
Write some code that will print a box around a string.

Examples:
User input: hello
*******
*hello*
*******

User input: programming is fun
********************
*programming is fun*
********************
'''





'''
You need to write a script that will generate an email to a customer who has just made a purchase. You have 3 variables:
name, which stores the customer's name as a string
product, which stores the product name as a string
price, which stores the price of the product as a float
Use an f-string to generate an email message with the following text, and print it. Make sure to round the price to 2 decimal places. The email should be one multi-line string.
Dear {name},
Thank you for your purchase of a {product}. Your credit card has been charged ${price}.
We appreciate your business and look forward to serving you again.
Sincerely,
The ABC Company
'''

#name = 'Josiah Wilson'
#product = 'ABC Sneakers'
#price = 74.95343452342

# Remember to format the price



'''
Write some code that takes a string and tells if it is a palindrome (same forwards and backwards).
Hint: Use indexing/slicing and boolean expressions

Examples:
racecar: True
cat: False
'''

#userin == ' ', syspassword == ' '

#while userin != 'stop' :
    #userin = input('Please enter word or Stop to end the Loop')
    #print(userin)

    #username, password, day_of_week = " 1", " 2", "3 "
    #print(username)
    #print(password)
    #print(day_of_week)

#my_string = 'Hcrsaeriojplbjhfu'
#for s in my_string:
 #   print(s)


#my_list = ['dog', 'cat', 'bird', 'giraffe', 'fox', 'elephant', 'mouse', 'zebra']
#for animal in my_list:
#    print(animal)

    # DICTIONARY
#my_dictionary = {"First name": "Jill",
                 #"Last name": "Simmons",
                 #"Age": 34,
                 #"Address":"1515 Mockingbird Lane"}
#for keys
#for k in my_dictionary.keys():
 #   print(k)

    #for values
#for v in my_dictionary.values():
 #   print(v)

        #for both
#for k,v in my_dictionary.items():
 #   print(k,v)

#Range
#for x in range(10,12):
 #   print(x)

# STRING
#my_string = 'Supercalifragilisticexpialidocious'
#count = 0 #maintain the count in the letters of our string
#for s in my_string:
 #   print(s)
  #  count += 1 #incrimenting count for string
   # print(f'There are {count} letters in the word {my_string}')

#sum = 0
#user_input = input('Please enter your number: ')
#for t in user_input:
 #   if user_input.isdecimal():
  #      t = int(t)
   #     sum += t
#print(f'Your total is {sum}')

#word = 'hello'
#vowels = ['a', 'e', 'o', 'i', 'u']
#for w in word:

 #   if w in vowels:
  #      print(f'{w} is a vowel')
   # else:
    #    print(f"{w} is a consonant")

result = ''
user_input = input('Please enter your data')
for u in user_input:
    if u.isalpha():
        result += u 
    else:
        print(f'{u} is not letter')
print(result)
