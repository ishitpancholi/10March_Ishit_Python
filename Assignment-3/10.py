# program to copy the contents of a file to another file

with open("myfile.text","r") as firstfile, open("newfile.txt","a") as secondfile:
    for line in firstfile:



        secondfile.write(line)
