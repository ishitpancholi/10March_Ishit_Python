#Write a Python program to get the Fibonacci series of given range



n=int(input("Enter a number"))
a=0
b=1
c=0 

for x in range(n):
    print(c,end=" ")
    c=a+b
    b=a
    a=c