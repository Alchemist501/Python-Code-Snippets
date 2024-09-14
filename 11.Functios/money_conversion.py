def convert_money(amnt):
    INR = 83.57
    return amnt * INR


amnt = float(input("Enter the amount : "))
print(amnt, "$ in INR is : ", convert_money(amnt), "rs")
