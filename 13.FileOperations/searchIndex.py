def search_lineNo(word, file_path):
    with open(file_path, "r") as f:
        data = f.readlines()
        f.seek(0)
        lines_no = 1
        for i in data:
            words = i.split(" ")
            for i in words:
                i = i.replace(".", "")
                i = i.replace("\n", "")
                if i == word:
                    print("Word '", word, "' found at line ", lines_no)
                    return
            lines_no += 1
        print("Word '", word, "' not found ")
        return


search_lineNo("learning", "13.FileOperations/practice.txt")
