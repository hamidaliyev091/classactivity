# Hamid Aliyev
# 29.09.2026 - Control structures: if-elif-else, for loop, while loop

# 1. Grading system
marks = int(input("Enter your exam marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "F"

print("Your grade is:", grade)

# 2. Multiplication table
number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)

# 3. Password retry system
password = "python123"
attempts = 0

while attempts < 3:
    guess = input("Enter the password: ")

    if guess == password:
        print("Access granted.")
        break

    attempts = attempts + 1
    print("Wrong password. Attempts left:", 3 - attempts)

if attempts == 3:
    print("Too many attempts. Access denied.")
