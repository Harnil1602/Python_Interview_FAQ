num1= int(input("Enter your num1 value: "))
num2= int(input("Enter your num2 value: "))

print("Numbers before swapping:",num1)
print("Numbers before swapping:",num2)

#temp = num1 # Approach 1
#num1= num2 
#num2= temp

# Approach 2

num1,num2 = num2,num1

print("Numbers after swapping:",num1)
print("Numbers after swapping:",num2)
