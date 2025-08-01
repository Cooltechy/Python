# This program calculates the sum of the series: 1/2 + 2/3 + 3/4 + ... + n/(n+1).

def sum_series(n):
    total = 0.0
    for i in range(1, n + 1):
        total += i / (i + 1)
    return total

if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    result = sum_series(n)
    print(f"Sum of the series up to {n}/({n+1}) is: {result}")