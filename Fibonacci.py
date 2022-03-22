fibonacci_list = [1]
n1 = 0
n2 = 1
for i in range(9): # "range" just specifies how many times the function will be repeated
    next = n1 + n2
    n1 = n2
    n2 = next
    fibonacci_list.append(next)
print(fibonacci_list)
