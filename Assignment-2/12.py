# To check Weather a list contains a sub list


list=['a','b',[1,2,3,4,5,'Monsoon']]
for i in list:
    if len(i) > 2:
        print("Sub list present in list")
        break
else:
    print("Sub list is not present")    

    

