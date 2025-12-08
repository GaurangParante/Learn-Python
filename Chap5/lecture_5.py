# count = 1 # iterators

# Loop is Iteration

# while count <= 5:
#     print("Hello ji")
#     count += 1

# print(count)

# i = 5
# while i > 0:
#     print(i)
#     i -= 1

# i = 1
# while i <= 5:
#     print(i)
#     if(i == 3):
#         break
#     i += 1

# tupel = (1,2,9,16,25,36,49,64,81,100)
# n = 9
# i = 0
# while i < len(tupel):
#     if(n == tupel[i]):
#         print("Found at index:",tupel[i])
#         break
#     else:
#         print('Finding...')
#     i += 1

i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue 
    print(i)
    i += 1
print("End of loop")