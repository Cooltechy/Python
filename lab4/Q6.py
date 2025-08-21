# input tuples and return a new tuple conating elements that's appear twice in original tuple, preserving their order


def find_duplicates(input_tuple):
    element_count = {}
    for elem in input_tuple:
        element_count[elem] = element_count.get(elem, 0) + 1
    return tuple(elem for elem in element_count if element_count[elem] == 2)


if __name__ == "__main__":
    result = find_duplicates((4,5,6,4,7,5,8,5))
    print("Elements appearing twice:", result)

