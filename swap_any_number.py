mylist=[23,45,67,89,90]
print(mylist)

pos1=int(input("Enter the first position you want to change: "))
pos2=int(input("Enter the second position you want to change: "))

mylist[pos1],mylist[pos2]=mylist[pos2],mylist[pos1]

print("List after swapping: ",mylist)