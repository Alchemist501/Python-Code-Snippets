def fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact = i * fact
    return fact


num = int(input("Enter the number : "))
print(num, "!", " = ", fact(num), sep="")
