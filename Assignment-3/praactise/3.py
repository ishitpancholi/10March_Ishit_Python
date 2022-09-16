#single heritance
class father:
    car=0
    bal=0

    def get_data(self):
        self.car=input("enter car detail:")
        self.bal=input("enter bank balance:")
class son(father):

    def printdata(self):
        print("car",self.car) 
        print("bal",self.bal)
sons=son()
sons.get_data()
sons.printdata()              