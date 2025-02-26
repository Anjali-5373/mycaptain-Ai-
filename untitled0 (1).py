
nterms = int(input("How many terms of series you want to print?(positive integer)"))
n1=0
n2=1

count=0

if(nterms<=0):
  print("Invalid Choice: Please enter a positive integer.")
elif(nterms==1):
  print(n1)
else:
  print("The Fiboncci Series:")
  while count < nterms:
    print(n1)
    nth=n1+n2
    n1=n2
    n2=nth
    count+=1

