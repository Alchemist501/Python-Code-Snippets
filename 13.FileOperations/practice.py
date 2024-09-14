import os

os.remove("13.FileOperations/practice.txt")
with open("13.FileOperations/practice.txt", "a") as f:
    f.write("Hi everyone")
    f.write("\nwe are learning File I/O")
    f.write("\nusing Java.")
    f.write("\nI like programming in Java.")
    f.close()
