from datetime import datetime
import datetime

'''
Classes
'''
# Class Definition and Initializer

class Point2D:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
      return f'({self.x},{self.y})'
    
    def __add__(self, other):
       return Point2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self,other):
       return Point2D(self.x - other.x, self.y - other.y)
    
    def __equal__(self,other):
       if self.x == other.x and self.y == other.y:
          return True 
       return False
    
    #def __lt__(self, other):
       if self.x < other.x and self.y < other.y:
          return True
       return False
    
    def set_x(self, other):
      self.x = other

    def set_y(self, other):
      self.y = other

    def get_x(self):
      return self.x
 

    
point1 = Point2D(4,10)
point2 = Point2D(7,3)
print(point1)
print(point2)
print(point1+point2)
print(point1-point2)
point3 = Point2D(1,2)
point4 = Point2D(1,2)
print(point3==point4)

point5 = Point2D(12,12)
point6 = Point2D(13,15)
#print(point5<point6)
        

# Return a string representation of this object
   
   
    
# Adds this object to another object from the same class, return a new object.
    
    
# Subtracts another object from this object, return a new object.
    

# Test equality between this object and another, return a boolean.
   
     
    
# Mutator method


point7 = Point2D(5,11)
point7.set_x(7)
print(point7)

point8 = Point2D(5,11)
point8.set_y(33)
print(point8)

point9 = Point2D(11,22)
#point9.get_x()
#print(point9)
print(point9.get_x())


# Accessor method
   

# Create a point object with attributes x=2, y=3

# Let’s add a __str__ method to our Point2D class so we can print Point2D objects.


# Lets add __add__ to add objects of the same class together


# Lets try __sub__ to add objects of the same class together

# Let's try __eq__ method to test equality
'''What is the output of this code if we don't override ==?
What is the output if we override == to use value equality?
Is it the same or different? Why?

Without the __eq__ method, we will only be able to test if it is the same object
'''



# Let's try __lt__ method to test less than


# Setting with mutator methods



# Getting with accessor methods





''' Exercise - Date Class 
1. Display the date in format mm/dd/yyyy
2. Compare 2 different days, if they are equal
3. Compare which date came first
4. Determine if a date is a leap year


'''

class Date:
   def __init__(self, year=1970, month=1, day = 1):
      self.year = year
      self.month = month
      self.day = day

   def __str__(self):
      return f'{self.month:02d}/{self.day:02d}/{self.year}'
      pass

   def __eq__(self, other: object) -> bool:
      if self.year == other.year and self.month == other.month and self.day == other.day:
         return True
      return False
      pass
   def __lt__(self,other):
      selfdate = datetime.datetime(self.year, self.month, self.day)
      otherdate = datetime.datetime(other.year, other.month, other.day)
      if selfdate < otherdate:
         return True
      return False
   
   def leap_year(self):
      if self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0):
         return True
      return False
   


my_date_info = Date(2004, 10, 3) #Create the object
second_date = Date(2004, 10, 4)
print(my_date_info==second_date)
print(type(my_date_info))
print(my_date_info)
print('Today\'s date is ', my_date_info)

old_date = (1999, 10, 23)
new_date = (2003,11, 12)
print('Date bool', old_date<new_date)

datenew = Date(2007, 6, 1)
print(datenew.leap_year())




 




'''
Exercise - Dog Class
'''

class Dog:
   def __init__(self, name, y_birth, breed):
      self.name = name
      self.y_birth = y_birth
      self.breed = breed

   def __str__(self):
      return f'{self.name} is a {self.breed} and was born in {self.y_birth}'
   
   def human_age(self):
       today = datetime.datetime.now()
       year = today.year
       #return f'{self.name} is {year - self.y_birth}'
       return year - self.y_birth 
   #print(human_age)

   #def dog_age(self):
       #today = datetime.datetime.now()
       #year = today.year
       #return f'{self.name} is {year - self.y_birth}'
       #return 7 * self.human_age() 
   #print(dog_age)


dog1 = Dog('Fido', '2020', 'Gold retriever')
dog2 = Dog('Zuzu', '2018', 'Dash')
dog3 = Dog('Stella','2016','Japanese')
#print(dog1.human_age())
print(dog2)
print(dog3)

#print(dog1.dog_age())









