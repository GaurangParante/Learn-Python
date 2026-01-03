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

# class Account:
#     def __init__(self,bal,acc):
#         self.balance = bal
#         self.account_no = acc

#     # Debit method
#     def debit(self,amount):
#         self.balance -= amount
#         print("Rs.",amount,"was debited")
#         print("Total balance =",self.get_balance())

#     # Credit method
#     def credit(self,amount):
#         self.balance += amount
#         print("Rs.",amount,"was credited")
#         print("Total balance =",self.get_balance())

#     # Get Balance
#     def get_balance(self):
#         return self.balance
    

# acc1 = Account(10000,12345)
# # print(acc1.balance)
# # print(acc1.account_no)
# acc1.debit(1000)
# acc1.credit(500)

# Problem

# class Circle:
#     def __init__(self,redius):
#         self.redius = redius

#     def area(self):
#         return (22/7) * self.redius ** 2
    
#     def perimeter(self):
#         return 2 * (22/7) * self.redius
    
    
# c1 = Circle(21)
# print(c1.area())
# print(c1.perimeter())

# problem
# class Employee:
#     def __init__(self,role,dept,salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def showDetails(self):
#         print("Role=",self.role)
#         print("Dept=",self.dept)
#         print("Salary=",self.salary)

# class Engineer(Employee):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer","IT","75,000")


# e1 = Employee("Accountant","Finance","60,000")
# e1.showDetails()

# eng1 = Engineer("Gaurang","27")
# eng1.showDetails()


# Problem
class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self,odr2):
        return self.price > odr2.price
            
         

odr1 = Order("Chips",20)
odr2 = Order("Tea",15)

print(odr1 > odr2)