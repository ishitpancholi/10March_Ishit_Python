# program read last n lines of a file

fl=open("myfile.text","r")

no_of_lines=6

for i in range(no_of_lines):
    lastline=fl.readline()
    print(lastline)