# DAY 1: Intro/Variables/Typecasting/UserInput

import time
# Variable = A container for a value (String, Integer, Float, Boolean)
#   A variable behaves as if it was the value it contains
# F-string = An f-string in Python is a way to insert variables or expressions directly into a string using {} and prefixing the string with f.
#   This is an example of F-String

#first_name = "Ritchy"
#food = "Pizza"
#email = "FakeEmail123@fake.com"
#print (f"Hey, whats up {first_name}")
#print(f"Don't you like {food}?")
#print(f"Your email is {email}")

# Integer = An integer is a whole number (positive, negative, or zero). Cannot be in parenthesis
#age = 22
#Quantity = 3
#num_of_students = 30
#print (f"You are {age} years old")
#print (f"You are buying {Quantity} Boxes")
#print (f"Is that enough to feed the {num_of_students} in your class?")

# Float = A float is a data type that represents numbers with decimal points
#price = 10.99
#gpa = 3.2
#distance = 5.5

#print(f"The total price is ${10.99} per box")
#print(f"Only those with a GPA above {gpa} will get a slice")
#print(f"The store is about {distance} miles away")

# Boolean = A boolean is a data type that represents one of two values: True or False.

#is_student = False
#for_sale = True
#is_online = True
#if is_student:
#    print("You are a student")
#else:
#    print("You are NOT a student")

#if for_sale:
#    print("That Item is for Sale")
#else:
#    print("That Item is NOT Available")
#if is_online:
#    print("You are Online")
#else:
#    print("You are Offline")

# Typecasting = The process of converting a variable from one data type to another
#       str(), int(), float(). bool()
# Typecasting is super useful when handling user input. User input is always a string

#name = "Ritchy Joseph"
#age = 22
#gpa = 3.5
#is_student = True

#roundedgpa = int(gpa)
#print(roundedgpa)

#decimal_age = float(age)
#print(decimal_age)

# If you turn a number into a string type function, its like doing "22" instead of the numerical amount. Example below
#age = str(age)
#print(age)

#decimal_age += 2
#print(decimal_age)

# When you typecast a string into a boolean in Python, any non-empty string is converted to True, while an empty string ("") is converted to False.
#name = bool(name)
#print(name)

# When you typecast an integer/float into a boolean in Python, the integer 0 is converted to False, while any non-zero integer is converted to True.
#age = bool(age)
#print(age)

# Input() = A function that prompts the user to enter data. User input is stored as strings
#   Returns the entered data as a string

#name = input("What is your name?: ")
# You can enclose the input into a typecast to not take extra lines
#age = int(input("How old are you?: "))

#age = age + 1

#print(f"Hey, {name}, how's it been?")
#print("HAPPY BIRTHDAY!")
#print(f"Oh dang, you're turning {age} next year? Time Flys!")

# Exercise 1
# Time.sleep() is used as a Wait function
#age = int(input("How old are you again?: "))
#year = int(input("What year are we in?: "))
#birthday_year = year - age
#birthday_year_early = birthday_year - 1
#print("Hmm....let me think")
#time.sleep(2)
#print("Ok, I think I got it")
#time.sleep(1)
#print(f"You were born between {birthday_year_early}, and {birthday_year}?")

# Exercise 2

#item = input("What item would you like to buy?: ")
#price = float(input("What is the price?: "))
#quantity = int(input("How many would you like?: "))
#total = price * quantity

#print(f"You have bought {quantity} x {item}/s. The total will be ${total}")


# Day 2: Arithmetic Operators/Math Functions/if statements

#friends = 10
# friends = friends + 1
#friends += 1
# friends = friends - 2
#friends -= 2
# friends = friends * 3
#friends *= 3
# friends = friends / 2
#friends /= 2
# friends - friends ** 2
#friends **= 2
#print(friends)
#remainder = friends % 3

# % is used to calculate the remainder. example, friends % 3 will print to 1 since friends = 10 and 10/3 will leave 1 remainder
# print(f"The remainder is {remainder}")

#x = 3.14
#y = 4
#z = 5
# abs is absolute value. determins how far it is from 0
# pow is to the power. must reference 2 numbers. example pow(4, 3) is 4 to the power of 3
# max is the maximum value between a set of numbers
# min is the minimum value between a set of numbers

#results = round(x)
#results = abs(y)
#results = pow(4, 3)
#results = min(x, y, z)
#results = max(x, y, z)
#print(results)

