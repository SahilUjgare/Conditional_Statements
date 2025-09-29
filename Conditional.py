# Conditional Statements Examples in Python

# Example 1: Simple if statement
age = 20
if age >= 18:
    print("You are eligible to vote!")


# Example 2: if-else statement
number = 7
if number % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")


# Example 3: if-elif-else statement
marks = 85
if marks >= 90:
    print("Grade: A+")
elif marks >= 75:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
else:
    print("Grade: C")


# Example 4: Nested if statement
x = 15
if x > 0:
    if x % 5 == 0:
        print("Positive number divisible by 5")
    else:
        print("Positive number but not divisible by 5")
else:
    print("Not a positive number")
