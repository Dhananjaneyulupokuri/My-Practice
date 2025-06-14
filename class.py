class  Account :
    def __init__(self, accountNumber,userName, ifscCode, balance):
     self.accountNumber = accountNumber
     self.userName = userName
     self.ifscCode = ifscCode
     self.balance =balance 
     
    def method(self):
        print(self.accountNumber, self.userName, self.ifscCode, self.balance)

obj =Account(935301000872, "chowdary", "SBI000012", 200000) 
obj.method()

