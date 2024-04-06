''' Ranges 
Fun Facts about Ranges

A range is a group of numbers. (They must be ints, whole numbers.)
A range is an iterator like a string or list.
A range is different from a list of numbers, in that it does not store all the numbers it instead uses calculations to determine what the numbers should be.
We use them because they are really simple to write out, create, and don't force us to type out a list of numbers.
They also take up considerably less ram than a list containing the same information.

'''

''' Range(start, stop, step)'''

# Lets use the range function to count from 0 to 10


# for c in range(11):



# Let's use range to count from 10 to 50




# Let's use range to count from 0 to 20, and skip by 2




# Let's examine the output

# for i in range(16, 2, -3):
#     print(i, end=" ") # change default end parameter from newline to space

# for i in range(4):
#     print(i, i+1, sep=", ")

# To see output, we would need to add a negative step, -1
# for i in range(3, 2): 
#     print(i)



''' Exercise
Write a range that is every five years from 1960 to 2000.
Write a range that counts down from 30 to 0

'''




'''
Rewrite the for loop we made last class that goes through a list and prints each item in the list, along with its index. (Hint: you can use a range, and you won't need a separate counter variable.)

Example:
planets = ["mercury", "venus", "earth", "mars"]
0: mercury, 1: venus, 2: earth, 3: mars


Previous Solution with counter

counter = 0
planets = ["mercury", "venus", "earth", "mars"]


for p in planets:
    print(f'{counter}: {p}')
    counter += 1
'''
# Solution with range, no counter needed



''' Exercise
You have a list of employees, and a list of job titles. Assume the lists are the same length and in the same order.
Use one for loop to go through both lists and print the job title of each employee.
For example, if these are your lists:
employees = ['Bob', 'Cynthia', 'Abdul']
job_titles = ['accountant', 'engineer', 'recruiter']
This should be your output:
Bob's job title is accountant.
Cynthia's job title is engineer.
Abdul's job title is recruiter.

'''

employees = ['Bob', 'Cynthia', 'Abdul']
job_titles = ['accountant', 'engineer', 'recruiter']



''' 
Exercise

Write some code that creates a range based on what the user enters. 
Challenge: you can make a range with 1, 2, or 3 numbers. How would you allow the user to pick any of these options?

'''

