n = int(input("Enter a positive integer: "))
if n <= 0:
    print("Please enter a positive integer.")
    exit()  

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i*j, end=' ') 
    print()


