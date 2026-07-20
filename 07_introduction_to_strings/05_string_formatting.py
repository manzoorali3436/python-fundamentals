"""
Python String Formatting

Definition:
String formatting is used to insert variables or values
into a string.

Python provides several ways to format strings:

1. Using commas (,)
2. Using the + operator
3. Using f-strings (Recommended)
4. Using the format() method
"""

# =====================================================
# Example 1
# =====================================================
# Using commas.

print("Example 1")

name = "Ali"
age = 12

print("My name is", name)
print("I am", age, "years old.")

print("-" * 50)

# =====================================================
# Example 2
# =====================================================
# Using the + operator.

print("Example 2")

first_name = "Ali"
last_name = "Khan"

full_name = first_name + " " + last_name

print(full_name)

print("-" * 50)

# =====================================================
# Example 3
# =====================================================
# f-string.

print("Example 3")

name = "Ahmed"
age = 15

print(f"My name is {name}.")
print(f"I am {age} years old.")

print("-" * 50)

# =====================================================
# Example 4
# =====================================================
# Multiple variables.

print("Example 4")

city = "Karachi"
country = "Pakistan"

print(f"I live in {city}, {country}.")

print("-" * 50)

# =====================================================
# Example 5
# =====================================================
# Simple calculation.

print("Example 5")

number1 = 10
number2 = 20

print(f"{number1} + {number2} = {number1 + number2}")

print("-" * 50)

# =====================================================
# Example 6
# =====================================================
# User input.

print("Example 6")

name = input("Enter your name: ")

print(f"Welcome, {name}!")

print("-" * 50)

# =====================================================
# Example 7
# =====================================================
# Display marks.

print("Example 7")

student = "Sara"
marks = 95

print(f"{student} scored {marks} marks.")

print("-" * 50)

# =====================================================
# Example 8
# =====================================================
# Shopping example.

print("Example 8")

item = "Apple"
quantity = 5

print(f"You bought {quantity} {item}s.")

print("-" * 50)

# =====================================================
# Example 9
# =====================================================
# Temperature.

print("Example 9")

city = "Dubai"
temperature = 38

print(f"The temperature in {city} is {temperature}°C.")

print("-" * 50)

# =====================================================
# Example 10
# =====================================================
# Price.

print("Example 10")

price = 99.99

print(f"The price is ${price}")

print("-" * 50)

# =====================================================
# Example 11
# =====================================================
# format() method.

print("Example 11")

name = "John"

print("Hello, {}!".format(name))

print("-" * 50)

# =====================================================
# Example 12
# =====================================================
# Multiple placeholders.

print("Example 12")

name = "Ali"
age = 20

print("Name: {} | Age: {}".format(name, age))

print("-" * 50)

# =====================================================
# Example 13
# =====================================================
# Number formatting.

print("Example 13")

pi = 3.14159265

print(f"Pi = {pi:.2f}")

print("-" * 50)

# =====================================================
# Example 14
# =====================================================
# Percentage.

print("Example 14")

score = 0.95

print(f"Score: {score:.0%}")

print("-" * 50)

# =====================================================
# Example 15
# =====================================================
# Align text.

print("Example 15")

name = "Python"

print(f"|{name:<10}|")
print(f"|{name:^10}|")
print(f"|{name:>10}|")

print("-" * 50)

# =====================================================
# Example 16
# =====================================================
# Repeat information.

print("Example 16")

name = "Ahmed"

print(f"{name} likes Python.")
print(f"{name} practices every day.")

print("-" * 50)

# =====================================================
# Example 17
# =====================================================
# Email.

print("Example 17")

email = "student@example.com"

print(f"My email is {email}")

print("-" * 50)

# =====================================================
# Example 18
# =====================================================
# Phone number.

print("Example 18")

phone = "03001234567"

print(f"My phone number is {phone}")

print("-" * 50)

# =====================================================
# Example 19
# =====================================================
# Favorite subject.

print("Example 19")

subject = "Mathematics"

print(f"My favorite subject is {subject}.")

print("-" * 50)

# =====================================================
# Example 20
# =====================================================
# Final review.

print("Example 20")

name = "Ali"
city = "Karachi"
age = 18

print(f"My name is {name}. I live in {city}. I am {age} years old.")

print("-" * 50)

# =====================================================
# Summary
# =====================================================

print("Summary")

print("Use commas (,) for simple output.")
print("Use + to join strings.")
print("Use f-strings for clean and readable formatting.")
print("Use format() when needed.")
print("You can insert variables directly into strings.")
print("You can format numbers using f-strings.")