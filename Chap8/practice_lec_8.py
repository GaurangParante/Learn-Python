# Problem

# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hello",self.name,"your avg score is:",sum/3)


# s1 = Student("Karan",[97,99,98])
# s1.get_avg()

# s1.name = "Ironman"
# s1.get_avg()

class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc

    # Debit method
    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount,"was debited")
        print("Total balance =",self.get_balance())

    # Credit method
    def credit(self,amount):
        self.balance += amount
        print("Rs.",amount,"was credited")
        print("Total balance =",self.get_balance())

    # Get Balance
    def get_balance(self):
        return self.balance
    

acc1 = Account(10000,12345)
# print(acc1.balance)
# print(acc1.account_no)
acc1.debit(1000)
acc1.credit(500)
