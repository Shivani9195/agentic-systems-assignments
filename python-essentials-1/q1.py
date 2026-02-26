#Part 1: Number Operations with Error Handling

try:
    # Take input from user
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Check division by zero
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        # Calculate and print results
        print("Sum:", num1 + num2)
        print("Division:", num1 / num2)

# Handle non-numeric input
except ValueError:
    print("Invalid input")