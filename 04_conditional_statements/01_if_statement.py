"""
Python if Statement

Definition:
The if statement allows your program to make a decision.

If a condition is True, Python executes the code inside the if block.

If the condition is False, Python skips the code.

Syntax:

if condition:
    # code to execute
"""

# =====================================================
# Example 1
# =====================================================
# If the condition is True,
# the message will be displayed.

print("Example 1")

age = 20

if age >= 18:
    print("You are eligible to vote.")

print("-" * 50)

# =====================================================
# Example 2
# =====================================================
# Here the condition is False,
# so nothing inside the if block will run.

print("Example 2")

temperature = 18

if temperature > 30:
    print("It's a hot day.")

print("The program continued because the condition was False.")

print("-" * 50)

# =====================================================
# Example 3
# =====================================================
# We can also compare strings.

print("Example 3")

favorite_color = "Blue"

if favorite_color == "Blue":
    print("Blue is a beautiful color!")

print("-" * 50)

# =====================================================
# Example 4
# =====================================================
# We can check Boolean values.

print("Example 4")

is_logged_in = True

if is_logged_in:
    print("Welcome back!")

print("-" * 50)

# =====================================================
# Example 5
# =====================================================
# Using user input.

print("Example 5")

name = input("Enter your name: ")

if name == "Manzoor":
    print("Welcome, Manzoor!")

print("-" * 50)

# =====================================================
# Example 6
# =====================================================
# Another real-life example.

print("Example 6")

money = 100

if money >= 50:
    print("You can buy an ice cream.")

print("-" * 50)

# =====================================================
# Example 7
# =====================================================
# Checking exam marks.

print("Example 7")

marks = 95

if marks >= 90:
    print("Excellent work!")

print("-" * 50)

# =====================================================
# Example 8
# =====================================================
# Checking whether a shop is open.

print("Example 8")

shop_open = True

if shop_open:
    print("Let's go shopping!")

print("-" * 50)

# =====================================================
# Summary
# =====================================================

print("Summary")

print("✔ if executes code only when the condition is True.")
print("✔ If the condition is False, Python skips the if block.")
print("✔ The condition must return either True or False.")