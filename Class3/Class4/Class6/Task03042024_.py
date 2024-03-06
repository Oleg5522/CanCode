#Username and Password from Data
Username = "Oleg"
Password = "CanCode"


#Operator cycle
while True: 
    Username1 = input('Please, enter your Username')
    Password1 = input('Please, enter your Password')
    
    
    if Username1 == Username and Password1 == Password:
       print("Login successful")
       break


    print('You enter incorrect Data, please, try again')
  
