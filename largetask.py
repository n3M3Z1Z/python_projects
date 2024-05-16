#!/ust/bin/env python3

def calculator():
    # User inputs for numbers and operation
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose an operation (+, -, *, /): ")

    # Calculation based on the selected operation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        # Checking for division by zero
        if num2 == 0:
            print("Error: Division by zero is not allowed. Drink a coffe while you refresh your math")
            return
        else:
            result = num1 / num2
    else:
        print("Invalid operation!")
        return

    # Output the result
    print("Result:", result)

    # Ask if the user wants to perform another calculation Y for Yes; N for no
    repeat = input("Do you want to perform another calculation? (Y/N): ").lower()
    if repeat == 'yes':
        calculator()
    else:
        print("The program will be terminated.")

# Call the function to start the calculator
calculator()