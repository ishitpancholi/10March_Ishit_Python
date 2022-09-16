#multiple geritance

class abhijeet:
    aid=0
    asub=""

    def a_getdata(self):
        self.aid=input("Enter your id:")
        self.asub=input("Enter your subject:")
class daya:
    did=0
    dsub=""

    def d_getdata(self):
        self.did=input("Enter your id:")
        self.dsub=input("Enter your subject:")


class acp(abhijeet,daya):

    def get_detail(self):
        print("-----------------------------")
        print("abhijeet id:",self.aid)
        print("abhjeet suubject:",self.asub)
        print("-----------------------------")
        print("daya id:",self.did)
        print("daya subject:",self.dsub)

dcp=acp()        
dcp.a_getdata()
dcp.d_getdata()
dcp.get_detail()
