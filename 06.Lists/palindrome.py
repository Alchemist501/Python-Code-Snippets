data = list(input("Enter the list : "))
print("list you entered is : ",data)
cp = data.copy()
data.reverse()
print("Reverse list : ",data)
if(data==cp):
    print("The list is palindrome")
else:
    print("The list is not a palindrome")