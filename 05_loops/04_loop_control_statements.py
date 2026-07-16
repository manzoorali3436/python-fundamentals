"""
Python Loop Control Statements

Definition:
Loop control statements allow you to change the normal
flow of a loop.

Python provides three loop control statements:

1. break
2. continue
3. pass
"""

# =====================================================
# break Statement
# =====================================================
# Definition:
# The break statement immediately stops the loop,
# even if there are more iterations remaining.

print("Example 1 - break")

for number in range(1, 11):

    if number == 6:
        break

    print(number)

print("Loop stopped.")

print("-" * 50)

# =====================================================
# break with User Input
# =====================================================
# Keep asking until the correct password is entered.

print("Example 2 - break")

while True:

    password = input("Enter password: ")

    if password == "python123":
        print("Login successful!")
        break

    print("Incorrect password. Try again.")

print("-" * 50)

# =====================================================
# continue Statement
# =====================================================
# Definition:
# The continue statement skips the current iteration
# and moves to the next iteration of the loop.

print("Example 3 - continue")

for number in range(1, 6):

    if number == 3:
        continue

    print(number)

print("-" * 50)

# =====================================================
# continue Example
# =====================================================
# Skip even numbers.

print("Example 4 - continue")

for number in range(1, 11):

    if number % 2 == 0:
        continue

    print(number)

print("-" * 50)

# =====================================================
# pass Statement
# =====================================================
# Definition:
# The pass statement does nothing.
#
# It is used as a placeholder when code will be
# added later.

print("Example 5 - pass")

for number in range(1, 6):

    if number == 3:
        pass

    print(number)

print("-" * 50)

# =====================================================
# pass Example
# =====================================================
# Placeholder for future code.

print("Example 6 - pass")

age = 20

if age >= 18:
    pass

print("Program continues normally.")

print("-" * 50)

# =====================================================
# Comparison
# =====================================================

print("Example 7")

print("break")
for number in range(1, 6):

    if number == 3:
        break

    print(number)

print("-" * 20)

print("continue")
for number in range(1, 6):

    if number == 3:
        continue

    print(number)

print("-" * 20)

print("pass")
for number in range(1, 6):

    if number == 3:
        pass

    print(number)

print("-" * 50)

# =====================================================
# Summary
# =====================================================

print("Summary")

print("✔ break    -> Stops the loop immediately.")
print("✔ continue -> Skips the current iteration.")
print("✔ pass     -> Does nothing (placeholder).")