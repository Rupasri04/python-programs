evensum=0
oddsum=0
n=int(input("enter the series n :"))
for i in range(n+1):
    if(i%2==0):
        evensum=evensum+i
    else:
        oddsum=oddsum+i
print("EVEN SUM:",evensum)
print("ODD SUM:",oddsum)
