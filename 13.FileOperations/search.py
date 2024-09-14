def search(word, file_path):
    with open(file_path, "r") as f:
        data = f.read()
        if data.find(word) != -1:
            print("The word '", word, "' is found ", sep="")
        else:
            print("The word '", word, "' is not found ", sep="")


search("learning", "13.FileOperations/practice.txt")
