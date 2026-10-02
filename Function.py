# INTRO TO THE FUNCTION IN PYTHON:-
# a=2
# b=3
# c=4
# Average=a+b+c/3
# print(Average) -This is not suitable approach for finding avg of big data set again and again. 

# def greet(name):
#     print("hello")
# greet("name")

# FUNCTION WITH PARAMETER:-
# def hello(a,b):
#     print(a+b)
# hello(10,20)

# def quad(a,b):
#     print(a+b)
# quad(10,20)

# def chauhan(name):
#     print("Welcome",name)
# chauhan("adarsh")
# print(type(chauhan))

# def adarsh(name):
#     print("Welcome",name)
# adarsh("damodar")
# print(type(adarsh))

# def data(name):
#     print("Good",name)
# data("Day")
# print(type(data))

# def Add(a,b):
#     print(a+b)
# Add(10,30)
# Add(20,50) -This show we have not repeat the code only we call the function(Add) again and again for different add .

# FUNCTION WITH RETURN:-
# def add(a,b):
#     return a+b
# result=add(20,50)
# print(result)

# def ac(a,b):
#     return a*b
# result=ac(20,50)
# print(result)

# def Adarsh():
#     return 
# result=Adarsh()
# print(result) -RESULT WILL GIVE NONE BACAUSE RETURN CONTAINS NOTHING.

# def calculate(a,b):
#     return a+b, a-b ,a*b
# result = calculate(50,10)
# print(result)

# def adarsh(a,b):
#     return a/b,a*b,a%b
# result=adarsh(20,5)
# print(result)

# FUNCTION WITHOUT PARAMETER:-  
# def greet():
#     print("Good","Morning")
# greet()

# def adarsh():
#     print("Adarsh","Rajput")
# adarsh()

# FUNCTION WITH MULTIPLE PARAMETER:-
# def student(name,age,course):
#     print("Name:",name)
#     print("Age:",age)
#     print("Course:",course)
# student("ADARSH",18,"BTECH")


# POSTIONAL ARGUMENT:-
# The first argument goes to the first parameter, the second argument goes to the second parameter, and so on.

# KEYWORD ARGUMENT:-A keyword argument passes a value by explicitly specifying the parameter name,so here order no matters.

# *ARGS:-
# *Args allows a function to accept any number of positional arguments.
# def add(*args):
#     print(*args)
# add(10,20,30,40)

# def add(*numbers):
#     return sum(numbers)
# print(add(10,20))
# print(add(10,30,60,45,70,90))

# def show(*args):
#      print(type(args))
#      print(sum(args))

# show(1,2)

# # def show(*args):
#     print(args[1])
#     print(args[2])
# show(100,200,300)

# def show(*args):
#     print(args[1])
#     print(args[2])
# show(10,20,30)

# **KWARGS:-
# def student(**details):
#     print(details)
# student(name="Aman",age=18,course="Btech")

# def define(**structure):
#     print(structure)
# define(name="Adarsh",age=18,field="CSE")

# def show (**k):
#     print (k)
#     print(k["name"])
# show(name="Aman",age=20)

# COMBINATION OF BOTH ARGS AND KWARGS:-

# def function(*args,**kwargs):
#     print(args)
#     print(kwargs)
# function(10,20,30,40,name="adarsh",age=20,school="Udayan")

# def show(*bmw,**audi):
#     print(bmw,audi)
# show("Fortuner","scorpio","Thar",name="G-wagon",type="Luxury",Version="Electric",Model="2026")


# VARIABLE IN FUNCTION:-
# [1] Local Variable:- means variable only create inside the function.
# A local variable is created inside a function or block and can usually be used only there.

# def greet(name):
#      print("Welcome",name)
# greet("Mumbai Indians")

# def test(name):
#  print("x=10",name)
# test("Math")

# def greet():
#     print("welcome")
# greet() -here welcome is local to greet .trying to use welcome outside the function will cause an error.

# [2] Global variable:-
# A global variable is created outside functions and can generally be accessed from different parts of the program.

