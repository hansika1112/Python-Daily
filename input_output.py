# 🐍 Python Daily - Day 02
# 📚 Topic: Input & Output
# 👩‍💻 Author: Hansika Gehlot

print("🐍 Python Daily - Day 02")
print("📚 Topic: Input & Output")
print("-" * 40)

# Output using print()
print("Welcome to my Python learning journey!")
print("Today I am learning Input and Output.")

# Taking string input
name = input("\nEnter your name: ")

# Taking integer input
age = int(input("Enter your age: "))

# Taking float input
height = float(input("Enter your height in cm: "))

# Displaying the entered information
print("\n📋 Your Information")
print("-" * 40)

print("Name:", name)
print("Age:", age)
print("Height:", height, "cm")

# Using f-string
print(f"\nHello {name}! 👋")
print(f"You are {age} years old.")
print(f"Your height is {height} cm.")

# Simple calculation with input
birth_year = 2026 - age

print(f"Your approximate birth year is {birth_year}.")

print("\n✅ Day 02 Completed!")
print("🚀 Keep learning. Keep growing.")