#must import math to call for advance math functions
#can call for pi with math.pi and constant with math.e
#can call for square root with math.sqrt
#ceil rounds up and floor rounds down

import math
#x = 9.9
#print(math.pi)
#print(math.e)
#results = math.sqrt(x)
#results = math.ceil(x)
#results = math.floor(x)
#print(results)

#radius = float(input("Enter the Radius of a circle: "))
#circumference = 2 * math.pi * radius

#you can round to a given decimal place by stating the amount after. example {round(circumference, 2)}
#print(f"The circumference is rounded to: {round(circumference, 2)}cm")

#radius = float(input("Enter the Radius of a circle: "))
#area = math.pi * pow(radius, 2)
#print(f"The radius of this circle is: {round(area, 2)}cm^2")

#to calculate c you need the square root of a squared + b squared
#a = float(input("Enter side A: "))
#b = float(input("Enter side B: "))

#c = math.sqrt(pow(a, 2) + pow(b, 2))

#print(f"Side C = {c}")

# if = Do some code only IF some condition is True
# Else do something else
# Any code under an If statement needs to be indented
# elif = else if. allows you to do another else/if statement under the if
# if statements function off of priority. it will not reach elif function 3 if function 1 is true
# to check if something is equal you use 2 signs. example: ==


#create = input("Would you like to create an account? (Yes/No): ")
#if create == "Yes":
#    print("Ok, we can help you with that.")

#    name = input("Enter your name: ")
#    if name == "":
#        print("Sorry, you did not enter your name!")
#    else:
#        print(f"Hello {name}")

#    age = int(input("Enter your age: "))
#    if age >= 18:
#        print(f"You are now signed up {name}!")
#    elif age < 0:
#        print("You haven't been born yet!")
#    else:
#        print("Sorry, must be 18+ to sign up")
#elif create == "No":
#    print("We will be returning you to the main Menu")
#else:
#    print("This is not a valid response. Please Try again.")

# You can also use boolean with if statements as shown below

#online = True

#if online:
#    print("The user is online!")
#else:
#    print("The user is offline!")

# Day 3: Calculator Program
import math

# != means not equal to. below we check to make sure that you cannot devide by 0.
#using "not in" allows you to make sure it doesnt fire if it is not one of the selections. this way they cannot deviate from the operations
#using "in" allows you to make sure it fires if it is in one of the selections

# Input the operator
#operator = input("Enter an operator (+ - * /): ")

# Validate the operator
#if operator not in ["+", "-", "*", "/"]:
#    print("This is not a valid operation")
#
#else:
    # Input the numbers if the operator is valid
#    num1 = float(input("Enter the 1st number: "))
#    num2 = float(input("Enter the 2nd number: "))

    # Perform the operation
#    if operator == "+":
#        result = num1 + num2
#        print(f"The result of {num1} + {num2} is: {result}")
#    elif operator == "-":
#        result = num1 - num2
#        print(f"The result of {num1} - {num2} is: {result}")
#    elif operator == "*":
#        result = num1 * num2
#        print(f"The result of {num1} * {num2} is: {result}")
#    elif operator == "/":
#        if num2 != 0:
#            result = num1 / num2
#            print(f"The result of {num1} / {num2} is: {result}")
#        else:
#            print("Error: Division by zero is not allowed!")

# Day 4: Weight Conversion Program/Temperation Conversion Program

#Weight conversion
#weight = float(input("Enter your weight: "))
#unit = input ("Kilograms or Pounds? (K or L): ")

#if unit == "K":
#    weight = weight * 2.205
#    unit = "Lbs"
#elif unit == "L":
#    weight = weight / 2.205
#    unit = "Kgs"
#else:
#    print(f"{unit} was not valid")
#print(f"Your weight is: {round(weight, 1)}{unit}")

#Temp Conversion
#unit = input("Its the temperature in Celcius or Fahrenheit (C/F): ")
#temp = float(input("Enter the temperature: "))

#if unit == "C":
#    temp = round((9 * temp) / 5 + 32, 1)
#    print(f"The temperature in Fahrenheit is: {temp} F")
#elif unit == "F":
#    temp = round((temp - 32) * 5 / 9, 1)
#    print(f"The temperature in Celcius is: {temp} C")
#else:
#    print(f"{unit} is an invalid unit of measurement")

# Day 5: Logical Operators/Conditional Expressions/String Methods
# Logical Operators = evaluate multiple conditions (or, and, not)
#   or = at least one condition must be true
#   and = both conditions must be true
#   not = inverts the condition (not False, not True)

