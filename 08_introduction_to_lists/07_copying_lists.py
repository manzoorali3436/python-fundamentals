"""
Python Copying Lists

Definition:
There are different ways to copy a list.

Some ways create another reference to the same list.

Other ways create a completely new list.

Common methods:

1. Assignment (=)
2. copy()
3. Slicing [:]
4. list()
"""

# =====================================================
# Example 1
# =====================================================
# Assignment (=)

print("Example 1")

fruits = ["Apple", "Banana", "Orange"]

new_fruits = fruits

print(fruits)
print(new_fruits)

print("-" * 50)

# =====================================================
# Example 2
# =====================================================
# Assignment shares the same list.

print("Example 2")

fruits = ["Apple", "Banana", "Orange"]

new_fruits = fruits

new_fruits.append("Mango")

print("Original:", fruits)
print("New     :", new_fruits)

print("-" * 50)

# =====================================================
# Example 3
# =====================================================
# copy()

print("Example 3")

fruits = ["Apple", "Banana", "Orange"]

new_fruits = fruits.copy()

print(fruits)
print(new_fruits)

print("-" * 50)

# =====================================================
# Example 4
# =====================================================
# copy() creates a new list.

print("Example 4")

fruits = ["Apple", "Banana", "Orange"]

new_fruits = fruits.copy()

new_fruits.append("Mango")

print("Original:", fruits)
print("New     :", new_fruits)

print("-" * 50)

# =====================================================
# Example 5
# =====================================================
# Slicing [:]

print("Example 5")

numbers = [10, 20, 30]

new_numbers = numbers[:]

print(numbers)
print(new_numbers)

print("-" * 50)

# =====================================================
# Example 6
# =====================================================
# Modify copied list.

print("Example 6")

numbers = [10, 20, 30]

new_numbers = numbers[:]

new_numbers.append(40)

print("Original:", numbers)
print("New     :", new_numbers)

print("-" * 50)

# =====================================================
# Example 7
# =====================================================
# list()

print("Example 7")

colors = ["Red", "Blue", "Green"]

new_colors = list(colors)

print(colors)
print(new_colors)

print("-" * 50)

# =====================================================
# Example 8
# =====================================================
# list() creates a new list.

print("Example 8")

colors = ["Red", "Blue", "Green"]

new_colors = list(colors)

new_colors.remove("Blue")

print("Original:", colors)
print("New     :", new_colors)

print("-" * 50)

# =====================================================
# Example 9
# =====================================================
# Compare assignment and copy.

print("Example 9")

list1 = [1, 2, 3]

list2 = list1
list3 = list1.copy()

list2.append(4)
list3.append(5)

print("list1:", list1)
print("list2:", list2)
print("list3:", list3)

print("-" * 50)

# =====================================================
# Example 10
# =====================================================
# Compare assignment and slicing.

print("Example 10")

letters = ["A", "B", "C"]

copy_letters = letters[:]

copy_letters.append("D")

print("Original:", letters)
print("Copy    :", copy_letters)

print("-" * 50)

# =====================================================
# Example 11
# =====================================================
# Changing an item.

print("Example 11")

fruits = ["Apple", "Banana"]

new_fruits = fruits.copy()

new_fruits[0] = "Mango"

print("Original:", fruits)
print("Copy    :", new_fruits)

print("-" * 50)

# =====================================================
# Example 12
# =====================================================
# Removing an item.

print("Example 12")

numbers = [10, 20, 30]

new_numbers = numbers.copy()

new_numbers.remove(20)

print("Original:", numbers)
print("Copy    :", new_numbers)

print("-" * 50)

# =====================================================
# Example 13
# =====================================================
# IDs with assignment.

print("Example 13")

list1 = [1, 2, 3]
list2 = list1

print(id(list1))
print(id(list2))

print("-" * 50)

# =====================================================
# Example 14
# =====================================================
# IDs with copy().

print("Example 14")

list1 = [1, 2, 3]
list2 = list1.copy()

print(id(list1))
print(id(list2))

print("-" * 50)

# =====================================================
# Example 15
# =====================================================
# IDs with slicing.

print("Example 15")

list1 = [1, 2, 3]
list2 = list1[:]

print(id(list1))
print(id(list2))

print("-" * 50)

# =====================================================
# Example 16
# =====================================================
# IDs with list().

print("Example 16")

list1 = [1, 2, 3]
list2 = list(list1)

print(id(list1))
print(id(list2))

print("-" * 50)

# =====================================================
# Example 17
# =====================================================
# Shopping list.

print("Example 17")

shopping = ["Milk", "Bread"]

today = shopping.copy()

today.append("Eggs")

print("Shopping:", shopping)
print("Today   :", today)

print("-" * 50)

# =====================================================
# Example 18
# =====================================================
# Student names.

print("Example 18")

students = ["Ali", "Sara"]

backup = students[:]

backup.append("Ahmed")

print(students)
print(backup)

print("-" * 50)

# =====================================================
# Example 19
# =====================================================
# Favorite colors.

print("Example 19")

colors = ["Blue", "Black"]

new_colors = list(colors)

new_colors.append("White")

print(colors)
print(new_colors)

print("-" * 50)

# =====================================================
# Example 20
# =====================================================
# Review.

print("Example 20")

items = ["Pen", "Book"]

copy_items = items.copy()

copy_items.append("Bag")

print("Original:", items)
print("Copy    :", copy_items)

print("-" * 50)

# =====================================================
# Summary
# =====================================================

print("Summary")

print("= creates another reference to the same list.")
print("copy() creates a new list.")
print("[:] creates a new list.")
print("list() creates a new list.")
print("Changing a copied list does not change the original.")
print("id() shows whether two variables reference the same object.")