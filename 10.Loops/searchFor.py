squares = []
i = 1
while i <= 10:
    squares.append(i * i)
    i += 1
print("The list of numbers is : ", squares)
num = int(input("Enter a number : "))
for val in squares:
    if val == num:
        print("Number found at index")
else:
    print("Element not found!")
