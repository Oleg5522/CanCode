
#full_name which concatenate and return the full name
def fullname():
    first_name = input('Enter first name', )
    last_name = input('Enter last name', )  
    result = (first_name+' '+last_name)
    print(result)

#Reverse name which flip the name around
def reversename():
    first_name = input('Enter first name', )
    last_name = input('Enter last name', )
    result = (last_name + ' '+ first_name)
    print(result)


#function which take the first and last name and return the initials
def initials():
    first_name = input('Enter first name', )
    last_name = input('Enter last name', )
    result = (first_name[0].title()+"."+"  "+last_name[0].title()+".")
    print(result)

