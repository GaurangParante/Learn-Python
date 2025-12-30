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

def check_word_exist(word):
    with open("new.txt","r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("Found")
        else:
            print("Not found")

check_word_exist("Python")