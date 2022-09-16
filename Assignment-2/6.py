#Python program to generate and print a list except fotr the first 5 element
#square of number between 1to30

def printValues():
    l = list()
    for i in range(1,31):
        l.append(i**2)
        print(l[5:])
printValues()
        
