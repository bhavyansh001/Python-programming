input_str = "Python"
reversed_str = ""

for char in input_str:
    reversed_str = char + reversed_str  

print(reversed_str)

# iter tools: for, comprehension; works on iteratable or iterable objects: lists, strings, file, __next__ (response of first iterable)
# Iteratable objects have memory location pointing at the start of the iteratable which is given to iter tools
# At the end StopIteration Exception is raised, which ends it
# this next can be given by user as well, a bit exception is present in files
# Check fileopen.py

# I = iter(myList)
# now I is pointing to the start of the list myList,
# I.__next__()      => prints first from list, same as next()
# I will still give the same location

# iter object is present by default in files (and files alone, not for any other datatype say list)
# iter(f) is f
# f.__iter__()

# iter(myList) is myList => false

# Dicionary is iteratable
# I = iter(D)

# R = range(5)
# I = iter(R)
# next(I)     # or __next__
# next(I)
# next(I)
# next(I)
# StopIteration

number = 3

for i in range(1, 11):
    if i == 5:
        continue
    print(number, 'x', i, '=', number * i)


while True:
    number = int(input("Enter value b/w 1 and 10: "))
    if 1 <= number <= 10:
        print("Thanks")
        break
    else:
        print("Invalid number, try again")


import math

def circle_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

a, c = circle_stats(3)

print("Area: ", a, "Circumference: ", c)



cube = lambda x: x ** 3

print(cube(3))


def sum_all(*args):
    print(args)
    for i in args:
        print(i * 2)
    return sum(args)

print(sum_all(1, 2, 3))


def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="shaktiman", power="lazer")
print_kwargs(name="shaktiman")
print_kwargs(name="shaktiman", power="lazer", enemy = "Dr. Jackaal")


x = 99
# global x
# x = 12 in a function will override global values, however, it is never to be done

def f1():
    x = 88
    def f2():
        print(x)
    return f2  # not the function, the reference of the function, meaning function definition is being returned, bag theory, closures (factory function) in python, vars go along with the reference

myResult = f1()
myResult()  # notice it is called, as the function was returned