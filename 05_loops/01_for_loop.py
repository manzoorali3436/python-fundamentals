"""
Python for Loop

Definition:
A for loop is used to repeat a block of code a specific
number of times or to go through each item in a sequence.

Think of it like this:

"If you have 5 candies and want to check each one,
a for loop lets you look at them one by one."

Syntax:

for variable in sequence:
    # code to repeat
"""

# =====================================================
# Example 1
# =====================================================
# Print numbers from 1 to 5.

print("Example 1")

for number in range(1, 6):
    print(number)

print("-" * 50)

# =====================================================
# Example 2
# =====================================================
# Print a message five times.

print("Example 2")

for count in range(5):
    print("Hello, Python!")

print("-" * 50)

# =====================================================
# Example 3
# =====================================================
# Count from 1 to 10.

print("Example 3")

for number in range(1, 11):
    print(number)

print("-" * 50)

# =====================================================
# Example 4
# =====================================================
# Print only even numbers.

print("Example 4")

for number in range(2, 11, 2):
    print(number)

print("-" * 50)

# =====================================================
# Example 5
# =====================================================
# Print only odd numbers.

print("Example 5")

for number in range(1, 11, 2):
    print(number)

print("-" * 50)

# =====================================================
# Example 6
# =====================================================
# Countdown.

print("Example 6")

for number in range(5, 0, -1):
    print(number)

print("Blast Off! 🚀")

print("-" * 50)

# =====================================================
# Example 7
# =====================================================
# Calculate the total.

print("Example 7")

total = 0

for number in range(1, 6):
    total += number

print("Total =", total)

print("-" * 50)

# =====================================================
# Example 8
# =====================================================
# User chooses how many times to print a message.

print("Example 8")

times = int(input("How many times should I print 'Welcome'? "))

for number in range(times):
    print("Welcome!")

print("-" * 50)

# =====================================================
# Understanding range()
# =====================================================
# Definition:
# range() generates a sequence of numbers.
#
# Syntax:
# range(start, stop, step)
#
# start -> Starting number (included)
# stop  -> Ending number (not included)
# step  -> Increase or decrease value

print("range(5)")

for number in range(5):
    print(number)

print("-" * 50)

print("range(1, 6)")

for number in range(1, 6):
    print(number)

print("-" * 50)

print("range(2, 11, 2)")

for number in range(2, 11, 2):
    print(number)

print("-" * 50)

# =====================================================
# Summary
# =====================================================

print("Summary")

print("✔ for loops repeat code.")
print("✔ range() creates a sequence of numbers.")
print("✔ start is included.")
print("✔ stop is NOT included.")
print("✔ step controls how much the number changes.")