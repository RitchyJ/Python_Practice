import time
from datetime import datetime
from turtledemo.penrose import start

while True:
    start = input("Would you like me to guess your birth year?: ")
    if start.lower() == "yes":
        while True:
            name = input("Enter your Name: ")
            if name.isalpha():
                break
            else:
                print("Invalid input. Please use letter characters for your name.")
        time.sleep(.2)
        print(f"Hello {name}, Welcome back.")
        time.sleep(.5)
# You can enclose the input into a typecast to not take extra lines
        while True:
            try:
                age = int(input("Enter your age: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number for your age.")

        current_year = datetime.now().year
        current_month = datetime.now().month
        while True:
            had_birthday = input("Have you had your birthday yet this year? (yes/no): ")
            if had_birthday.lower() == "yes":
                birth_year = current_year - age
            elif had_birthday.lower() == "no":
                birth_year = current_year - age - 1
                break
            else:
                print("Invalid response, please select (yes/no)")

        print("Processing")
        time.sleep(2)
        print("Complete!")
        time.sleep(1)
        print(f"By my calculation, you were born on the year {birth_year}")
    else:
        print("We will end this program")