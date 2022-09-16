#program to write a list to a file

mylist=["red","blue","green","yellow"]

with open("myfile.text","w") as myfile:
    for c in mylist:
        myfile.write("%s\n" % c)




content=open("myfile.text")
print(content.read())


        
