import re
u, p = '','' #initialization

taken_u = ['admin', 'admin123', 'superuser', 'superuser123'] #list of already used usernames

print('Hello, valuable client of our multinational corporation. In order to receive a monthly discount on our products, you need to register on our website. Please, sign up.') #Greetengs
while True:
    u = input('Please, create Username. The username must begin with a lowercase letter and can only contain letters, numbers, and underscores.', )
    print(u)
    if u[0].islower() and u.isidentifier(): #Checking that three requirements are met (first lowercase letter, no other characters except letters, numbers and underscores)
        print('Username meets requirements')
        break
        
    else:
        print('Username is incorrect, please, follow requirements')
        continue

while True:
      

 if u not in taken_u: #Checking whether the username entered by the user is missing from the database of existing usernames
    
        print('Username is correct, please, create your password')
        break
 else:
            
            print('Username is taken, please create different one')
            continue

while True:

        
    p = input('Please, create the password. The password must be:'
'At least 8 characters long',
'Contains at least one uppercase letter',
'Contains at least one lowercase letter',
'Contains at least one digit',
'Contains at least one of these characters: !, ?, @, #, $, ^, &, *, _, -',
'Does not contain any spaces', ) #User creation of a password
    print(p)
    if len(p)>=8: #Checking the minimum password length
        print(f"Password passed, {p} is greater than 8")
    else:
        print(f"Password failed, {p} is less 8")
        continue

# Checking at least 1 uppercase letter
    any_upper = any(x.isupper for x in p)
    if any_upper:
    print(f'Password passed, {p} contains uppercase letter')
else:
    print(f'Test failed, {p} does not contain an uppercase letter')
    continue

 # Checking at least 1 lowercase letter
    any_lower = any(y.islower for y in p)
    if any_lower:
    print(f'Password passed, {p} contains lowercase letter')
else:
    print(f'Test failed, {p} does not contain a lowercase letter')
    continue

# Checking at least 1 digit
digit_re = bool(re.match(r'\w*[0-9]\w*', p))
    if digit_re:
    print('Password passed, it contains digit')
else:
    print('Password failed, it does not contain a digit')
    continue

## Checking at least 1 special character
special_character = bool(re.match(r'\w*[!, ?, @, #, $, ^, &, *, _, -]\w*', p))
    if special_character:
    print('Password passed, it contains special character')
else:
    print('Password failed, it does not contain any special character')
    continue

# Checking for missing spaces
has_space = re.search(r'\s', p)
 if not has_space:
    print('Password passed, it does not contain any space')
    print('You signed up succesfully!')
    break
else:
    print('Password failed, it contains space')
    continue



# Sign-in process
while True:
    Username = input('Please, enter your Username', )
    Password = input('Please, enter your password', )
    if u == Username and p == Password:
        print("Login Successful")
        break
    else:
        print("Incorrect username and password")
        continue



















    
    


