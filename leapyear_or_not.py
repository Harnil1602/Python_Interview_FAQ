n=int(input("Enter your number here:"))
if (n%400==0):
    print("It's a leap year")
elif (n%4==0 and n%100!=0):
    print("It's a leap year")
else:
    print("It's not a leap year")