# sort dict on basis of it's value

def sort_dict_by_value(input_dict):
    return dict(sorted(input_dict.items(), key=lambda item: item[1]))   

if __name__ == "__main__":
    dic = eval(input("Enter dictionary"))
    sorted_dict = sort_dict_by_value(dic)
    print(sorted_dict)