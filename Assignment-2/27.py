# Program to cobine two dicitonary adding values for common key:-
from collections import Counter
d1={"a":100,"b":200,"c":300}
d2={"a":300,"b":200,"c":400}

d=Counter(d1) + Counter(d2)

print(d)