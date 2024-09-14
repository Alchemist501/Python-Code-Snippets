def evenNumbers(n):
    with open("13.FileOperations/evenNumbers.txt", "w") as f:
        for i in range(0, n):
            f.write(str(i))
            f.write(",")
        f.write(str(n))


def count(file_path):
    with open(file_path, "r") as f:
        data = f.read()
        print(data)
        print(type(data))
        count = 0
        Num = data.split(",")
        for i in Num:
            if int(i) % 2 == 0 and i != "0":
                count += 1
                print(i)
        return count


n = int(input("Enter a number : "))
evenNumbers(n)
print(
    "The number of even numbers present in the file is :",
    count("13.FileOperations/evenNumbers.txt"),
)
