import re

'''
You are testing a string to a while loop. The string must pass the following tests or the user must start over, be sure to tell the user the error.

1. String must be at least 10 characters
2. String must contain at least 1 number
3. String must contain at least 1 capital letter
4. String must contain '@' symbol
5. String must contain no spaces

Test data
jdefwkwf - not enough characters
sdnesleuex - at least 10 characters but no number
sdksdjsdf0 - at least 10 characters, contains number, no caps
Sdksdjsdf0 - at least 10 characters, contains number, has caps, no @ symbol
Sd@sdjs df0 - at least 10 characters, contains number, has caps, @ symbol, contains a space
Sd@sdjsdf0 - should pass all tests
'''
 # Not enough characters

user_input, re_prompt_user = '',''  #initialization

while True:

    user_input = input("Please enter your string ")
    print(user_input)
    if len(user_input)>=10:
        print(f"Test passed, {user_input} is greater than 10")
        break
    else:
        print(f"Test failed, {user_input} is less 10")
        continue
    
   

    
           # Contain at least 1 number
    contains_num = re.search(r'\d', user_input) # will look for a digit in a string 
#if contains_num:
#    print(f' Test passed: {user_input} contains number')
#    else:
#    print(f'Test failed, {user_input} does not contain number')
#    continue
    

  
    # Contains at least 1 capital letter
any_upper = any(u.isupper for u in user_input)
if any_upper:
    print(f'Test passed, {user_input} contains capital letter')
else:
    print(f'Test failed, {user_input} does not contain a capital letter')
    continue


    # Contains '@' symbol
if '@' in user_input:
    print('Test passed {user_input} contains '@'')
else:
    print('Test FAILEd {user_input} Does not contain '@'')
    continue


    
    # Contains no spaces
has_space = re.search(r'\s', user_input)

if not has_space:
    print(f'Test passed, {user_input} has no spaces')
    print('Congrats, all testing passes')
    break
else:
    print(f"Test failed, {user_input} contains a spase")
    continue

re_promt_user = ('Congrats on signing up, please log in')

if user_input==re_prompt_user:
    print('Congrats on logging in')
break
print('No dice! Start over!')
continue    
        



    
    
       
  

    
    