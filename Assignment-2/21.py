# program to replace last value of tuple in a list

from dataclasses import replace


mytech=[(10,20,30),(50,60,90),(100,200,200)]



print([t[:-1]+(500,)for t in mytech])
