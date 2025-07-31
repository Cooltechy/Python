def sum(arr ):
    total = 0
    for num in arr:
        total += num
    return total

def inputArray():
    arr = []
    while True:
        try:
            num = int(input("Enter a number (or type 'done' to finish): "))
            arr.append(num)
        except ValueError:
            break
    return arr

if __name__ == "__main__":
    arr = inputArray()
    if arr:
        total = sum(arr)
        print(f"The sum of the array is: {total}")
    else:
        print("No numbers were entered.")