###PRIME NUMBERS
div_num = 0
num = (input("Please enter a number as integer : "))
if num.isdigit():
    for i in range(2, int(num)):
        if int(num) % i == 0 :
           div_num += 1         
    if div_num == 0 :
        print(f"{num} is a prime number")
    else :
        print(f"{num} is not a prime number")
else:
    print("Invalid value spotted. Please enter a integer number")
