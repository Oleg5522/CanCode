#simbol = input('Enter something')
#if simbol.isdigit():
#print(f' {simbol} is a number')
#elif simbol.isalpha(): 
#print(f'{simbol}  is word')
#else:
#print(f"{simbol}This is something else")

#user_input = input("Enter number ")
#if user_input % 2 != 0:
 #   print('Odd')
#else:
#    print('Even')

#if not user_input.isdecimal():
 #   print(f'{user_input} is not odd or even')
#elif int(user_input) % 2 != 0:
#    print(f'{user_input} is Odd')
#else:
#    print(f'{user_input} is Even')

#try:
 #   user_input = int(input('Enter your number: '))
#except:
#    print('Unknown')
#else:
 #   if user_input % 2 != 0:
  #     print('Odd')
   # else:
#print('Even')

user_input = input('Enter data')
if user_input.isdigit():
    print(f'{user_input} is a number')
elif user_input.isalpha():
    print(f'{user_input} is a word')
else:
    print(f'{user_input} is something else')