# python fuction to check weather a number in a given range

def perfect(n):
    sum=0
    for n in range(1,n):
        if n % n ==0:
            sum+=n
    return sum==n        

print(perfect(10))


        