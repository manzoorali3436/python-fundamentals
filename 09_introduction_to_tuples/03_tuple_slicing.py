"""
Python Tuple Slicing

Definition:
Tuple slicing allows you to extract a portion of a tuple.

Syntax:

tuple[start:stop]

start:
The index where the slice begins.

stop:
The index where the slice ends.
The stop index is NOT included.

You can also use:

tuple[start:stop:step]

step:
Specifies how many items to skip.
"""

# =====================================================
# Example 1
# =====================================================
# Slice from index 0 to 3.

print("Example 1")

fruits = ("Apple", "Banana", "Orange", "Mango", "Grapes")

print(fruits[0:3])

print("-" * 50)

# =====================================================
# Example 2
# =====================================================
# Slice from index 2 to the end.

print("Example 2")

fruits = ("Apple", "Banana", "Orange", "Mango", "Grapes")

print(fruits[2:])

print("-" * 50)

# =====================================================
# Example 3
# =====================================================
# Slice from the beginning to index 4.

print("Example 3")

fruits = ("Apple", "Banana", "Orange", "Mango", "Grapes")

print(fruits[:4])

print("-" * 50)

# =====================================================
# Example 4
# =====================================================
# Copy the entire tuple.

print("Example 4")

fruits = ("Apple", "Banana", "Orange")

print(fruits[:])

print("-" * 50)

# =====================================================
# Example 5
# =====================================================
# Negative slicing.

print("Example 5")

fruits = ("Apple", "Banana", "Orange", "Mango", "Grapes")

print(fruits[-3:])

print("-" * 50)

# =====================================================
# Example 6
# =====================================================
# Remove the first item.

print("Example 6")

numbers = (10, 20, 30, 40, 50)

print(numbers[1:])

print("-" * 50)

# =====================================================
# Example 7
# =====================================================
# Remove the last item.

print("Example 7")

numbers = (10, 20, 30, 40, 50)

print(numbers[:-1])

print("-" * 50)

# =====================================================
# Example 8
# =====================================================
# Every second item.

print("Example 8")

numbers = (10, 20, 30, 40, 50, 60)

print(numbers[::2])

print("-" * 50)

# =====================================================
# Example 9
# =====================================================
# Every third item.

print("Example 9")

numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90)

print(numbers[::3])

print("-" * 50)

# =====================================================
# Example 10
# =====================================================
# Reverse a tuple.

print("Example 10")

numbers = (10, 20, 30, 40, 50)

print(numbers[::-1])

print("-" * 50)

# =====================================================
# Example 11
# =====================================================
# Slice student names.

print("Example 11")

students = ("Ali", "Ahmed", "Sara", "John", "Zara")

print(students[1:4])

print("-" * 50)

# =====================================================
# Example 12
# =====================================================
# Slice colors.

print("Example 12")

colors = ("Red", "Blue", "Green", "Black", "White")

print(colors[:3])

print("-" * 50)

# =====================================================
# Example 13
# =====================================================
# Slice weekdays.

print("Example 13")

days = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
)

print(days[0:5])

print("-" * 50)

# =====================================================
# Example 14
# =====================================================
# Slice using negative indexes.

print("Example 14")

animals = ("Cat", "Dog", "Rabbit", "Horse", "Cow")

print(animals[-4:-1])

print("-" * 50)

# =====================================================
# Example 15
# =====================================================
# User input.

print("Example 15")

first = input("Enter first color: ")
second = input("Enter second color: ")
third = input("Enter third color: ")

colors = (first, second, third)

print(colors[:2])

print("-" * 50)

# =====================================================
# Example 16
# =====================================================
# Store a slice in another variable.

print("Example 16")

languages = ("Python", "PHP", "JavaScript", "C++")

popular = languages[:2]

print(popular)

print("-" * 50)

# =====================================================
# Example 17
# =====================================================
# Skip every second fruit.

print("Example 17")

fruits = (
    "Apple",
    "Banana",
    "Orange",
    "Mango",
    "Grapes",
    "Peach"
)

print(fruits[::2])

print("-" * 50)

# =====================================================
# Example 18
# =====================================================
# Last three items.

print("Example 18")

numbers = (10, 20, 30, 40, 50, 60)

print(numbers[-3:])

print("-" * 50)

# =====================================================
# Example 19
# =====================================================
# Middle items.

print("Example 19")

letters = ("A", "B", "C", "D", "E", "F")

print(letters[2:5])

print("-" * 50)

# =====================================================
# Example 20
# =====================================================
# Review.

print("Example 20")

items = ("Pen", "Book", "Bag", "Bottle", "Pencil")

print("First Three :", items[:3])
print("Last Two    :", items[-2:])
print("Reverse     :", items[::-1])

print("-" * 50)

# =====================================================
# Summary
# =====================================================

print("Summary")

print("tuple[start:stop]")
print("The stop index is NOT included.")
print("[:stop] starts from the beginning.")
print("[start:] goes to the end.")
print("[::step] skips items.")
print("[::-1] reverses a tuple.")
print("Slicing creates a new tuple.")
print("Tuples are immutable.")