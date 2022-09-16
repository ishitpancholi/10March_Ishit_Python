# Program to combine values in python list od dictionary

from collections import Counter

mylist=[{"item": "item1","amount":400},{"item": "item2","amount":300},{"item": "item1","amount":400}]

result=Counter()

for d in mylist:
    result[d["item"]] += d["amount"]
print(result)    