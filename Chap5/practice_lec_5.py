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
# tupel = (1,2,9,16,25,36,49,64,81,100)
# n = 9
# i = 0

# while i < len(tupel):
#     if(n == tupel[i]):
#         print("Found at IDX:",i)
#     else:
#         print("Finding...")
#     i += 1


# Program 6
# list = [1,2,9,16,25,36,49,64,81,100]

# for val in list:
#     print(val)

# Program 7
# list = (1,2,9,16,25,36,49,64,81,100,36)
# x = 36
# idx = 0
# for el in list:
#     if(el == x):
#         print("X found at idx:",idx)
#         break
#     idx += 1

# Program 8
# for i in range(1,101):
#     print(i)

# Program 9
# for i in range(100,0,-1):
#     print(i)

# Program 10
# n = int(input("Enter number: "))
# for i in range(1, 11):
#     print(n,'*',i,'=',n*i)

# Program 11
n = 5
i = 1
sum = 0
while i <= n:
    sum += i
    i +=1
print(sum)

fact = 1
for i in range(1,n+1):
    fact *= i

print(fact)
