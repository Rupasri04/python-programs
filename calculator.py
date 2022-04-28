def addition(num1,num2):
    add=num1+num2
    return add
def subtraction(num1,num2):
    sub=num1-num2
    return sub
def multiply(num1,num2):
    multi=num1*num2
    return multi
def division(num1,num2):
    divi=num1/num2
    return divi
def percentage(n):
    percent=n/100
    return percent
#mainprogram
while True:
    print("enter your choice :\n 1.addition\n 2.subtraction\n 3.multiplication\n 4.division\n 5.Percentage")
    choice=input("enter your choice:")
    if choice in ('1','2','3','4','5'):
        if choice=='1':
            num1=eval(input("enter num1 value:"))
            num2=eval(input("enter num2 value:"))
            print("addition :",addition(num1,num2))
        elif choice=='2':
            num1=eval(input("enter num1 value:"))
            num2=eval(input("enter num2 value:"))
            print("subtraction:",subtraction(num1,num2))
        elif choice=='3':
            num1=eval(input("enter num1 value:"))
            num2=eval(input("enter num2 value:"))
            print("multiplication:",multiply(num1,num2))
        elif choice=='4':
            num1=eval(input("enter num1 value:"))
            num2=eval(input("enter num2 value:"))
            print("division:",division(num1,num2))
        elif choice=='5':
            n=eval(input("enter the n value for calculating percentage:"))
            print("percentage:",percentage(n))
        ask=input("enter yes or no to proceed:")
        if ask=='no':
            break
    else:
        print("ENTER THE VALID CHOICE NUMBER\n")
    
        
        
