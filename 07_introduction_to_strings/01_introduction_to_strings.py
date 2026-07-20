"""
Python Strings

Definition:
A string is a sequence of characters used to store text.

A string can contain:
- Letters
- Numbers
- Spaces
- Symbols

Strings are created by enclosing text inside:
- Single quotes (' ')
- Double quotes (" ")

Examples:
"Hello"
'Python'
"123"
"""

# =====================================================
# Example 1
# =====================================================
# Creating a string.

print("Example 1")

name = "Ali"

print(name)

print("-" * 50)

# =====================================================
# Example 2
# =====================================================
# Using single quotes.

print("Example 2")

city = 'Karachi'

print(city)

print("-" * 50)

# =====================================================
# Example 3
# =====================================================
# String containing numbers.

print("Example 3")

number = "12345"

print(number)

print(type(number))

print("-" * 50)

# =====================================================
# Example 4
# =====================================================
# String with spaces.

print("Example 4")

message = "Learning Python is fun."

print(message)

print("-" * 50)

# =====================================================
# Example 5
# =====================================================
# Empty string.

print("Example 5")

text = ""

print(text)

print(type(text))

print("-" * 50)

# =====================================================
# Example 6
# =====================================================
# Full name.

print("Example 6")

first_name = "Ali"
last_name = "Khan"

print(first_name)
print(last_name)

print("-" * 50)

# =====================================================
# Example 7
# =====================================================
# Concatenation.

print("Example 7")

first_name = "Ali"
last_name = "Khan"

full_name = first_name + " " + last_name

print(full_name)

print("-" * 50)

# =====================================================
# Example 8
# =====================================================
# Repeating a string.

print("Example 8")

print("Hi! " * 3)

print("-" * 50)

# =====================================================
# Example 9
# =====================================================
# Multi-line string.

print("Example 9")

story = """
Once upon a time,
there was a boy
who loved Python.
"""

print(story)

print("-" * 50)

# =====================================================
# Example 10
# =====================================================
# Store a school name.

print("Example 10")

school = "ABC Public School"

print(school)

print("-" * 50)

# =====================================================
# Example 11
# =====================================================
# Store a country name.

print("Example 11")

country = "Pakistan"

print(country)

print("-" * 50)

# =====================================================
# Example 12
# =====================================================
# Store a favorite food.

print("Example 12")

food = "Pizza"

print(food)

print("-" * 50)

# =====================================================
# Example 13
# =====================================================
# User input always returns a string.

print("Example 13")

username = input("Enter your name: ")

print("Hello,", username)

print(type(username))

print("-" * 50)

# =====================================================
# Example 14
# =====================================================
# Compare two strings.

print("Example 14")

print("Apple" == "Apple")

print("Apple" == "Orange")

print("-" * 50)

# =====================================================
# Example 15
# =====================================================
# String length.

print("Example 15")

word = "Python"

print(len(word))

print("-" * 50)

# =====================================================
# Example 16
# =====================================================
# Strings are immutable.
# (Simple introduction only.)

print("Example 16")

language = "Python"

print(language)

print("Strings cannot be changed directly after creation.")

print("-" * 50)

# =====================================================
# Example 17
# =====================================================
# String with punctuation.

print("Example 17")

sentence = "Hello, World!"

print(sentence)

print("-" * 50)

# =====================================================
# Example 18
# =====================================================
# Store an email.

print("Example 18")

email = "student@example.com"

print(email)

print("-" * 50)

# =====================================================
# Example 19
# =====================================================
# Store a phone number as a string.

print("Example 19")

phone = "03001234567"

print(phone)

print(type(phone))

print("-" * 50)

# =====================================================
# Example 20
# =====================================================
# Real-life example.

print("Example 20")

favorite_book = "Harry Potter"

print("My favorite book is", favorite_book)

print("-" * 50)

# =====================================================
# Summary
# =====================================================

print("Summary")

print("A string is used to store text.")
print("Strings are created using single or double quotes.")
print("A string can contain letters, numbers, spaces, and symbols.")
print("The + operator joins strings together.")
print("The * operator repeats a string.")
print("len() returns the number of characters in a string.")
print("input() always returns a string.")
print("Strings are immutable.")