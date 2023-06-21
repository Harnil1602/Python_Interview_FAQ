n=int(input("Enter your number here:"))
count=0

if n>1:  
    for i in range (1,n+1):
        if (n%i)==0:
            count=count+1
    if count == 2:
        print("Number is a prime number")     
    else:
        print("Number is not a prime number")
