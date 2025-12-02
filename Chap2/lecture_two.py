#Strings
# str1 = "This is a string."
# str2 = 'Gaurang'
# str3 = """This is also string."""


#escape sequence characters (Formatting)
# str1 = "This is a string.\twe are creating it in python."
# print(str1)


#Opration On String
# a = "Gaurang"
# len_a = len(a)
# print(len_a)

# b = "Parante"
# len_b = len(b)
# print(len_b)
# final_str = a + " " + b

# print(final_str)
# print(len(final_str))


#Indexing
# str1 = "GAURANG_PARANTE"
# ch0 = str1[0]
# ch3 = str1[3]
# print(ch3)

#Slicing
# str1 = "GAURANG_PARANTE"
# print(str1[2:8])
# print(str1[:4]) #[0:4]
# print(str1[8:]) #[8:len(str1)]
# print(str1[4:len(str1)])


#Nagitive Indexing
# str1 = "Apple"
# print(str1[-3:-1])


#String Functions
# str1 = "i am learning python"
# print(str1.endswith("on"))
# print(str1.endswith("app"))
# print(str1.capitalize())
# print(str1.replace("python","JS"))
# print(str1.find("o"))
# print(str1.count("a"))

#Conditional Statements
# age = 27
# if(age >= 18):
#     print("Can vote & apply for license") #Tab (4 spaces) its called indentation

# light = "yellow"
# if(light == "green"):
#     print("Go")
# elif(light == "red"):
#     print("Stop")
# elif(light == "yellow"):
#     print("Look")

# light = "pink"
# if(light == "green"):
#     print("Go")
# elif(light == "red"):
#     print("Stop")
# elif(light == "yellow"):
#     print("Look")
# else:
#     print("Light is broken")


# marks = int(input("Enter your marks: "))

# if(marks >= 90):
#     grade = "A"
# elif(marks >= 80 and marks < 90):
#     grade = "B"
# elif(marks >= 70 and marks < 80):
#     grade = "C"
# else:
#     grade = "D"

# print("Your grade is",grade)

age = 95
if(age >= 18):
    if(age >= 80):
        print("Can not drive")
    else:
        print("Can drive")
else:
    print("Can not drive")