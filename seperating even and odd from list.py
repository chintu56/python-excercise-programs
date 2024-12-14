li=list(range(0,100+1))
even_numbers=[]
odd_numbers=[]
for i in li:
    if i%2==0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)
print("EVEN NUMBERS ARE:",even_numbers)
print("ODD NUMBERS ARE:",odd_numbers)