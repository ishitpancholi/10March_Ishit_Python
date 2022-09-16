#object orinented programming
#class create


class student:
    stid=4
    stnm="Ishit"

    def getdata(self):
        print("This is get data from  student")


#object create

ishit=student()
print(ishit.stid)
print(ishit.stnm)
ishit.getdata()