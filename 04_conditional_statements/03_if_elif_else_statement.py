"""
Python if...elif...else Statement

Definition:
The if...elif...else statement is used when there are
multiple conditions to check.

Python checks each condition from top to bottom.

✔ If a condition is True, Python executes that block
  and skips the remaining conditions.

✔ If none of the conditions are True,
  the else block is executed.

Syntax:

if condition1:
    # Executes when condition1 is True

elif condition2:
    # Executes when condition2 is True

elif condition3:
    # Executes when condition3 is True

else:
    # Executes when none of the conditions are True
"""

# =====================================================
# Example 1
# =====================================================
# Check exam grades.

print("Example 1")

marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
else:
    print("Keep practicing!")

print("-" * 50)

# =====================================================
# Example 2
# =====================================================
# Check the weather.

print("Example 2")

temperature = 35

if temperature >= 40:
    print("It's extremely hot!")
elif temperature >= 30:
    print("It's a hot day.")
elif temperature >= 20:
    print("The weather is pleasant.")
else:
    print("It's cold today.")

print("-" * 50)

# =====================================================
# Example 3
# =====================================================
# Check traffic lights.

print("Example 3")

traffic_light = "Yellow"

if traffic_light == "Green":
    print("Go")
elif traffic_light == "Yellow":
    print("Slow down")
elif traffic_light == "Red":
    print("Stop")
else:
    print("Traffic light not recognized.")

print("-" * 50)

# =====================================================
# Example 4
# =====================================================
# Choose a drink.

print("Example 4")

drink = "Juice"

if drink == "Tea":
    print("Here is your tea.")
elif drink == "Coffee":
    print("Here is your coffee.")
elif drink == "Juice":
    print("Here is your juice.")
else:
    print("Sorry, we don't have that drink.")

print("-" * 50)

# =====================================================
# Example 5
# =====================================================
# Check age group.

print("Example 5")

age = 12

if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
elif age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

print("-" * 50)

# =====================================================
# Example 6
# =====================================================
# User input example.

print("Example 6")

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

print("-" * 50)

# =====================================================
# Example 7
# =====================================================
# Check the day of the week.

print("Example 7")

day = "Sunday"

if day == "Monday":
    print("Time to go to school!")
elif day == "Friday":
    print("Almost the weekend!")
elif day == "Saturday":
    print("Enjoy your weekend!")
elif day == "Sunday":
    print("Relax and have fun!")
else:
    print("Have a great day!")

print("-" * 50)

# =====================================================
# Example 8
# =====================================================
# Guess the animal.

print("Example 8")

animal = "Cat"

if animal == "Dog":
    print("Dogs are loyal friends.")
elif animal == "Cat":
    print("Cats are playful and cute.")
elif animal == "Rabbit":
    print("Rabbits love carrots.")
else:
    print("That's an interesting animal!")

print("-" * 50)

# =====================================================
# Summary
# =====================================================

print("Summary")

print("✔ if checks the first condition.")
print("✔ elif checks another condition if the previous one is False.")
print("✔ You can have multiple elif blocks.")
print("✔ else runs when none of the conditions are True.")
print("✔ Python stops checking after the first True condition.")