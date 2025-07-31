def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence
def main():
    num = int(input("Enter the number of Fibonacci terms to generate: "))
    if num < 0:
        print("Please enter a non-negative integer.")
        return
    fib_sequence = fibonacci(num)
    print(f"The first {num} terms of the Fibonacci sequence are: {fib_sequence}")

if __name__ == "__main__":
    main()