firstNumber = int(input("Enter the first number: "))
secondNumber = int(input("Enter the second number: "))
thirdNumber = int(input("Enter the third number: "))

if firstNumber > secondNumber and firstNumber > thirdNumber:
    print(f"({firstNumber}) is the largest.")
elif secondNumber > firstNumber and secondNumber > thirdNumber:
    print(f"({secondNumber}) is the largest.")
elif thirdNumber > firstNumber and thirdNumber > secondNumber:
    print(f"({thirdNumber}) is the largest.")
else:
    print("There is no single largest number; at least two numbers are equal.")