n=int(input("Enter number of terms to find sd:"))
list=[]
for i in range(n):
    list.append(int(input("Enter all the terms in:")))
mean=sum(list)/n
var=0
for i in list:
    var+=(i-mean)**2
var=var/n
sd=var**0.5
print("The standard deviation is",sd)