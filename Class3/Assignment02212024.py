#This program calculates the perimeter of a triangle in two ways
# Simple way
print("Simple way")
Side1 = 5
Base = 6
Side2 = 10
print("The perimeter of a triangle is ", (Side1+Base+Side2))
print("Is Side1 greater than Side2?", Side1>Side2)
print("Is the base equal to Side1?", Base == Side1)
#Difficult way
print("Difficult way")
def sum(a, b, c):
    return (a + b + c)
a = float(input('Enter Side1: '))
b = float(input('Enter Base: '))
c = float(input('Enter Side2: '))
print(f'Perimeter is {sum(a, b, c)}')
print("Is Side1 greater than Side2?", Side1>Side2)
print("Is the base equal to Side1?", Base == Side1)