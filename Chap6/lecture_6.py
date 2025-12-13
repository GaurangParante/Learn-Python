# a = 10
# b = 15
# sum = a + b
# print(sum)

# insted of this make function who do this multiple time when you required

# def calc_sum(a,b):
#     sum = a + b
#     return sum

# print(calc_sum(5,6)) # call function

# Function Defination
# def calc_sum(a, b): # Parameters
#     return a + b

# sum = calc_sum(1,3) # Function call,arguments
# print(sum)

# def print_hello():
#     print("Hello")

# print_hello()
# print_hello()
# print_hello()\

# output= print_hello()
# print(output) # None


# Average of 3 numbers
# def average_of(a,b,c):
#     return (a + b + c)/3

# a = int(input("Enter first value: "))
# b = int(input("Enter second value: "))
# c = int(input("Enter third value: "))

# output = average_of(a,b,c)
# print(output)


# print("Gaurang" , end=" ")
# print("Parante")

# def cal_mul(a = 1,b = 1):
#     mul = a * b
#     print(a*b)
#     return mul

# cal_mul()

def show(n):
    if n == 0:
        return
    print(n)
    show(n-1)

show(5)