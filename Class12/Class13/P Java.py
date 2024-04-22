'''
Exercise - Sets
See flowchart
You work at a company where some people know Python, some people know JavaScript, and some people know both.
In a loop, prompt the user to input an employee name, whether they know Python, and whether they know JavaScript. Use this to build two sets: a set of employees that know Python, and a set of employees that know JavaScript.
Use set operators to compute the following sets:
The set of employees that know both Python and JavaScript
The set of employees that know JavaScript, but not Python
The set of employees that know Python or JavaScript, but not both
'''
# instructions
print('''Python and JS Developer Tracker Instructions 
      Input 's' or 'stop' at anytime to exit program 
      To add a Python developer type 'p' when prompted
      To add a JavaScript developer type 'js' when prompted. ''' )
# initialize our variables

# Data collection sets
python_devs, js_devs = set(), set()

# User input
dev_type_input, dev_name_input = '', ''

#Error messages
error_msgs = ('Invalid input, please try again', 'Thank you, have a nice day')
# put our error messages in a tuple
# while loop
while True:
    dev_type_input = input("Type 'P' for python developer, 'JS' for Java developer, or 'STOP' to exit program: ").lower()
    if dev_type_input == 'stop':
        print(error_msgs[1])
        break 
# Get a dev type , add to our sets, and offer an exist
    if dev_type_input == 'p' or dev_type_input == 'js':
        dev_name_input = input('Enter developer name:  ').lower()

        if dev_name_input == 'stop':
            print(error_msgs[1])
            break
        elif dev_type_input == 'p':
            python_devs.add(dev_name_input.title())
        else:
            js_devs.add(dev_name_input.title())
    else:
        print(error_msgs[0])
        continue

    both_languages = python_devs.intersection(js_devs) #Everybody who knows both
    know_js_not_python = js_devs.difference(python_devs) # know js not python - difference 
    know_python_or_js_but_not_both = js_devs.symmetric_difference(python_devs) # who knows python or js but not both

    #if sets are empty , display no data for user
    if both_languages == set():
        both_languages = 'No data'
    if know_js_not_python == set():
        know_js_not_python = 'No data'
    if know_python_or_js_but_not_both == set():
        know_python_or_js_but_not_both = 'No data'

    print('Results')
    print('--------------------------------------------------------------------------------------')
    print(f'The following developers know both languages: {both_languages}')
    print(f'The following developers know_js_not_python: {know_js_not_python}')
    print(f'The following developers know_python_or_js_but_not_both: {know_python_or_js_but_not_both}')
    print('--------------------------------------------------------------------------------------')


    #print(both_languages, know_js_not_python, know_python_or_js_but_not_both)
    #break  


#while True:




# inputs
# string methods, title
# if statements, break keyword, continue, 

# print statement, formatted strings, to display result

# sets
