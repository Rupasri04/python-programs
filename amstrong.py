num1=eval(input("enter the value of number:"))
copy=num1
rev=0
while(num1!=0):
    remainder=num1%10
    rev=rev+(remainder**3)
    num1=num1//10
if(copy==rev):
    print("amstrong number:",rev)
else:
    print("The entered number is not amstrong")


