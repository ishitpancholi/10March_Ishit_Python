#count number of string

a=0
list1=['aba','121','kgf','abc']
for x in list1:
    if len(x)>1 and x[0]==x[-1]:
        print(x)
        a=a+1
print(a)