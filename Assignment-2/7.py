#Program function that takes a list and returns a new list with unique emlements of the first list.

def unique_list(l):
    x = []
    for a in l:
     if a not in x:
         x.append(a)
    return x


print(unique_list([1,1,1,2,2,3,3,3,4,4,4,5,5,6,6,7,7]))        