#temp = -1
#is_raining = False

#if temp > 35 or temp < 0 or is_raining:
#    print("The outdoor event is cancelled")
#else:
#    print("The outdoor event is still scheduled")

#temp = 20
#is_sunny = False

#if temp >= 28 and is_sunny:
#    print("It is HOT outside")
#    print("It is SUNNY")
#elif temp <= 0 and is_sunny:
#    print("It is Cold Outside")
#    print("It is SUNNY")
#elif 28 > temp > 0 and is_sunny:
#    print("It is WARM Outside")
#    print("It is SUNNY")
#elif temp >= 28 and is_sunny:
#    print("It is WARM Outside")
#    print("It is SUNNY")
#elif temp >= 0 and not is_sunny:
#    print("It is Hot outside")
#    print("It is Cloudy")
#elif 28 > temp > 0 and not is_sunny:
#    print("It is WARM Outside")
#    print("It is Cloudy")
#else:
#    print("It is not Sunny")

#   Conditional Expression = A one-line shortcut for the if-else statement (ternary operator)
#       Print or Assign one of two values based on a condition
#       X if condition else Y

#num = 5
#a = 6
#b = 7
#age = 25
#temp = 30
#user_role = "admin"
#print("Positive" if num > 0 else "Negative")
#result = "Even" if num %2 == 0 else "Odd"
#max_num = a if a > b else b
#min_num = a if a < b else b
#status = "Adult" if age > 18 else "Child"
#weather = "Hot" if temp > 20 else "Cold"
#access_level = "Full Access" if user_role == "Admin" else "Limited Access"

#print(result)
#print(min_num)
#print(status)
#print(weather)
#print(user_role)

#   String Methods
# len() function in Python tells you how many items are in something, like how many characters in a word or how many elements in a list.
# find() will return first occurance of a given character
# rfind() shows the last occurance
# capitalize() converts the first character into a uppercase
# upper() makes all characters uppercased
# lower() makes all characters lowercased
# isdigit() if it contiains only digits it will come back as true of false
# isdigit() if it contiains only alphabetical characters it will come back as true of false (a space is not a alphabet)
# count() will count how many characters are in a string
# replace() will replace any occurance of 1 character with another
# help() shows detailed information or documentation about functions, modules, or objects to explain how they work.

#name = input("Enter your Full Name: ")
#phone_number = input("Enter your Phone Number: ")

#result = len(name)
#result = name.find("R")
#result = name.rfind("i")
#name = name.capitalize()
#name = name.upper()
#name = name.lower()
#result = name.isdigit()
#name = name.isalpha()

#result = phone_number.count("-")
#phone_number = phone_number.replace(" ","-")
#print(name)
#print(phone_number)
#print(phone_number)


# Day 6: String Indexing/Format Specifiers/While Loops
# indexing = accessing elements of a sequence using [] (indexing operator)
# [start: end : step ]

#credit_number = "1234-5678-9012-3456"
#print(credit_number[5])
#print(credit_number[0:4])
#print(credit_number[5:9])
#last_digits = credit_number[-4:]
#print(f"XXXX-XXXX-XXXX-{last_digits}")

# Format Specifiers = {value:flags} format a value absed on what flags are inserted

#price1 = 3.14159
#price2 = -987.65
#price3 = 12.34

#print(f"Price 1 is ${price1:.2f}")
#print(f"Price 2 is ${price2:10}")
#print(f"Price 2 is ${price2:+}")
#print(f"Price 3 is ${price3:^10}")

# While Loop = Execute some code while some condition remains true

#name = input("Enter your name: ")
#while name == "":
#    print("You did not enter your name")
#    name = input("Enter your name: ")
#else:
#    print(f"Hello {name}")
#
#age = int(input("Enter your Age: "))
#
#while age < 21:
#    print("You are not of age to order a Drink")
#    age = int(input("Enter your Age: "))
#print(f"You are {age} years old")

#drink = input("What would you like to have? (q to quit): ")
#while not drink == "q":
#    print(f"You have ordered {drink}")
#    drink = input("What else would you like to have? (q to quit): ")
#print("bye")

#num = int(input("Enter a # between 1 - 10: "))

#while num < 1 or num > 10:
#    print(f"{num} is not valid")
#    num = int(input("Enter a # between 1 - 10: "))
#print(f"Your number is {num}")

# Day 7: Compound Interest Calculator/For Loops/Lists, Sets, Tuples/Shopping Cart Program


# Day 8: asd asd s