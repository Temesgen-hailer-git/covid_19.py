
# A simple, single-calculation calculator.
try:
    # Get the two numbers and the operator from the user.
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter an operator (+, -, *, /): ")

    # Perform the calculation based on the operator.
    if operator == '+':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operator == '-':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operator == '*':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif operator == '/':
        # Handle division by zero.
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Invalid operator.")

except ValueError:
    print("Invalid input. Please enter a number.")