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
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("Car started...")

car1 = Car()
car1.start()