"""
Python Function Arguments

Definition:
Arguments are values that you pass to a function.

Arguments allow a function to work with different values
every time it is called.

Without arguments:
A function always performs the same task.

With arguments:
A function becomes more flexible and reusable.

Syntax:

def function_name(parameter):
    # Code

function_name(argument)

Parameter:
A variable inside the function definition.

Argument:
The actual value passed to the function.
"""

# =====================================================
# Example 1
# =====================================================
# Function with one argument.

print("Example 1")


def greet(name):
    print("Hello,", name)


greet("Ali")

print("-" * 50)

# =====================================================
# Example 2
# =====================================================
# Calling the same function with different values.

print("Example 2")


def greet(name):
    print("Welcome,", name)


greet("Ahmed")
greet("Sara")
greet("John")

print("-" * 50)

# =====================================================
# Example 3
# =====================================================
# Display age.

print("Example 3")


def show_age(age):
    print("Age:", age)


show_age(10)

print("-" * 50)

# =====================================================
# Example 4
# =====================================================
# Display favorite color.

print("Example 4")


def favorite_color(color):
    print("Favorite Color:", color)


favorite_color("Blue")

print("-" * 50)

# =====================================================
# Example 5
# =====================================================
# Function with two arguments.

print("Example 5")


def student(name, age):
    print("Name:", name)
    print("Age:", age)


student("Ali", 12)

print("-" * 50)

# =====================================================
# Example 6
# =====================================================
# Add two numbers.

print("Example 6")


def add(number1, number2):
    print("Sum =", number1 + number2)


add(10, 20)

print("-" * 50)

# =====================================================
# Example 7
# =====================================================
# Multiply two numbers.

print("Example 7")


def multiply(number1, number2):
    print("Answer =", number1 * number2)


multiply(5, 4)

print("-" * 50)

# =====================================================
# Example 8
# =====================================================
# Display city and country.

print("Example 8")


def address(city, country):
    print(city + ", " + country)


address("Karachi", "Pakistan")

print("-" * 50)

# =====================================================
# Example 9
# =====================================================
# User input with arguments.

print("Example 9")


def welcome(name):
    print("Welcome,", name)


username = input("Enter your name: ")

welcome(username)

print("-" * 50)

# =====================================================
# Example 10
# =====================================================
# Three arguments.

print("Example 10")


def student_info(name, age, grade):
    print("Name :", name)
    print("Age  :", age)
    print("Grade:", grade)


student_info("Ali", 12, "A")

print("-" * 50)

# =====================================================
# Example 11
# =====================================================
# Positional arguments.

print("Example 11")


def introduce(name, city):
    print(name, "lives in", city)


introduce("Ahmed", "Lahore")

print("-" * 50)

# =====================================================
# Example 12
# =====================================================
# Keyword arguments.

print("Example 12")


def introduce(name, city):
    print(name, "lives in", city)


introduce(city="Karachi", name="Sara")

print("-" * 50)

# =====================================================
# Example 13
# =====================================================
# Default argument.

print("Example 13")


def country(name, country="Pakistan"):
    print(name, "lives in", country)


country("Ali")
country("John", "Canada")

print("-" * 50)

# =====================================================
# Example 14
# =====================================================
# Multiple function calls.

print("Example 14")


def say_hello(name):
    print("Hello,", name)


say_hello("Ali")
say_hello("Ahmed")
say_hello("Sara")
say_hello("John")

print("-" * 50)

# =====================================================
# Example 15
# =====================================================
# Shopping example.

print("Example 15")


def buy(item, quantity):
    print("Item     :", item)
    print("Quantity :", quantity)


buy("Apple", 5)

print("-" * 50)

# =====================================================
# Example 16
# =====================================================
# School marks.

print("Example 16")


def marks(student_name, score):
    print(student_name, "scored", score)


marks("Ahmed", 95)

print("-" * 50)

# =====================================================
# Example 17
# =====================================================
# Temperature.

print("Example 17")


def weather(city, temperature):
    print(city, "Temperature:", temperature)


weather("Dubai", "38°C")

print("-" * 50)

# =====================================================
# Example 18
# =====================================================
# Rectangle dimensions.

print("Example 18")


def rectangle(length, width):
    print("Length:", length)
    print("Width :", width)


rectangle(20, 10)

print("-" * 50)

# =====================================================
# Example 19
# =====================================================
# Pet information.

print("Example 19")


def pet(name, animal):
    print(name, "is a", animal)


pet("Tom", "Cat")

print("-" * 50)

# =====================================================
# Example 20
# =====================================================
# Pizza order.

print("Example 20")


def pizza(size, flavor):
    print("Size   :", size)
    print("Flavor :", flavor)


pizza("Large", "Pepperoni")

print("-" * 50)

# =====================================================
# Summary
# =====================================================

print("Summary")

print("Parameter : A variable inside the function definition.")
print("Argument  : The actual value passed to the function.")
print("Functions can receive one or more arguments.")
print("Arguments make functions reusable.")
print("Python supports positional, keyword, and default arguments.")