# print("Hello World!")
# name = input("Enter your name: ")
# print("Name: " + name)

# Datatypes
# Here are some of the most common data types in Python:

# Numeric types: int, float, complex
# Boolean type: bool
# Sequence types: list, tuple, range
# Text type: str
# Mapping type: dict
# Set types: set, frozenset
# Binary types: bytes, bytearray, memoryview

# x = 5 # integer
# y = 2.5 # float
# print(x + y) # addition
# print(x - y) # subtraction
# print(x * y) # multiplication
# print(x / y) # division
# print(x % 2) # modulo operator


# string
# s1 = "Hello"
# s2 = "World"
# s3 = s1 + ", " + s2 + "!"
# print(s3)
# print(s3.upper()) # convert to uppercase
# print(s3.lower()) # convert to lowercase
# print(s3.replace("o", "*")) # replace 'o' with '*'

# lists
# list1 = [1, 2, 3, 4, 5]
# list2 = ["apple", "banana", "cherry"]
# list1.append(6) # add an element to the end of the list
# list2.insert(1, "orange") # add an element at index 1
# print(list1)
# print(list2)

# tuple
# tuples are a type of sequence in Python, similar to lists. However, tuples are immutable
# # Define a tuple with some values
# my_tuple = (1, 2, 3, 4, 5)

# # Access values in the tuple using indexing
# print(my_tuple[0])  # Output: 1
# print(my_tuple[3])  # Output: 4

# # Iterate over the values in the tuple using a for loop
# for value in my_tuple:
#     print(value)


# dictionaries
# # Define a dictionary with some key-value pairs
# person = {'name': 'John', 'age': 30, 'city': 'New York'}

# # Access values in the dictionary using the keys
# print(person['name'])  # Output: John
# print(person['age'])   # Output: 30
# print(person['city'])  # Output: New York

# # Add a new key-value pair to the dictionary
# person['occupation'] = 'Software Engineer'

# # Update the value of an existing key in the dictionary
# person['age'] = 35

# # Remove a key-value pair from the dictionary
# del person['city']


# Conditionals
# x = 5
# if x < 10:
#     print("x is less than 10")
# else:
#     print("x is greater than or equal to 10")

# fruits = ["apple", "banana", "cherry", "orange"]
# for fruit in fruits:
#     print(fruit)

# i = 0
# while i < 5:
#     print(i)
#     i += 1

# Functions
# def add_numbers(x, y):
#     """
#         Adds two numbers together and returns the result.
#     """
#     return x + y

# result = add_numbers(3, 5)
# print(result)
# help(add_numbers)  # uses docstring to display help

# Using a module
# import math
# result = math.sqrt(16)
# print(result)

# Classes
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def introduce(self):
#         print("Hi, my name is " + self.name + " and I am " + str(self.age) + " years old.")

# person1 = Person("John", 30)
# person1.introduce()

# Another
# class Person:
#   name = "Bhavyansh"
#   occupation = "Software Developer"
#   networth = 10
#   def info(self):
#     print(f"{self.name} is a {self.occupation}")

# self = the object for which the mehtod is called upon

# a = Person()
# b = Person()
# c = Person()

# a.name = "Shubham"
# a.occupation = "Accountant"

# b.name = "Nitika"
# b.occupation = "HR"

# # print(a.name, a.occupation)
# a.info()
# b.info()
# c.info()

# Decorators: modify a function
# def greet(fx):
#   def mfx(*args, **kwargs):
#     print("Good Morning")
#     fx(*args, **kwargs)
#     print("Thanks for using this function")
#   return mfx

# @greet
# def hello():    # hello function decorated with greet
#   print("Hello world")

# @greet
# def add(a, b):
#   print(a+b)
  
# # greet(hello)()    # this was to be done if @greet was not used above hello function
# hello()
# # greet(add)(1, 2)
# add(1, 2)

# Getters and Setters
# class MyClass:
#   def __init__(self, value):
#       self._value = value
    
#   def show(self):
#     print(f"Value is {self._value}")
    
#   @property
#   def ten_value(self):
#       return 10* self._value
    
#   @ten_value.setter
#   def ten_value(self, new_value):
#       self._value = new_value/10

# obj = MyClass(10)
# obj.ten_value = 67
# print(obj.ten_value)
# obj.show()


# File I/O
# with open("file.txt", "r") as file:
#     contents = file.read()
#     print(contents)

# Exception handling
# try:
#     x = 5 / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero")

# Libraries and frameworks
# Using the requests library to make HTTP requests

# import requests

# response = requests.get("https://api.github.com")
# print(response.status_code)

# Using flask to create a simple webapp
# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return "Hello, World!"

# if __name__ == "__main__":
#     app.run(debug=True)


# The __name__ and __main__
# if a module is being run as the main program (i.e., not being imported into another module), __name__ is set to the string "__main__". This can be useful for writing code that can be run either as a standalone program or as a module that is imported into another program.

# Here's an example that demonstrates how __name__ works:
# # Define a function that prints the value of __name__
# def print_name():
#     print(__name__)

# # If this module is being run as the main program, call print_name()
# if __name__ == '__main__':
#     print_name()

# In the example above, we define a function called print_name() that prints the value of __name__. We then check if __name__ is equal to "__main__", and if so, we call the print_name() function. When we run this script, the output will be "__main__", because we are running the script as the main program. If we were to import this module into another script, the print_name() function 'would not be called', because __name__ would be set to the name of the imported module instead of "__main__".

# walrus operator :=

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

# # Without the walrus operator
# while True:
#     user_input = input('Enter a value (q to quit): ')
#     if user_input == 'q':
#         break
#     print(f'You entered: {user_input}')

# # With the walrus operator
# while (user_input := input('Enter a value (q to quit): ')) != 'q':
#     print(f'You entered: {user_input}')

# With f-strings, you can include expressions inside curly braces {} within a string literal. These expressions are evaluated at runtime, and their values are inserted into the string.