"""
Python while Loop

Definition:
A while loop repeats a block of code as long as
a condition is True.

Unlike a for loop, a while loop does not know
how many times it will run.

Syntax:

while condition:
    # code to repeat
"""

# =====================================================
# Example 1
# =====================================================
# Print numbers from 1 to 5.

print("Example 1")

number = 1

while number <= 5:
    print(number)
    number += 1

print("-" * 50)

# =====================================================
# Example 2
# =====================================================
# Countdown.

print("Example 2")

count = 5

while count > 0:
    print(count)
    count -= 1

print("Blast Off! 🚀")

print("-" * 50)

# =====================================================
# Example 3
# =====================================================
# Print even numbers.

print("Example 3")

number = 2

while number <= 10:
    print(number)
    number += 2

print("-" * 50)

# =====================================================
# Example 4
# =====================================================
# Print odd numbers.

print("Example 4")

number = 1

while number <= 10:
    print(number)
    number += 2

print("-" * 50)

# =====================================================
# Example 5
# =====================================================
# Add numbers from 1 to 5.

print("Example 5")

number = 1
total = 0

while number <= 5:
    total += number
    number += 1

print("Total =", total)

print("-" * 50)

# =====================================================
# Example 6
# =====================================================
# User chooses how many times to print a message.

print("Example 6")

times = int(input("How many times should I print 'Hello'? "))

count = 1

while count <= times:
    print("Hello!")
    count += 1

print("-" * 50)

# =====================================================
# Example 7
# =====================================================
# Keep asking until the correct password is entered.

print("Example 7")

password = ""

while password != "python123":
    password = input("Enter password: ")

print("Login successful!")

print("-" * 50)

# =====================================================
# Example 8
# =====================================================
# Fill a water bottle.

print("Example 8")

water_level = 0

while water_level < 5:
    water_level += 1
    print(f"Water Level: {water_level}")

print("Bottle is full!")

print("-" * 50)

# =====================================================
# Infinite Loop
# =====================================================
# Definition:
# An infinite loop happens when the condition
# never becomes False.
#
# Example:
#
# while True:
#     print("This will run forever!")
#
# Be careful! Always make sure your condition
# can eventually become False.

print("Remember:")
print("Always update the variable inside a while loop.")

print("-" * 50)

# =====================================================
# Summary
# =====================================================

print("Summary")

print("✔ while repeats code while a condition is True.")
print("✔ The condition is checked before each iteration.")
print("✔ Update the variable inside the loop.")
print("✔ Otherwise, you may create an infinite loop.")