#program to read two list of color. Print out all colors from list1 that are not in list 2.

def unique_colors(list1, list2):
    return [color for color in list1 if color not in list2] 

if __name__ == "__main__":
    # Input for first list of colors
    print("Enter colors for first list (enter 'done' when finished):")
    list1 = []
    while True:
        color = input("Color: ").strip()
        if color.lower() == 'done':
            break
        if color:  # Only add non-empty strings
            list1.append(color)
    
    # Input for second list of colors
    print("Enter colors for second list (enter 'done' when finished):")
    list2 = []
    while True:
        color = input("Color: ").strip()
        if color.lower() == 'done':
            break
        if color:  # Only add non-empty strings
            list2.append(color)

    print("Unique colors from first list:", unique_colors(list1, list2))

