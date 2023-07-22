num1=int(input("enter the number to find whether it is prime or not:"))
for i in range(2,num1//2):
    if(num1%i==0):
        print("THE ENTERED NUMBER IS NOT A PRIME NUMBER")
        break
    else:
        print("THE ENTERED NUMBER IS  A PRIME NUMBER")
        break
