#program to count the number of lines in a text file.


fl=open("myfile.text","r")
counter=0
f=fl.read()

colist=f.split("\n")

for i in colist:
    if i:
        counter +=1
print(counter)        