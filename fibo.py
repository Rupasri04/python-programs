def fibo(n):
    count=0
    a=0
    b=1
    while(count<=n):
        c=a+b
        print(a)
        a=b
        b=c
        count=count+1
#main program
n=int(input("enter the number:"))
fibo(n)
