# 🐍 Python Daily - Day 07
# 📚 Topic: Lists
# 👩‍💻 Author: Hansika Gehlot

print("🐍 Python Daily - Day 07")
print("📚 Topic: Lists")
print("-" * 40)

# Creating a List
print("\n📋 Creating a List")

fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Fruits:", fruits)

# Accessing List Elements
print("\n🔢 Accessing List Elements")

print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])
print("Last fruit:", fruits[-1])

# List Slicing
print("\n✂️ List Slicing")

print("First two fruits:", fruits[:2])
print("Last two fruits:", fruits[-2:])

# Changing List Elements
print("\n🔄 Changing List Elements")

fruits[1] = "Grapes"

print("Updated list:", fruits)

# Adding Elements
print("\n➕ Adding Elements")

fruits.append("Watermelon")
print("After append:", fruits)

fruits.insert(1, "Pineapple")
print("After insert:", fruits)

# Removing Elements
print("\n➖ Removing Elements")

fruits.remove("Orange")
print("After remove:", fruits)

removed_fruit = fruits.pop()
print("Removed fruit:", removed_fruit)
print("After pop:", fruits)

# List Length
print("\n📏 List Length")

print("Number of fruits:", len(fruits))

# Sorting a List
print("\n🔤 Sorting List")

numbers = [45, 12, 78, 23, 9, 56]

print("Original numbers:", numbers)

numbers.sort()
print("Ascending order:", numbers)

numbers.sort(reverse=True)
print("Descending order:", numbers)

# Searching in a List
print("\n🔍 Searching in List")

if 23 in numbers:
    print("23 is present in the list.")
else:
    print("23 is not present in the list.")

# Looping through a List
print("\n🔁 Looping Through List")

for fruit in fruits:
    print("Fruit:", fruit)

# List with User Input
print("\n⌨️ User Input")

names = []

for i in range(3):
    name = input(f"Enter name {i + 1}: ")
    names.append(name)

print("\nNames entered:", names)

# Finding Maximum and Minimum
print("\n📊 Maximum and Minimum")

marks = [85, 72, 91, 68, 95]

print("Marks:", marks)
print("Highest marks:", max(marks))
print("Lowest marks:", min(marks))
print("Total marks:", sum(marks))

print("\n✅ Day 07 Completed!")
print("🚀 Keep learning. Keep growing.")
