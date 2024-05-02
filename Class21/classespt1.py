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
    
point1 = Point2D(4,10)
point2 = Point2D(7,3)
print(point1)
print(point2)
print(point1+point2)
print(point1-point2)
        

# Return a string representation of this object
   
   
    
# Adds this object to another object from the same class, return a new object.
    
    
# Subtracts another object from this object, return a new object.
    

# Test equality between this object and another, return a boolean.
   
     
    
# Mutator method
  

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





''' Exercise - Date Class '''




 




'''
Exercise - Dog Class
'''






