# program read first n lines of a file

fl=open("myfile.text","r")

no_of_lines=4

for i in range(no_of_lines):
    line=fl.readline()
    print(line)