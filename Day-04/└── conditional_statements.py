# 🐍 Python Daily - Day 04
# 📚 Topic: Conditional Statements
# 👩‍💻 Author: Hansika Gehlot

print("🐍 Python Daily - Day 04")
print("📚 Topic: Conditional Statements")
print("-" * 40)

# Taking input
age = int(input("Enter your age: "))

# if statement
if age >= 18:
    print("You are eligible to vote.")
    
# if-else statement
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# if-elif-else statement
if age < 13:
    print("Category: Child")
elif age < 18:
    print("Category: Teenager")
elif age < 60:
    print("Category: Adult")
else:
    print("Category: Senior Citizen")


# Checking positive, negative or zero
number = float(input("\nEnter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# Checking even or odd
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# Nested if
marks = float(input("\nEnter your marks: "))

if marks >= 0 and marks <= 100:
    if marks >= 40:
        print("Result: Pass")
        
        if marks >= 90:
            print("Grade: A+")
        elif marks >= 80:
            print("Grade: A")
        elif marks >= 70:
            print("Grade: B")
        elif marks >= 60:
            print("Grade: C")
        else:
            print("Grade: D")
    else:
        print("Result: Fail")
else:
    print("Invalid marks! Enter marks between 0 and 100.")


print("\n✅ Day 04 Completed!")
print("🚀 Keep learning. Keep growing.")
