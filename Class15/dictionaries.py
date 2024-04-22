from statistics import mode
#pip install pandas
import pandas
import numpy as np

''' Fun facts about dictionaries 

    -collection of keys and values
    -used to store associated information
    -keys are the words, values are the definitions

'''

# How do we create a dictionary?

user_data = {'user id':400, 'name':'Fritz'}
print(user_data)
print(user_data['name'])
print(type(user_data))


# Access keys with brackets


# # Add new key value
user_data['state'] = 'NY'
print(user_data)
user_data['state'] = 'NJ'
print(user_data['state'])


# lets look at all the methods available to us
print(dir(user_data))
print(user_data.__contains__('user_id'))



# lets try one


# Dict constructor
new_dictionary = dict()
print(type(new_dictionary))
pet_name = dict(name = 'Fido', age = 14)
print(pet_name)
print(type(pet_name))





# Dictionary methods


dog = {
    "breed": "japanese chin",
    "gender": "female",
    "age": 7
}

# Lets use the keys methods to get the keys from this dictionary
# Assign keys to a variable
dog_information = dog.keys()
print(dog_information)
print(dog)



# Assign values to a variable
#dog.clear()
#print(dog)



# Lets use clear method to remove all elements



# Lets use get method to get a key value

age = dog.get('age')
print(age)
print(dog.get('temperament', "not exist"))



# # # lets look at one of the parameters to show an error if the key doesnt exist

# Lets create a copy

dog_copy = dog.copy()
print(dog_copy)


# Lets remove a specified key with pop

#dog_copy.pop('breed')
#print(dog_copy)




# Lets remove a last inserted key-value pair with popitem
#dog_copy.popitem()
#print(dog_copy)


# Get a list with each key-value pair with items

key_value_pairs = dog_copy.items()
print(key_value_pairs)




# we can loop through

for k, v in dog_copy.items():
    print(k, v)


# Update allows us to update by changing and adding data
dog.update({'temperament':'happy', 'breed':'chihuahua'})
print(dog)


# Dictionaries vs Lists
list1 = ['a', 'b', 'c', 'd', 'e']
dict1 = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 5: 'e'}

print(list1[3])
print(dict1[3])
 

'''
Write some code that takes two lists and converts them into one dictionary.
In:
list1 = ['one', 'two', 'three']
list2 = [4, 10, 30]
Out:
{'one': 4, 'two': 10, 'three': 30}

'''
list1 = ['one', 'two', 'three']
list2 = [4, 10, 30]

new_dict = {}
for n in range(len(list1)):
    new_dict.update({list1[n]:list2[n]})
print(new_dict)

#diction = dict(list1{n}+list2{m})
#print(diction)
#for x in list1:
#print(f x in '{list1: list2}')
#for n in list1:




my_keys = ['one', 'two', 'three']
my_values = [4, 10, 30]

# Using Zip & Dict
my_diction = dict(zip(my_keys, my_values))
print(my_diction)



# Using dictionary comprehension
#my_dictiona = {keys: values for (keys, my_values) in zip (my_keys, my_values)}
#print(my_dictiona)



'''
Exercise

Write a dictionary that contains five words and their definitions. Then have your code print the word and their definition one at a time.
Hint: Use the items() method

'''

words = {"color":"blue", "veggie":"radish", "vehicle": "bike", "mood": "happy", "pet":"cat"}

print(words.items())

for w, c in words.items():
    print(w, c)




# As datasets, we can use bracket notation

choices = {"flavors":['strawberry', 'vanilla', 'orange'],
           "sizes":['large', 'medium', 'small']}

print(choices['flavors'][0])


'''
Exercise
Create a dictionary for an automobile including make, model, year, number of doors, and number of cylinders.
'''

# car = {"make":"honda", 
#        "model":"accord", 
    #    "year":2011 , 
   #     "number of doors":4,
  #      "cylinders": 6}

 #print(car)

'''
In statistics, the mode is the value that appears most frequently in a dataset.
For example, in this list: [1,2,4,1,3,4,1,1] the mode is 1
Write some code that uses a dictionary to calculate the mode of a list.

'''

my_list_items = [1,2,4,1,3,4,1,1,7,7,7,7,7] # our list
output =  {}
for m in my_list_items:
    if m not in output:
        output[m] = 1
        
    else:
        output[m] +=1
print(output)

for l in my_list_items:
    output[l] = my_list_items.count(l)
print(output)    


# Statistics module

use_stats_module = [1,2,4,1,3,4,1,1,7,7,7,7,7]
result = mode(use_stats_module)
print(result)



# Looping through and adding 
incomes = {"apple": 5600.00, "orange": 3500.00, "banana": 5000.00}
total_income = 0.00
#for q, t in incomes.items():
#    print(q, t)
for i in incomes.values():
    total_income +=i
print(total_income)

print(sum(incomes.values()))




'''
Suppose you have a list of employee records that contain the following information for each employee: name, job title, salary. The records are stored as a list of dictionaries.
Use this list to create a dictionary where the keys are the job titles and the values are the average salaries for each job title.
Example:
records = [{'name': 'Bob', 'title': 'manager', 'salary': 50000},\
           {'name': 'Alice', 'title': 'developer', 'salary': 60000},\
           {'name': 'David', 'title': 'developer', 'salary': 65000}]
Output: {'manager': 50000, 'developer': 62500}
'''

records = [{'name': 'Bob', 'title': 'manager', 'salary': 50000},\
           {'name': 'Alice', 'title': 'developer', 'salary': 60000},\
           {'name': 'David', 'title': 'developer', 'salary': 65000},
           {'name': 'Alice', 'title': 'consultant', 'salary': 25000},\
           {'name': 'David', 'title': 'consultant', 'salary': 40000},
           {'name': 'Isaiah', 'title': 'accountant', 'salary': 120000},
           {'name': 'Brenetta', 'title': 'seller', 'salary': 150000}]

title_salary_dict = {} # capture our titles and salary totals
title_count_dict = {} #capture title count

#loop through our list of dictionaries
for r in records:
    #define key and value pair for output 
    title = r['title']
    salary = r['salary']
#if the job title does not currently exist, we will add the title and the salary
    if title not in title_salary_dict:
        title_salary_dict[title] = salary
        title_count_dict[title] = 1
        #print(title_salary_dict)
        #print(title_count_dict)
    else:
        #otherwise, we will update the salary , and update the count of titles
        title_salary_dict[title] += salary
        title_count_dict[title] += 1

#Lets take a look at our output
print('All titles and sum of salaries', title_salary_dict)
print('Title , and the count of employees', title_count_dict)

result = {s:float(title_salary_dict[s])/title_count_dict[s] for s in title_salary_dict}
print(result)

#Pandas solution 
df = pandas.DataFrame.from_records(records) 
result = df.groupby('title')['salary'].mean()
print(result)










 



