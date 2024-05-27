#finding the frequency of a number
digit=input("Enter a multi digit number:")
for i in set (digit):
    freq=0
for j in digit:
  if i==j:
      freq=freq+1
  print("The frequency of a number is",j,"is",freq )
  
