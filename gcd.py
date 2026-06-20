'''Find the GCD of Given Two Numbers'''
def GCD(n,m):
    if n==0:
        return m
    elif m==0:
        return n
    else:
        return GCD(m,n%m)
    
num1=int(input("Enter 1st Numbers: "))
num2=int(input("Enter 2nd Number: "))
print(GCD(num1,num2))