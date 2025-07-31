firstNumber = int(input("Enter the first number: "))
secondNumber = int(input("Enter the second number: "))

a = abs(firstNumber)
b = abs(secondNumber)

while b != 0:
    a, b = b, a % b

print(f"The GCD of {firstNumber} and {secondNumber} is {a}")

