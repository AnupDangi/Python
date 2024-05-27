#armstrong refers to the sum of the cube of each digit is equal to the provided number.
num=int(input("Enter a number: "))
rev=num
sum=0
while rev>0:
    digit=rev%10
    sum=sum+digit**3
    rev//=10
if num==sum:
    print("the armstrong number is",num)
else:
    print("Not")