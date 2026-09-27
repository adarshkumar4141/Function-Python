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

# KEYWORD ARGUMENT DEFINITION :-A keyword argument passes a value by explicitly specifying the parameter name,so here order no matters.

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

# def show(*args):
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

# VARIABLE IN FUNCTION:-
# [1] Local Variable:-
# A local variable is created inside a function or block and can usually be used only there.

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

# THE LEGB RULE:-

# x="global"
# def outer():
#     x="enclosing"

#     def inner():
#         x="local"
#         print(x)
#     inner()
# outer()

# DOCSTRING:-
# A docstring (documentation string) is a special string written inside a function to describe what the function does, its parameters, and what it returns.
        
# def add(a,b):
#     """ Return the sum of two numbers"""
#     return a+b

# print(add.__doc__) -This is used to print output of a docstring.


#  DOCSTRING IN FUNCTION:-
# A docstring is placed immediately inside a function, usually using triple quotes:

# def add(a,b):
#     """This function adds two numbers."""
#     return a + b

# print(add.__doc__)

# FOR SUBTRACTION:-
# import operator
# a=operator.sub(10,4)
# print(a)



