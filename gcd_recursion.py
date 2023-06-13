def gcd(p,q):
    if q==0:
        return p
    else:
        return (gcd(q,p%q))
p= int(input("Enter first number here:"))
q= int(input("Enter second number here:"))
z=gcd(p,q)
print("GCD is:",z)
