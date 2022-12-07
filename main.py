# def add(x,y): #function 
#     return x+y
# print(add(1,2))

# first_name = "Rehnuma" #variable name can not have space
# print(first_name)

# is_online = False # boolean , case sensetive , can not use small f
# print(is_online)

# name = input("what is your name? ") #input type in python
# print("Hello " + name)

# #Type conversion 
# birth_year = input("Enter your birth year? ")
# age= 2022- int(birth_year)
# print(age)

# num1 = input("First number: ")
# num2 = input("Second number: ")
# sum = num1+num2
# print(sum)  # as input passes string so it only concatinate the input values

# num3 = input("First number: ")
# num4 = input("Second number: ")
# sum = int(num3)+int(num4)
# print(sum) 

# #Concatinating str and float
# num5 = input("First number: ")  # alternative: num5 = float(input("First number: "))
# num6 = input("Second number: ")
# sum = float (num5)+float (num6)
# print("The result is: " + str (sum)) 

# #Strings
# course = 'start python course'
# print(course)
# print(course.upper())
# print(course.find('y'))
# print(course.find('Y'))
# print(course.replace('start',''))
# print('python' in course) #special key word: in operator; will return bool

# # arithmatic operation
# print(10+3)
# print(10-3)
# print(10*3)
# print(10/3)
# print(10//3) # will return int
# print(10%3)
# print(10**3) #exponent

# #argumental assignment operator 
# x=10
# x += 3
# print(x)

# #operator precedence
# x= 10+3*2
# print(x)
# x= (10+3)*2
# print(x)

# #comparison operators(>,<,>=,<=,!=,==) ; they return bool
# x = 3>2
# print(x)
# x = 3==2
# print(x)
# x = 3==3
# print(x)
# x = 3!=2
# print(x)

# #logical operator(and, or, not); return bool 
# price = 25
# print(price >10 and price<30) # both true
# price = 5
# print(price >10 or price<30) # at least one true returns true 
# price = 25
# print(not price >10) #not = inverse result

# #if-else statement 
# temp = 35
# if temp>30:
#     print("It's a summer")
# elif temp<20:
#     print("It's winter")
# else: 
#     print("Can not detect")



# #dictionary 
# dicts = {
#     "key1" : "food",
#     "key2" : "flower",
#     "key2" : "fruit",  #Duplicate values will overwrite existing values:
#     "key3" : "flower",
#     "key4" : ["butterfly","star","hills"]
# }
# print(dicts)
# print(dicts["key1"])
# print(len(dicts))
# print(type(dicts))

# #The dict() Constructor

# dictionary = dict(key0="country", key1="division", key2="unioun")
# print(dictionary)

# #Creating Pie Charts 
# import matplotlib.pyplot as plt
# import numpy as np
# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

# plt.pie(y, labels = mylabels)
# plt.show() 

