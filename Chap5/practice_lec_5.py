# Program 1
# i = 1

# while i <= 100:
#     print(i)
#     i += 1

# Program 2
# i = 100

# while i >= 1:
#     print(i)
#     i -= 1


# Program 3
# n = int(input("Enter number for table : "))
# i = 1
# while i <= 10:
#     print(n,"*",i,"=",i*n)
#     i += 1

# Program 4
# list = [1,2,9,16,25,36,49,64,81,100]

# i = 0

# while i < len(list):
#     print(list[i])
#     i += 1

# Program 5
tupel = (1,2,9,16,25,36,49,64,81,100)
n = 9
i = 0

while i < len(tupel):
    if(n == tupel[i]):
        print("Found at IDX:",i)
    else:
        print("Finding...")
    i += 1
