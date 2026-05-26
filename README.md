### Python Beginner Programs – Basics & Conditions
### Repository Structure

This repository contains beginner-friendly Python programs organized topic-wise for easy learning and practice.

These programs help in understanding:
- Python syntax
- Variables and data types
- Input and output
- Conditional statements
- Basic mathematical formulas
- Problem-solving skills

---

### Topics Covered

Basics
↓
Conditions
↓
Loops
↓
Patterns
↓
Strings
↓
Lists
↓
Functions

### Basics

The Basics section introduces fundamental Python concepts such as printing output, taking user input, performing calculations, and using formulas.

### Programs Included
# 1.Hello World

print("hello,world!)


# 2.Simple calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
if num2!=0:
    print("Division:",num1/num2)
else:
    print("Division cannot performed")
    

# 3.Swap two numbers
# i) Swap without using temporary variable

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a=a+b
b=a-b
a=a-b
print("After swapping:")
print("a =", a)
print("b =", b)


# ii)Swap using temporary variable

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
temp=a
a=b
b=temp
print("After swapping:")
print("a =", a)
print("b =", b)


# 4.Find Square and Cube of a number

num = int(input("Enter a number: "))

print("Square:", num ** 2)
print("Cube:", num ** 3)


# 5.Convert Celcius to Fahrenheit

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print("Fahrenheit:", fahrenheit)


# 6.Find Area of Circle

radius = float(input("Enter radius: "))
area = 3.14 * radius * radius

print("Area:", area)

# 7.Find Simple intrest

p=int(input("enter p value:"))
t=int(input("enter t value:"))
r=int(input("enter r value:"))
SI=p*t*r
print("simple intrest is:",SI)


### Conditional Statements

The Conditions section helps in understanding decision-making using:
-if
-if-else
-elif ladder
-nested if

### Programs Included

# 1. Even or Odd Number  

num = int(input("Enter a number:"))

if num % 2 == 0:
    print("number is Even")
else:
    print("number is Odd")

    
# 2. Positive or Negative Number  

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

    
# 3. Largest of 3 Numbers  

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1>num2 and num1>num3:
    print("num1 is large")
elif num2>num1 and num2>num3:
    print("num3 is large")
else:
    print("num3 is large")


# 4. Leap Year Checker

year = int(input("Enter year: "))

if (year % 4 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

    
# 5. Grade Calculator 

marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

    
# 6. Voting Eligibility Checker  

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")


### Loops
    


### How to Run the Programs

# Step 1: Install Python

Download Python:
https://www.python.org/downloads/

# Step 2: Run Program

Open terminal or command prompt:

python filename.py
