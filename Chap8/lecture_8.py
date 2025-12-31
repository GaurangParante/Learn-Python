## Class & Object in Python

# class Student:
#     name = "Karan"

# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s2.name)

# class Car:
#     color = "blue"
#     brand = "mercedes"

# car1 = Car()
# print(car1.color)
# print(car1.brand)


## __init__ Function Or Constractor 

# class Student:
#     # Default Constructors
#     # def __init__(self):
#     #     pass

#     # Parameterized constructors
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("Adding new student in Database...")

# s1 = Student("Karan",98)
# print(s1.name)
# print(s1.marks)

# s2 = Student("Arjun",97)
# print(s2.name)
# print(s2.marks)

## Class & Instance Attributes

# class Student:
#     collage_name = "ABC Collage" # class Attribute
#     name = "Anonymous" # class attribute
#     def __init__(self,name):
#         self.name = name # object attribute > class attribute

# s1 = Student("Karan")
# print(s1.name)
# print(s1.collage_name)

## Methods

# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     def welcome(self):
#         print("Welcome student,",self.name)

#     def get_marks(self):
#         return self.marks

# s1 = Student("Karan",97)
# s1.welcome()
# print(s1.get_marks())

## Static Method

# class Student:
#     def __init__(self,marks):
#         self.marks = marks

#     @staticmethod
#     def hello():
#         print("Hello")

# s1 = Student(97)
# print(s1.marks)
# s1.hello()


## Important
# Abstration
# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("Car started...")

# car1 = Car()
# car1.start()


## del keyword

# class Student:
#     def __init__(self,name,mark):
#         self.name = name
#         self.mark = mark

# s1 = Student("Gaurang",60)
# print(s1)
# # del s1
# del s1.name 
# print(s1)

## Private atributes and methods

# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass

#     def reset_pass(self):
#         print(self.__acc_pass)


# acc1 = Account("123546","Test@123")

# print(acc1.acc_no)
# # print(acc1.__acc_pass)
# acc1.reset_pass()

# class Person:
#     __name = "anonymous"

#     def __hello(self):
#         print("Hello")

#     def welcome(self):
#         self.__hello()

# p1 = Person()
# p1.welcome()

## Inheritance
# Single Inheritance

# class Car:
#     color = "black"
#     @staticmethod
#     def start():
#         print("Car started...")

#     @staticmethod
#     def stop():
#         print("Car stopped...")

# class ToyotaCar(Car):
#     def __init__(self,name):
#         self.name = name


# car1 = ToyotaCar("Fortuner")
# car2 = ToyotaCar("Prius")
# print(car2.color)
# car2.start()

# Multi-level Inheritance

# class Car:
#     @staticmethod
#     def start():
#         print("Car started...")

#     @staticmethod
#     def stop():
#         print("Car Stopped...")

# class ToyotaCar(Car):
#     def __init__(self,brand):
#         self.brand = brand

# class Fortuner(ToyotaCar):
#     def __init__(self,type):
#         self.type = type


# car1 = Fortuner("Disel")
# car1.start()

# Multiple Inheritance

# class A:
#     varA = "Welcome class A"

# class B:
#     varB = "Welcome class B"

# class C(A,B):
#     varC = "Welcome class C"

# c1 = C()
# print(c1.varA)
# print(c1.varB)
# print(c1.varC)

## Super Methods

# class Car:
#     def __init__(self,type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("Car Started...")

#     @staticmethod
#     def stop():
#         print("Car Stopped...")

# class ToyotaCar(Car):
#     def __init__(self,name,type):
#         super().__init__(type)
#         self.name = name
#         super().start()

# c1 = ToyotaCar("prius","electric")

# print(c1.type)

## Class Method

# class Person:
#     name = "Anonymous"

#     # def changeName(self,name):
#     #     self.__class__.name = name
#     #     Person.name = name
#     #     self.name = name

#     @classmethod
#     def changeName(cls,name):
#         cls.name = name

# p1 = Person()
# p1.changeName("Rahul Kumar")
# print(p1.name)
# print(Person.name)

# Property

# class Student:
#     def __init__(self,phy,chem,math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#         # self.percentage = str((self.phy+self.math+self.chem)/3) + "%"

#     # def calcPercentage(self):
#     #     return str((self.phy+self.math+self.chem)/3) + "%"

#     @property
#     def percentage(self):
#         return str((self.phy+self.math+self.chem)/3) + "%"

# s1 = Student(98,97,99)

# print(s1.percentage)
# s1.phy = 86
# print(s1.percentage)

## Polymorphism : Operator Overloading

# print(1 + 2) #add
# print(type(1))

# print("Gaurang" + "Parante") # concate
# print(type("Gaurang"))

# print([1,2,3] + [4,5,6]) # Merge
# print(type([1,2,3]))


class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def showNumber(self):
       print(self.real ,"i" , self.img , "j")
    
    def __add__(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)
    
    def __sub__(self,num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal,newImg)
    

num1 = Complex(1,4)
num2 = Complex(3,8)
num3 = num1 - num2
num3.showNumber()