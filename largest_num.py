num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1>num2 and num1>num3:
    print("num1 is large")
elif num2>num1 and num2>num3:
    print("num3 is large")
else:
    print("num3 is large")
