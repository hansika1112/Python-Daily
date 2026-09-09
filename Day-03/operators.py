# 🐍 Python Daily - Day 03
# 📚 Topic: Operators
# 👩‍💻 Author: Hansika Gehlot

print("🐍 Python Daily - Day 03")
print("📚 Topic: Operators")
print("-" * 40)

# Taking input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Arithmetic Operators
print("\n🧮 Arithmetic Operators")
print("-" * 40)

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
    print("Floor Division:", num1 // num2)
    print("Modulus:", num1 % num2)
else:
    print("Division is not possible by zero.")
    print("Floor Division is not possible by zero.")
    print("Modulus is not possible by zero.")

print("Power:", num1 ** num2)


# Comparison Operators
print("\n🔍 Comparison Operators")
print("-" * 40)

print("num1 > num2 :", num1 > num2)
print("num1 < num2 :", num1 < num2)
print("num1 >= num2:", num1 >= num2)
print("num1 <= num2:", num1 <= num2)
print("num1 == num2:", num1 == num2)
print("num1 != num2:", num1 != num2)


# Assignment Operators
print("\n📝 Assignment Operators")
print("-" * 40)

score = 10

print("Initial score:", score)

score += 5
print("After += 5:", score)

score -= 2
print("After -= 2:", score)

score *= 2
print("After *= 2:", score)

score /= 2
print("After /= 2:", score)


# Logical Operators
print("\n🧠 Logical Operators")
print("-" * 40)

age = int(input("\nEnter your age: "))

print("Age >= 18 and Age <= 60:", age >= 18 and age <= 60)
print("Age < 18 or Age > 60:", age < 18 or age > 60)
print("Not adult:", not age >= 18)


print("\n✅ Day 03 Completed!")
print("🚀 Keep learning. Keep growing.")
