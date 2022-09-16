#multilevel heritance
class maganlal:
    land=0
    cow=0

    def m_data(self):
        self.land=input("Enter land detail:")
        self.cow=input("Enter cow detail:")

class janakrai(maganlal):
    gold=0
    house=0
    
    def j_data(self):
        self.gold=input("Enter gold detail:-")
        self.house=input("Enter house detail:-")

class kamlesh(janakrai):
    car=0
    bal=0

    def k_data(self):
        self.car=input("Enter car detail:-")
        self.bal=input("Enter bank detail:-")

class ishit(kamlesh):
    def i_data(self):
        print("land:",self.land)
        print("cow:",self.cow)
        print("gold:",self.gold)
        print("house:",self.house)
        print("car:",self.car)
        print("balance:",self.bal)

Ishit=ishit()
Ishit.m_data()
Ishit.j_data()
Ishit.k_data()
Ishit.i_data()