# name="Jhon"
# def greet():
#     print(name)
# greet()
# print(name)

# x=100
# def test():
#     print(x)
# test()

# x=10 
# def test():
#     global x
#     x=50
# test()
# print(x)

# x=100
# def test():
#     x=200
# test()
# print(x)

# CHANGING A GLOBAL VARIABLE INSIDE A FUNCTION:-
# To modify (not just read) a global variable from inside a function, you must declare it with global.
# x=10
# def change():
#         global x -here we use global keyword to update.
#         x=50
# change()
# print(x)

# count=20
# def update():
#     global count
#     count=30
# update()
# print(count)

# THE LEGB RULE:-The LEGB rule tells us the order in which Python searches for a variable or name.
# LEGB = Local → Enclosing → Global → Built-in
# EXAMPLE OF LEGB RULE:-

# def outer():
#     x="enclosing"
#     def inner():
#         x=20 - Here 20 is output because python follow legb rule first local then afterwards.
#         print(x)
#     inner()
# outer()


# x=20
# def outer():
#     name="Adarsh"
#     def inner():
#         print(name) - here inner() can access name of outer()as a enclosing function.
#     inner()
# outer()


# city="Japla"
# def outer():

#     def inner():
#         print(city)-here global variable is print as output japla.
#     inner()   
# outer() 


# def show():
    
#     print(len("Rajputana")) - this is example of built-in function .
# show()

# x=20
# def outer():
#     name="Don"
#     def inner():
#         print(name)
#         print(len("Quad AI"))
#     inner()
# outer()

# ENCLOSING SCOPE:-
# Enclosing scope is the scope of an outer function when you have a function defined inside another function.
# In simple words,Enclosing scope = the scope of the outer function that surrounds the inner function.
# x="global"
# def outer():
#     x="enclosing"

#     def inner():
#         x="local"
#         print(x)
#     inner()
# outer()

# def outer():
#     message="Hello"
#     def inner():
#         print(message)
#     inner()
# outer()


# BUILT-IN FINCTION:-
# Built-in functions are functions that are already provided by Python, so we can use them without defining them ourselves.
# x="ADARSH CHAUHAN"
# print(len(x))

# name="Japla"
# print(len(name))


# DOCSTRING:-
# A docstring (documentation string) is a special string written inside a function to describe what the function does, its parameters, and what it returns.
        
# def add(a,b):
#     """ Return the sum of two numbers"""
#     return a+b

# print(add.__doc__) -This is used to print output of a docstring.


#  DOCSTRING IN FUNCTION:-
# A docstring (documentation string) is a string written inside a function to describe what the function does.
# It is mainly used to make your code easy to understand and document.
# A docstring is placed immediately inside a function, usually using triple quotes:

# def add(a,b):
#     """This function adds two numbers."""
#     return a + b

# print(add.__doc__) -Python provides the __doc__ attribute to see a docstring in an output.

# def greet():
#     """ This fuction has greeting message""" -this is docstring.It tells another programmer what the greet() function does.

#     print("Hello Adarsh")
# greet()

# def show(a,b):
#     """ This function add two numbers"""
#     return a+b
# result=show(10,20)
# # print(result)

# def hello():
#     """ Welcome to Indian Railways"""
# print(hello.__doc__)

# FUNCTION ARE FIRST CLASS OBJECT IN PYTHON:-
# Functions are first-class objects in Python because
# they can be assigned to variables, passed as arguments, returned from functions, and stored in data structures just like other objects.

# 1.Assign a Function to a Variable:-
# def greet():
#    print("Hello")

# message=greet
# message()

# 2.Pass a Function as an Argument:-
# def greet():
#    print("Hello")
# def execute(func):
#       func()
# execute(greet)

# 3.Return a Function from Another Function:-
# def outer():
#     def inner():
#         print("Hello from inner function")

#     return inner

# my_function = outer()

# my_function()


# SOME ANOTHER TOPIC:-
# import math
# a=math.sqrt(16)
# print(a)

#import operator
# a=operator.sub(10,4)
# print(a)
