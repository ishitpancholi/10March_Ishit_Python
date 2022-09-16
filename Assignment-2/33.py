# progrsam python function palidrome or not

def palindrome(n):
    return n ==n[::-1]

n=input("Enter the string:-")
ans= palindrome(n)

if ans:
    print("it is palindrome")
else:
    print("It is not palindrome")

