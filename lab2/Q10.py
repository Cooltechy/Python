# Armstrong number using while loop

num = int(input("Enter a number: "))
temp = num
sum_of_powers = 0
n_digits = len(str(num))

while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** n_digits
    temp //= 10

if num == sum_of_powers:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")