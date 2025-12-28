# Problem 1

# def len_list(a):
#     print(len(a))

# def print_with_space(a):
#     for i in list:
#         print(i,end=" ")

# list = ["hello","value",6,5]
# len_list(list)
# print_with_space(list)

# Problem 3

# def factorial(n):
#     i = 1
#     fact = 1
#     while i <= n+1:
#         fact *= i
#         i += 1
#     print(fact)

# factorial(6)

# Problem 4

# def usd_to_inr(usd):
#     print(usd * 90)
#     return usd * 90
# usd_to_inr(12)

# Home work

# n = int(input("Enter number:"))

# def check_odd_even(n):
#     if(n % 2 == 0):
#         print("ODD")
#     else:
#         print("EVEN")

# check_odd_even(n)


# Problem 

# def sum_n(n):
#     if(n == 0):
#         return 0
#     return n + sum_n(n-1)

# print(sum_n(120))

# Problem



# def print_element(n):
#     if(n == 0):
#         return 0
#     print_element(n -1)
#     print(fruits[n-1])
# print_element(len(fruits))



def print_ele(list,idx = 0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_ele(list,idx+1)

fruits = ["Apple","Banana","Kiwi","Graps","Pineapple"]
print_ele(fruits)