string=str(input("enter the string:"))
if(string==string[::-1]):
    print(string,"is a palindrome")
else:
    print(string,"is not a palindrome")