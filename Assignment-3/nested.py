sub1=int(input("Enter Subject Mark:"))
sub2=int(input("Enter Subject Mark:"))
sub3=int(input("Enter Subject Mark:"))
#-------------------------------------#
print("Subject1=",sub1)
print("Subject1=",sub2)
print("Subject1=",sub3)

if sub1>=40 and sub2>40 and sub3>40:

    print("------------------------------")

    total=sub1+sub2+sub3
    print(total)

    print("--------------------------------")

    pr=total/3
    print(pr)

    print("--------------------------------")

    if pr>=70:
        print("Result: Disction")
    elif pr>=60:
        print("Result: First Class")
    elif pr>=50:
        print("Result: Second Class")
    elif pr>=40:
        print("Result Third Class")
else:
    print("Fail")          

    
    