num1=int(input("enter the number :"))
temp=num1
rev=0
while(num1>0):
    remainder=num1%10
    rev=(rev*10)+remainder
    num1=num1//10
if(rev==temp):
    print("THE ENTERED INTEGER IS PALINDROME")
else:
    print("THE ENTERED NUMBER IS NOT PALINDROME")
