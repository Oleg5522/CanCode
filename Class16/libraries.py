import math 
import statistics 
#import pandas 
from datetime import date
import datetime as dt
import requests


'''
Example
Import the math library.
Take the radius of a circle as user input.
Then, compute the area of the circle using the math library.
'''

try:
    
    radius = int(input('Enter radius '))
    area = math.pi*radius**2
    print(area)
except ValueError:
    print('Invalid data')

# BONUS

# lets do a try except just in case the user enters letters


'''
Exercise
Lets make some magic happen with the statistics library.
'''


# With Statistics Library

''' Nice little mean calculator to help with our testing

https://www.calculatorsoup.com/calculators/statistics/mean-median-mode.php
'''

# middle value in odd numbered list
odd_list = [1, 2, 3, 4, 5, 2, 9, 1, 3, 4, 6, 7]
median = statistics.median(odd_list)
print(median)


# # average of two middle values
even_list = [1, 2, 3, 4, 5, 2, 9, 1, 3, 4, 6, 7]
mean = statistics.mean(even_list)
print(mean)


'''
Exercise
Lets make some magic happen with the pandas library.
'''
# # dictionary with my users
canines = {
  "dog_name": ['saige', 'benji', 'stella', 'zuzu'],
  "dog_breed": ['dachsund', 'mastiff', 'golden retriever', 'hound'],
}

#df = pandas.DataFrame(canines)
#print(df)
# load into a dataframe


# I can even loop through it!

# Or assign a variable to a column and loop through that

# generate a csv
#df.to_csv('Output CSV', index = False)

'''
Exercise
Lets make some magic happen with the date time library.
'''

today = date.today()
print(today)
year = today.year
print(year)
last_week = today + dt.timedelta(days = -7)
print(last_week)

'''
https://jsonplaceholder.typicode.com/

This website provides free api testing. Lets leverage python's request module to see if we can do a get request against this data
'''
my_response = requests.get('https://jsonplaceholder.typicode.com/users')
print(my_response.text)

