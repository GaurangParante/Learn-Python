# f = open("demo.txt","r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

# f = open("demo.txt","r")
# # data = f.read(6)
# line1 = f.readline()
# print(line1)
# line2 = f.readline()
# print(line2)
# f.close()

# f = open("demo.txt","w")
# f.write("Hello this is new function for write data using python")
# f.close()

# f = open("demo.txt","a")
# f.write("\nThis is append function")
# f.close()

# If file not exist w and a mode will create file and then preform task
# f = open("sample.txt","w")
# f.close()

# f = open("demo.txt","r+")
# f.write("test")
# print(f.read())
# f.close()

# f = open("demo.txt","w+")
# print(f.read())
# f.write("Test 13")
# f.close()

# f = open("demo.txt","a+")
# f.write("This is append")
# print(f.read())
# f.close()

# with open("demo.txt","r") as f:
#     print(f.read())

# with open("demo.txt","w") as f:
#     f.write("New data")

import os
os.remove("sample.txt")