def descending(num):
    if num == 0:
        return num
    print(num)
    return descending(num - 1)


num = int(input("Enter the number : "))
print(descending(num))
