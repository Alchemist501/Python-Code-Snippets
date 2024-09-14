def print_ele(List, index=0):
    if index == len(List):
        return
    print(List[index])
    return print_ele(List, index + 1)


List = list(input("Enter the list : "))
print_ele(List)
