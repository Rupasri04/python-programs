num=int(input("enter the number to find factorial of a number:"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("FACTORIAL OF",num,"IS",fact)
