# Program function that two list and retur true if they have 
# one common member

def com_data(list1 , list2):
    result = False

    #traversing in first list
    for x in list1:
        #traversing in list2
        for y in list2:

            #if one common
            if x == y:
                result = True
                return result
        return result

#take list as user input
a = [x for x in input("Enter list 1:").split()]
b = [x for x in input("Enter list 2:").split()]

print(com_data(a,b))