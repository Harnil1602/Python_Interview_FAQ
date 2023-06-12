n= int(input("Enter the number of terms:"))
x=0
y=1
sum=0
while(sum<=n):
    print(sum)
    x=y
    y=sum
    sum=x+y

