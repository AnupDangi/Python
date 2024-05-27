#finding palindrome number
num=int(input("Enter a number:"))
temp=num
rev=0
for i in range(0,len(str(num))):
    digit=num%10
    rev=rev*10+digit
    num=num//10
if(temp==rev):
    print("The number is a palindrome")
else:
    print("It is not a palindrome")
    