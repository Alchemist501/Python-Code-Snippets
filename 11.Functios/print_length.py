def input_list():
    List = list(input("Enter the list : "))
    print("The list is : ", List)
    return List


def print_length(List):
    length = len(List)
    print(length)
    return length


List = input_list()
print("The length of list is : ", print_length(List))
