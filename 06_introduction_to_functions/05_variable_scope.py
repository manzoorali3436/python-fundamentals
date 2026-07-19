"""
Python Variable Scope

Definition:
Variable scope determines where a variable can be
accessed in your program.

Python has two main types of scope:

1. Local Scope
2. Global Scope
"""

# =====================================================
# Example 1
# =====================================================
# Global variable.

print("Example 1")

name = "Ali"


def greet():
    print("Hello,", name)


greet()

print(name)

print("-" * 50)

# =====================================================
# Example 2
# =====================================================
# Local variable.

print("Example 2")


def student():
    age = 12
    print("Age:", age)


student()

print("-" * 50)

# =====================================================
# Example 3
# =====================================================
# Local variables belong only to the function.

print("Example 3")


def school():
    classroom = "Grade 5"
    print(classroom)


school()

# print(classroom)
# This would cause an error because
# classroom is a local variable.

print("-" * 50)

# =====================================================
# Example 4
# =====================================================
# Global variable can be used inside a function.

print("Example 4")

city = "Karachi"


def address():
    print(city)


address()

print("-" * 50)

# =====================================================
# Example 5
# =====================================================
# Local and global variables can have
# the same name.

print("Example 5")

name = "Ahmed"


def student():
    name = "Ali"
    print("Inside Function:", name)


student()

print("Outside Function:", name)

print("-" * 50)

# =====================================================
# Example 6
# =====================================================
# Changing a global variable.

print("Example 6")

score = 50


def update_score():
    global score
    score = 100


update_score()

print(score)

print("-" * 50)

# =====================================================
# Example 7
# =====================================================
# Multiple functions using one global variable.

print("Example 7")

school_name = "ABC School"


def teacher():
    print(school_name)


def student():
    print(school_name)


teacher()
student()

print("-" * 50)

# =====================================================
# Example 8
# =====================================================
# Different local variables.

print("Example 8")


def first():
    number = 10
    print(number)


def second():
    number = 20
    print(number)


first()
second()

print("-" * 50)

# =====================================================
# Example 9
# =====================================================
# Global variable with calculation.

print("Example 9")

tax = 5


def calculate_price(price):
    print(price + tax)


calculate_price(100)

print("-" * 50)

# =====================================================
# Example 10
# =====================================================
# Local variable with calculation.

print("Example 10")


def add():
    number1 = 10
    number2 = 20

    print(number1 + number2)


add()

print("-" * 50)

# =====================================================
# Example 11
# =====================================================
# Local variable is recreated every time.

print("Example 11")


def counter():
    count = 1
    print(count)


counter()
counter()

print("-" * 50)

# =====================================================
# Example 12
# =====================================================
# Using a global constant.

print("Example 12")

PI = 3.14159


def show_pi():
    print(PI)


show_pi()

print("-" * 50)

# =====================================================
# Example 13
# =====================================================
# Local variables in different functions.

print("Example 13")


def cat():
    sound = "Meow"
    print(sound)


def dog():
    sound = "Woof"
    print(sound)


cat()
dog()

print("-" * 50)

# =====================================================
# Example 14
# =====================================================
# User input stored in a local variable.

print("Example 14")


def welcome():
    name = input("Enter your name: ")
    print("Hello,", name)


welcome()

print("-" * 50)

# =====================================================
# Example 15
# =====================================================
# Global variable shared by many functions.

print("Example 15")

country = "Pakistan"


def capital():
    print(country)


def currency():
    print(country)


capital()
currency()

print("-" * 50)

# =====================================================
# Summary
# =====================================================

print("Summary")

print("Local Variable")
print("- Created inside a function.")
print("- Can only be used inside that function.")

print()

print("Global Variable")
print("- Created outside a function.")
print("- Can be used inside and outside functions.")

print()

print("Use the 'global' keyword only when you need to")
print("change a global variable inside a function.")