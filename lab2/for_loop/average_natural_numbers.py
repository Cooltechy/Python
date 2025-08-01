# This program calculates the average of the first n natural numbers using a for loop.

number = int(input("Enter the value of n: "))

total = 0
for i in range(1, number + 1):
    total += i

average = total / number if number > 0 else 0

print(f"The average of first {number} natural numbers is: {average}")