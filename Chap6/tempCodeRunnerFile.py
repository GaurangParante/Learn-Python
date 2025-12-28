
def print_element(n):
    if(n == 0):
        return 0
    print_element(n -1)
    print(fruits[n-1])
print_element(len(fruits))