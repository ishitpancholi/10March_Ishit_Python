# program to find the longest word in file

fl=open("myfile.text","r")
f=fl.read()


for i in f:
    if(len(i)):
        print(i)


