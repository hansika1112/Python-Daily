# 🐍 Python Daily - Day 05
# 📚 Topic: Loops
# 👩‍💻 Author: Hansika Gehlot

print("🐍 Python Daily - Day 05")
print("📚 Topic: Loops")
print("-" * 40)

# For Loop
print("\n🔄 For Loop")
print("-" * 40)

for i in range(1, 6):
    print("Number:", i)


# Printing even numbers
print("\n🔢 Even Numbers from 1 to 10")

for i in range(1, 11):
    if i % 2 == 0:
        print(i)


# Printing odd numbers
print("\n🔢 Odd Numbers from 1 to 10")

for i in range(1, 11):
    if i % 2 != 0:
        print(i)


# Sum using for loop
print("\n➕ Sum of Numbers")

total = 0

for i in range(1, 11):
    total += i

print("Sum from 1 to 10:", total)


# Multiplication Table
print("\n✖️ Multiplication Table")

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} × {i} = {number * i}")


# While Loop
print("\n🔁 While Loop")
print("-" * 40)

count = 1

while count <= 5:
    print("Count:", count)
    count += 1


# Break Statement
print("\n🛑 Break Statement")

for i in range(1, 11):
    if i == 6:
        break
    print(i)


# Continue Statement
print("\n⏭️ Continue Statement")

for i in range(1, 11):
    if i == 5:
        continue
    print(i)


print("\n✅ Day 05 Completed!")
print("🚀 Keep learning. Keep growing.")
