#program to count the frequency of words in a file.
from collections import Counter
from posixpath import split

fl=open("myfile.text")
fl=fl.read()
print(Counter(fl))
