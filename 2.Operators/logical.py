a = 23
b = 56
qn = a>b
print(a,">",b,":",qn)
print("not(",a,">",b,") :",not (qn))
qn2 = a<b
print(a,">",b,":",qn)
print(a,"<",b,":",qn2)
print(a,">",b,"and ",a,"<",b,":",qn and qn2)
print(a,">",b,"or ",a,"<",b,":",qn or qn2)