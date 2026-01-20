a=int(input("enter the no"))
b=int(input("enter the no"))
c=int(input("enter the no"))
if a>b and a>c:
    large =a
elif b>c:
    large=b
else:
    large=c
print (large)