#  Add two numbers

'''x = int(input("enter a number1: "))
y = int(input("enter a number2: "))
def add(a,b):
    result = a + b
    return result
print("sum is",add(x,y))'''


# Maximum of two numbers


'''a = int(input("enter a number1: "))
b = int(input("enter a number2: "))
def max(x,y):
    if x > y:
        return x
    else:
        return y    
print("max of all is", max(a,b))
'''


# Factorial of a number
# n = int(input("enter a number1: "))
# def factorial(n):
#     if  n < 0:
#         print("no factorial for negative numbers")
#     elif n == 0 and n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# y = factorial(5)
# print(y)


# Find simple interest

'''p = int(input("enter the principle amout (initial amt): "))
r = float(input("enter the rate of interest per anum: "))
t = int(input("enter the time in (years): "))
def simple_interest(a,b,c):
    return  float( a * b * c) / 100
print(f"the simple interest of the given amount {p} at {r} rate of interest is :",simple_interest(p,r,t))
'''

# Find compound interest
# Check Armstrong Number
# Find area of a circle
'''
r = float(input("enter the radius of a circle: "))
PI = 3.14
def area_circle(radius):
    return PI * radius * radius  
print("max of all is", area_circle(r))
'''
# Print all Prime numbers in an Interval

# Check whether a number is Prime or not
# p = int(input("enter the number: "))
# def is_prime(n):
#     if n % 2 == 0:

# N-th Fibonacci number
# Check if a given number is Fibonacci number?
# Nth multiple of a number in Fibonacci Series

# Print ASCII Value of a character


# Sum of squares of first n natural numbers
'''n = int(input("enter the number: "))
square = 0
i = 1
for x in range(1,n + 1):
    square = square + x * x
    i = i + 1
print("square of the given number is",square)'''



# Cube sum of first n natural numbers



"""def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

print("Reversed:", reverse_string("hello"))"""


#lambda function
'''y = lambda a,b : a + b
print(y(3,4))


g  = lambda h,i,j : (h * i) - j
print(g(10,3,4))'''


#OOPS
#class and object
'''
class Person:
    def __init__(self, name, age):  # Correct: __init__
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

a = Person("aneena", 20)
a.display_info()
'''

class rectangle:
    def__init__(self,length,width):
        self.width = width
        self.length = length

    def display_area(self):
        print(length * breadth)
    def display_perimeter(self):
         print(2 *(length * breadth))


a = rectangle(2,5)
a.display_area()
a.display_perimeter()


# encapsulation
'''class BankAccount:
    def __init__(self,name,balance):
        self.name = name      #public
        self._account_type = "saving"  #protected
        self.__balance = balance   #private


        def show_balance(Self):
            print(f"balance: {self.__balance}")


        def deposit(Self, amount):
            if amount > 0:
                self.balane += amount
acc = BankAccount("John",1000)                 
acc.show_balance()                 
acc.deposit(500)                 
acc.show_balance("John",1000) 
'''



#single inheritance
'''class Animal:
    def sound()
        print("Animal sound")

class dog(Animal)
    def bark(self)      
        print("dog barks")


d = dog()
d.sound()
d.bark()'''


#multilevel inheritance
'''class Father:
    def skills(self):
        print("gardening")
class Mother:
    def skills(self):
        print("programming")
class Child(Father,Mother):
    def skills(self):
        print("cooking")
        Mother.skills(self)
        Father.skills(self)
        print("Playing")

c = Child()
c.skills()
'''

# Hierarchical Inheritance
'''
class Vehicle:
    def category(self):  # corrected 'Self' to 'self'
        print("This is a vehicle")

class Car(Vehicle):
    def wheels(self):
        print("Car has 4 wheels")

class Bike(Vehicle):
    def wheels(self):
        print("Bike has 2 wheels")

# Creating objects
c = Car()
b = Bike()

# Accessing methods
c.category()
b.category()
c.wheels()
b.wheels()
'''

#multilevel inheritance
'''
class grandparents:
    def heritage(Self):
        print("Heritage  from grandparents")
        
class parent(grandparents):
    def culture(Self):
        print("heritage from  parents")
        
class child(grandparents):
    def hobby(Self):
        print("my hobby")
        
h = child()
h.hobby()
# h.culture()
h.heritage()

'''
#method overloading
# Having multiple methods with the same name but different parameters.
# Python does NOT support method overloading by default like Java or C++.
# But we can achieve similar behavior using default arguments or variable-length arguments.

# class MathOperations:
#     def multiply(self, a, b=1, c=1):  # Default arguments allow flexible calls
#         print(a * b * c)

# m = MathOperations()
# m.multiply(5)         # Only one argument, treated as 5 * 1 * 1
# # Output: 5

# m.multiply(5, 4)      # Two arguments, treated as 5 * 4 * 1
# # Output: 20

# m.multiply(5, 4, 3)   # Three arguments, treated as 5 * 4 * 3
# # Output: 60

