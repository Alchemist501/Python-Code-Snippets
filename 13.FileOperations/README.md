# FILE I/O IN PYTHON

### Python can be used to perform operations on a file.

### Read and write data

## Types of all files

1. Text Files => .txt , .docx , .log etc
2. Binary Files => .mp4 , .mov , .png , .jpeg etc

## Open, read and close a file

To open => ` f = open("file_name","mode")` <br>
sample.txt == filename
mode can be read or write.

To read data => ` data = f.read()`<br>
To read data line by line => `data = f.readline()`<br>
To close the file => ` f.close()`

## Writing to a file

    f = open("sample.txt","w")
    f.write("New line") # overwrites everything

    f = open("sample.txt","a")
    f.write("This is a new line.") #adds to the file

## with sytax

    with open("sample.txt","r") as f:
        data = f.read()

## Deleting a File

using the os module
Module (like a code library) is a file written by another programmer that generally has a functions we can use.

    import os
    os.remove(file_name)
