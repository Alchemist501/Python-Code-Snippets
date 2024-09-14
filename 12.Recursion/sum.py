def sum(num):
    if num == 0:
        return num
    return num + sum(num - 1)


num = int(input("Enter the number : "))
print("The sum of numbers from 0 to ", num, "is", sum(num))
