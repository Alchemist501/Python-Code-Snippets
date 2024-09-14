# Creating class
class Student:
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def avg(self):
        sum = self.mark1 + self.mark2 + self.mark3
        avg = sum / 3
        return avg


s1 = Student("Alysanne", 78, 98, 56)
print("Average of marks is : ", s1.avg())
