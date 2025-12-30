# Problem

# string = "Hello everyone\nwe are learning file I/O\nusing Java.\nI like programming in Java"

# with open("new.txt","w") as f:
#     f.write(string)

# Problem

# with open("new.txt","r") as f:
#     data = f.read()

# new_data = data.replace("Java","Python")   
# print(new_data)
# with open("new.txt","w") as f:
#     f.write(new_data)

# Problem

# def check_word_exist(word):
#     with open("new.txt","r") as f:
#         data = f.read()
#         if(data.find(word) != -1):
#             print("Found")
#         else:
#             print("Not found")

# check_word_exist("Python")

# def check_for_line(word):
#     data = True
#     line_no = 1
#     with open ("new.txt","r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print("Found at Line no:",line_no)
#                 return
#             line_no = line_no + 1

#     return -1

# print(check_for_line("Python"))

count = 0
with open("new.txt","r") as f:
    data = f.read()
    # print(data)
    # num = ""
    # for i in range(len(data)):
    #     if(data[i] == ","):
    #         print(int(num))
    #         num = ""
    #     else:
    #         num += data[i]
    nums = data.split(",")
    for value in nums:
        if(int(value) % 2 == 0):
            count += 1
print(count)