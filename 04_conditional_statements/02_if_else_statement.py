"""
Python if...else Statement

Definition:
The if...else statement allows your program to choose between
two different actions.

If the condition is True, Python executes the code inside the if block.

If the condition is False, Python executes the code inside the else block.

Syntax:

if condition:
    # Executes when the condition is True
else:
    # Executes when the condition is False
"""

# =====================================================
# Example 1
# =====================================================
# Check whether a person is an adult.

print("Example 1")

age = 20

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

print("-" * 50)

# =====================================================
# Example 2
# =====================================================
# Check whether a number is positive.

print("Example 2")

number = 15

if number > 0:
    print("The number is positive.")
else:
    print("The number is not positive.")

print("-" * 50)

# =====================================================
# Example 3
# =====================================================
# Check if someone has enough money to buy a toy.

print("Example 3")

money = 25

if money >= 50:
    print("You can buy the toy.")
else:
    print("You need more money.")

print("-" * 50)

# =====================================================
# Example 4
# =====================================================
# Check if a shop is open.

print("Example 4")

shop_open = False

if shop_open:
    print("Welcome! The shop is open.")
else:
    print("Sorry, the shop is closed.")

print("-" * 50)

# =====================================================
# Example 5
# =====================================================
# Check if the entered password is correct.

print("Example 5")

password = input("Enter the password: ")

if password == "python123":
    print("Login successful!")
else:
    print("Incorrect password.")

print("-" * 50)

# =====================================================
# Example 6
# =====================================================
# Check whether it is raining.

print("Example 6")

is_raining = True

if is_raining:
    print("Take an umbrella.")
else:
    print("Enjoy the sunshine!")

print("-" * 50)

# =====================================================
# Example 7
# =====================================================
# Check exam result.

print("Example 7")

marks = 85

if marks >= 50:
    print("Congratulations! You passed.")
else:
    print("Don't give up. Try again!")

print("-" * 50)

# =====================================================
# Example 8
# =====================================================
# Check whether someone can ride a bicycle.

print("Example 8")

knows_cycling = True

if knows_cycling:
    print("Enjoy your ride!")
else:
    print("Practice first, then ride safely.")

print("-" * 50)

# =====================================================
# Summary
# =====================================================

print("Summary")

print("✔ if runs when the condition is True.")
print("✔ else runs when the condition is False.")
print("✔ Only one block (if or else) is executed.")