"""
Python Functions

Definition:
A function is a reusable block of code that performs
a specific task.

Instead of writing the same code again and again,
you can write it once inside a function and use it
whenever you need it.

Think of a function like a juice machine.

🍊 You put oranges into the machine.
🥤 The machine makes juice.
😊 Every time you want juice, you simply use the machine again.

Syntax:

def function_name():
    # Code

function_name()
"""

# =====================================================
# Example 1
# =====================================================
# Creating and calling a function.

print("Example 1")


def greet():
    print("Hello, World!")


greet()

print("-" * 50)

# =====================================================
# Example 2
# =====================================================
# Calling a function multiple times.

print("Example 2")


def say_hello():
    print("Hello!")


say_hello()
say_hello()
say_hello()

print("-" * 50)

# =====================================================
# Example 3
# =====================================================
# Welcome message.

print("Example 3")


def welcome():
    print("Welcome to Python!")


welcome()

print("-" * 50)

# =====================================================
# Example 4
# =====================================================
# Birthday message.

print("Example 4")


def birthday_message():
    print("🎂 Happy Birthday!")


birthday_message()

print("-" * 50)

# =====================================================
# Example 5
# =====================================================
# Animal sound.

print("Example 5")


def cat_sound():
    print("Meow! 🐱")


cat_sound()

print("-" * 50)

# =====================================================
# Example 6
# =====================================================
# School bell.

print("Example 6")


def school_bell():
    print("🔔 Ring Ring!")


school_bell()

print("-" * 50)

# =====================================================
# Example 7
# =====================================================
# Draw a separator.

print("Example 7")


def separator():
    print("=" * 30)


separator()
print("Section One")
separator()

print("-" * 50)

# =====================================================
# Example 8
# =====================================================
# Simple calculator.

print("Example 8")


def add_numbers():
    number1 = 10
    number2 = 20

    print("Sum =", number1 + number2)


add_numbers()

print("-" * 50)

# =====================================================
# Example 9
# =====================================================
# User greeting.

print("Example 9")


def greet_user():
    name = input("Enter your name: ")

    print(f"Hello, {name}!")


greet_user()

print("-" * 50)

# =====================================================
# Example 10
# =====================================================
# A function can be called many times.

print("Example 10")


def smile():
    print("😊 Keep Learning Python!")


smile()
smile()
smile()

print("-" * 50)

# =====================================================
# Summary
# =====================================================

print("Summary")

print("✔ A function is a reusable block of code.")
print("✔ Functions help avoid repeating code.")
print("✔ Use 'def' to create a function.")
print("✔ Call the function using its name followed by ().")