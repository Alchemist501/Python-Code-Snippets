def replace(old, new, file_path):
    with open(file_path, "r+") as f:
        data = f.read()
        print("Data before replacing \n-------------------- ", data)
        f.seek(0)
        f.write(data.replace(old, new))
        f.seek(0)
        dat = f.read()
        print("\nData after replacing \n---------------------", dat)


replace("Java", "Python", "13.FileOperations/practice.txt")
