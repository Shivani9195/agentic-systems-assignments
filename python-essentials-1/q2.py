# Program to take name and age input

# Take name inputs
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

try:
    # Take and convert age to integer
    age = int(input("Enter your age: "))

    # Check if age is negative
    if age < 0:
        print("Age cannot be negative")
    else:
        # Print required outputs
        print("Full Name:", first_name + " " + last_name)
        print("You will be", age + 1, "next year")

# Handle non-numeric age input
except ValueError:
    print("Invalid age input")