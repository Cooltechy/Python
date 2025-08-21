# dict key 1 to n and their value as square of their key


def create_square_dict(n):
    return {i: i**2 for i in range(1, n+1)}

if __name__ == "__main__":
    n = int(input("Enter a positive integer: "))
    square_dict = create_square_dict(n)
    print("Dictionary of squares:", square_dict)