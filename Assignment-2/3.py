# Remove duplicate from list
list=[10,20,30,40,50,20,60,30]
dup_items=set()
uniq_items=[]
for x in list:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)
print(dup_items)
