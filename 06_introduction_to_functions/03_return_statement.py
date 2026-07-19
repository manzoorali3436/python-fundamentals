"""
Python Return Statement

Definition:
The return statement is used to send a value back
from a function.

Unlike print(), return allows you to save the value,
use it later, or perform more operations on it.

Syntax:

def function_name():
    return value
"""

# =====================================================
# Example 1
# =====================================================
# Return a number.

print("Example 1")


def get_number():
    return 10


number = get_number()

print(number)

print("-" * 50)

# =====================================================
# Example 2
# =====================================================
# Return a string.

print("Example 2")


def get_name():
    return "Ali"


name = get_name()

print(name)

print("-" * 50)

# =====================================================
# Example 3
# =====================================================
# Return the sum of two numbers.

print("Example 3")


def add(number1, number2):
    return number1 + number2


result = add(10, 20)

print("Sum =", result)

print("-" * 50)

# =====================================================
# Example 4
# =====================================================
# Return the multiplication of two numbers.

print("Example 4")


def multiply(number1, number2):
    return number1 * number2


answer = multiply(5, 6)

print(answer)

print("-" * 50)

# =====================================================
# Example 5
# =====================================================
# Return a greeting message.

print("Example 5")


def welcome(name):
    return "Welcome " + name


message = welcome("Ahmed")

print(message)

print("-" * 50)

# =====================================================
# Example 6
# =====================================================
# Return True or False.

print("Example 6")


def is_adult(age):
    return age >= 18


print(is_adult(20))
print(is_adult(12))

print("-" * 50)

# =====================================================
# Example 7
# =====================================================
# Store the returned value.

print("Example 7")


def square(number):
    return number * number


result = square(8)

print(result)

print("-" * 50)

# =====================================================
# Example 8
# =====================================================
# Use the returned value in another calculation.

print("Example 8")


def add(number1, number2):
    return number1 + number2


total = add(10, 20)

print(total + 100)

print("-" * 50)

# =====================================================
# Example 9
# =====================================================
# Return user input.

print("Example 9")


def get_username():
    name = input("Enter your name: ")
    return name


username = get_username()

print("Hello,", username)

print("-" * 50)

# =====================================================
# Example 10
# =====================================================
# Return the largest number.

print("Example 10")


def largest(number1, number2):
    if number1 > number2:
        return number1

    return number2


print(largest(50, 30))

print("-" * 50)

# =====================================================
# Example 11
# =====================================================
# Return a list.

print("Example 11")


def fruits():
    return ["Apple", "Banana", "Orange"]


print(fruits())

print("-" * 50)

# =====================================================
# Example 12
# =====================================================
# Return multiple values.

print("Example 12")


def student():
    return "Ali", 12


name, age = student()

print(name)
print(age)

print("-" * 50)

# =====================================================
# Example 13
# =====================================================
# Return the length of a word.

print("Example 13")


def word_length(word):
    return len(word)


print(word_length("Python"))

print("-" * 50)

# =====================================================
# Example 14
# =====================================================
# Difference between print() and return.

print("Example 14")


def using_print():
    print("Hello")


def using_return():
    return "Hello"


using_print()

message = using_return()

print(message)

print("-" * 50)

# =====================================================
# Example 15
# =====================================================
# Return a full name.

print("Example 15")


def full_name(first_name, last_name):
    return first_name + " " + last_name


print(full_name("Ali", "Khan"))

print("-" * 50)

# =====================================================
# Example 16
# =====================================================
# Return a discount.

print("Example 16")


def discount(price):
    return price * 0.10


print(discount(100))

print("-" * 50)

# =====================================================
# Example 17
# =====================================================
# Return an even number check.

print("Example 17")


def is_even(number):
    return number % 2 == 0


print(is_even(10))
print(is_even(9))

print("-" * 50)

# =====================================================
# Example 18
# =====================================================
# Return the first letter.

print("Example 18")


def first_letter(word):
    return word[0]


print(first_letter("Python"))

print("-" * 50)

# =====================================================
# Example 19
# =====================================================
# Return a sentence.

print("Example 19")


def sentence():
    return "Learning Python is fun."


print(sentence())

print("-" * 50)

# =====================================================
# Example 20
# =====================================================
# Return today's goal.

print("Example 20")


def goal():
    return "Practice Python every day."


print(goal())

print("-" * 50)

# =====================================================
# Summary
# =====================================================

print("Summary")

print("print() displays a value on the screen.")
print("return sends a value back from a function.")
print("A returned value can be stored in a variable.")
print("A returned value can be used in another calculation.")
print("A function can return numbers, strings, lists, booleans, and more.")