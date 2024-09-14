marks = int(input("Enter your mark under 100: "))
if(marks<=100 and marks>=0):
    if(marks>=90):
        print("Grade is A")
    elif(marks>=80):
        print("Grade is B")
    elif(marks>=70):
        print("Grade is C")
    elif(marks>=60):
        print("Grade is D")
    else:
        print("Try next time")
else:
    print("Marks should be less than or equal to 100")