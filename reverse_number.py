i= int(input("enter your number:"))
rev=0
while(i>0):
    rev=(rev*10) + (i%10)
    i=i//10
print("Your reverse number is: ",rev)