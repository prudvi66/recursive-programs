# python code for finding factorial of a number using recursive function
def fact(n):
    if(n<=1):
        return 1
    else:
        return (n*fact(n-1))
x=int(input("Enter the number"))
print("the factorial of given number is: " ,fact(x))
