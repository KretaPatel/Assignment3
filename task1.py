#Factorial:

#defining function to calculate factorial
def fact(val):
    a=1;
    fact=1;
    while(a<=n):         #loop to calculate factorial
        fact=fact*a
        a+=1
    return (fact)

#taking input from user
n=int(input("Enter Number:"))
print("Factorial of",n,"is:",fact(n))



#using recursive function:

def fact(n):
    if n<2:
        return 1
    else:
        return n*(fact(n-1))

n=int(input("Enter Number:"))
res=fact(n)

print("The answer for factorisl is",res)
