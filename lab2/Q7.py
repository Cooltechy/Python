number = int(input("Enter a integer: "))

if number < 0:
    print("-1" , end=' ')
    number *= -1

i = 1;

while i <= number:  
    if number % i == 0:
        print(i, end=' ')
    i += 1
