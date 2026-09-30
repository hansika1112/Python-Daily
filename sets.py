# 🐍 Python Daily - Day 09
# 📚 Topic: Sets
# 👩‍💻 Author: Hansika Gehlot

print("🐍 Python Daily - Day 09")
print("📚 Topic: Sets")
print("-" * 40)

# Creating a Set
print("\n📦 Creating a Set")

fruits = {"Apple", "Banana", "Mango", "Orange"}

print("Fruits:", fruits)

# Sets do not allow duplicate values
print("\n🚫 Duplicate Values")

numbers = {10, 20, 30, 20, 10, 40}

print("Set:", numbers)

# Adding Elements
print("\n➕ Adding Elements")

fruits.add("Grapes")
print("After add:", fruits)

# Adding Multiple Elements
fruits.update(["Pineapple", "Watermelon"])

print("After update:", fruits)

# Removing Elements
print("\n➖ Removing Elements")

fruits.remove("Banana")
print("After remove:", fruits)

fruits.discard("Mango")
print("After discard:", fruits)

# Set Length
print("\n📏 Set Length")

print("Number of fruits:", len(fruits))

# Membership Checking
print("\n🔍 Membership Checking")

if "Apple" in fruits:
    print("Apple is present in the set.")
else:
    print("Apple is not present in the set.")

# Set Union
print("\n🔗 Set Union")

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print("Set A:", set_a)
print("Set B:", set_b)

print("Union:", set_a.union(set_b))

# Set Intersection
print("\n🎯 Set Intersection")

print("Intersection:", set_a.intersection(set_b))

# Set Difference
print("\n➖ Set Difference")

print("A - B:", set_a.difference(set_b))
print("B - A:", set_b.difference(set_a))

# Symmetric Difference
print("\n🔄 Symmetric Difference")

print("Symmetric Difference:", set_a.symmetric_difference(set_b))

# Subset and Superset
print("\n📊 Subset and Superset")

small_set = {1, 2, 3}
large_set = {1, 2, 3, 4, 5}

print("Small set:", small_set)
print("Large set:", large_set)

print("Small set is subset:", small_set.issubset(large_set))
print("Large set is superset:", large_set.issuperset(small_set))

# Looping Through a Set
print("\n🔁 Looping Through Set")

for fruit in fruits:
    print("Fruit:", fruit)

# Converting List to Set
print("\n🔄 List to Set")

marks = [80, 90, 80, 75, 90, 85]

print("Original list:", marks)

unique_marks = set(marks)

print("Unique marks:", unique_marks)

print("\n✅ Day 09 Completed!")
print("🚀 Keep learning. Keep growing.")
