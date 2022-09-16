# Program to remove an empty tuple from list of tuple

mylist=[(),(),(''),("a","b","c"),("a","b","c"),("d")]

mylist=[t for t in mylist if t]

print (mylist)



