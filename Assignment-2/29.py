# program to find the highest value in dicionary
from heapq import nlargest
mydict={
    "Ishit": "60",
    "Abhijeet": "40",
    "Aditya": "90"
}
print(nlargest(3,mydict,key=mydict.get))