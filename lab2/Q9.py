number = int(input("Enter a number: "))

if number < 0:
    print("Negative numbers are not supported.")
    exit()

temp = number
reversed_number = 0

while temp > 0:
    digit = temp % 10
    reversed_number = reversed_number * 10 + digit
    temp //= 10


print(f"The reverse of {number}  is: {reversed_number}")