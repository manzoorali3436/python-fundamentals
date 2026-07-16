"""
Python Nested Loops

Definition:
A nested loop is a loop inside another loop.

The inner loop runs completely every time
the outer loop runs once.

Syntax:

for variable1 in sequence:

    for variable2 in sequence:
        # code to repeat
"""

# =====================================================
# Example 1
# =====================================================
# Print row and column numbers.

print("Example 1")

for row in range(1, 4):
    for column in range(1, 4):
        print(f"Row {row}, Column {column}")

print("-" * 50)

# =====================================================
# Example 2
# =====================================================
# Print coordinates.

print("Example 2")

for x in range(1, 4):
    for y in range(1, 4):
        print(f"({x}, {y})")

print("-" * 50)

# =====================================================
# Example 3
# =====================================================
# Classroom example.

print("Example 3")

for classroom in range(1, 3):
    print(f"Classroom {classroom}")

    for student in range(1, 4):
        print(f"  Student {student}")

print("-" * 50)

# =====================================================
# Example 4
# =====================================================
# Building floors and rooms.

print("Example 4")

for floor in range(1, 4):
    print(f"Floor {floor}")

    for room in range(1, 4):
        print(f"  Room {room}")

print("-" * 50)

# =====================================================
# Example 5
# =====================================================
# Days and school periods.

print("Example 5")

for day in range(1, 4):
    print(f"Day {day}")

    for period in range(1, 5):
        print(f"  Period {period}")

print("-" * 50)

# =====================================================
# Example 6
# =====================================================
# Multiplication table (1 to 5).

print("Example 6")

for number in range(1, 6):
    print(f"\nTable of {number}")

    for multiply in range(1, 11):
        print(f"{number} x {multiply} = {number * multiply}")

print("-" * 50)

# =====================================================
# Example 7
# =====================================================
# for loop inside a while loop.

print("Example 7")

count = 1

while count <= 3:

    print(f"Round {count}")

    for player in range(1, 4):
        print(f"  Player {player}")

    count += 1

print("-" * 50)

# =====================================================
# Example 8
# =====================================================
# while loop inside a for loop.

print("Example 8")

for round_number in range(1, 4):

    print(f"Round {round_number}")

    score = 1

    while score <= 3:
        print(f"  Score {score}")
        score += 1

print("-" * 50)

# =====================================================
# Summary
# =====================================================

print("Summary")

print("✔ A nested loop is a loop inside another loop.")
print("✔ The inner loop finishes before the outer loop continues.")
print("✔ You can nest for loops.")
print("✔ You can nest while loops.")
print("✔ You can also combine for and while loops.")