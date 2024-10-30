while True:
    years = float(input("Enter the amount of years you would like to convert to days: "))
    days = years * 365
    print(f"there are about {days} days in {years} years")#\

    again = input("Would you like to do another conversion? yes/no: ")
    if again.lower() != "yes":
        break