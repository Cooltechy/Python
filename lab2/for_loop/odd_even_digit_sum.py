# This program takes a number as input and calculates the sum of digits at even and odd places (from the left).

number = input("Enter a number: ")
if not number.isdigit():
    print("Please enter a valid positive integer.")
    exit()

    
odd_sum = 0
even_sum = 0

for idx, digit in enumerate(number):
    if (idx ) % 2 == 0:  
        odd_sum += int(digit)
    else:
        even_sum += int(digit)

print("Sum of digits at even places:", even_sum)
print("Sum of digits at odd places:", odd_sum)