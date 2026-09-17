# 🐍 Python Daily - Day 06
# 📚 Topic: Strings
# 👩‍💻 Author: Hansika Gehlot

print("🐍 Python Daily - Day 06")
print("📚 Topic: Strings")
print("-" * 40)

# Creating a String
name = "Hansika Gehlot"

print("\n📝 String")
print("Name:", name)

# String Length
print("\n📏 String Length")
print("Length:", len(name))

# String Indexing
print("\n🔢 String Indexing")
print("First character:", name[0])
print("Last character:", name[-1])

# String Slicing
print("\n✂️ String Slicing")
print("First 7 characters:", name[:7])
print("Last 6 characters:", name[8:])
print("Reversed string:", name[::-1])

# String Methods
print("\n🛠️ String Methods")

text = "python programming"

print("Original:", text)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title Case:", text.title())
print("Capitalized:", text.capitalize())

# Replace
print("\n🔄 Replace")
print("After replacement:", text.replace("python", "Python"))

# Find
print("\n🔍 Find")
print("Position of 'programming':", text.find("programming"))

# Count
print("\n🔢 Count")
print("Count of 'p':", text.count("p"))

# Checking String
print("\n✅ String Checking")

word = "Python"

print("Starts with P:", word.startswith("P"))
print("Ends with n:", word.endswith("n"))
print("Is alphabetic:", word.isalpha())
print("Is numeric:", word.isnumeric())

# Taking String Input
print("\n⌨️ String Input")

user_name = input("Enter your name: ")

print("Hello,", user_name)
print("Your name has", len(user_name), "characters.")

# F-String
print("\n🎯 F-String")

age = int(input("Enter your age: "))

print(f"My name is {user_name} and I am {age} years old.")

# String Concatenation
print("\n🔗 String Concatenation")

first_name = "Hansika"
last_name = "Gehlot"

full_name = first_name + " " + last_name

print("Full Name:", full_name)

print("\n✅ Day 06 Completed!")
print("🚀 Keep learning. Keep growing.")
