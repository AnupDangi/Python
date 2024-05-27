#finding binomial coefficient of a number
def fact(num):
    if num<=0:
        return 1
    else:
        return(num*fact(num-1))
n=int(input("Enter the value of n:"))
r=int(input("Enter a value of r:"))
if n>=r:
    ncr=fact(n)/(fact(n-r)*fact(r))
    print("The value is ",ncr)
else:
    print("The value cannot be found")