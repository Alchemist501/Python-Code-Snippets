def check(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "ODD"


num = int(input("Enter the number : "))
print(num, "is", check(num))
