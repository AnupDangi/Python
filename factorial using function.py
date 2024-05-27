#to find factorial of a number using function
def fact_num(num):
    if num<=0:
        return 1
    else:
        return num*fact_num(num-1)
num=int(input("Enter a number:"))
print(fact_num(num))
