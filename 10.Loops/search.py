i = 1
flag = 0
squares = []
while i <= 10:
    squares.append(i * i)
    i += 1
Sq = tuple(squares)
num = int(input("Enter the number : "))
i = 0
while i < 10:
    if num == squares[i]:
        print("Number found!!! at index", i)
        flag = 1
        break
    else:
        print("Searching in progress!")
    i += 1
if flag == 0:
    print("Number is not present in the list")
