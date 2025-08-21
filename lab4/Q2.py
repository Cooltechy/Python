#list of integers after removing even numbers

list_of_integers = input("Enter a list of integers separated by commas: ").split(",")
list_of_integers = [i for i in list_of_integers if int(i) % 2 != 0]
print("List after removing even numbers:", list_of_integers)    
