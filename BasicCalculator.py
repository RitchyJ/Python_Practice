# != means not equal to. below we check to make sure that you cannot devide by 0.
#using "not in" allows you to make sure it doesn't fire if it is not one of the selections. this way they cannot deviate from the operations
#using "in" allows you to make sure it fires if it is in one of the selections

# Input the operator
operator = input("Enter an operator (+ - * /): ")

# Validate the operator
if operator not in ["+", "-", "*", "/"]:
    print("This is not a valid operation")

else:
    # Input the numbers if the operator is valid
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))

    # Perform the operation
    if operator == "+":
        result = num1 + num2
        print(f"The result of {num1} + {num2} is: {result}")
    elif operator == "-":
        result = num1 - num2
        print(f"The result of {num1} - {num2} is: {result}")
    elif operator == "*":
        result = num1 * num2
        print(f"The result of {num1} * {num2} is: {result}")
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is: {result}")
        else:
            print("Error: Division by zero is not allowed!")