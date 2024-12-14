num=int(input("enter the number:"))
factorial=1
if num == 0:
    print("factorial for ",num,"is 1")
elif num < 0:
    print("factorial does not exist for negative numbers")
else:

    for  i in range(1,num+1):
        factorial = factorial * i
    print(factorial)