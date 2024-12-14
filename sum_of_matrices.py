a=[[12,23,34],
   [43,32,21],
   [56,67,78]]
b=[[47,58,69],
   [14,25,36],
   [12,23,33]]
result=[[0,0,0],
        [0,0,0],
        [0,0,0]]

for i in range(len(a)):
    for j in range(len(a)):
        result[i][j] =a[i][j]+b[i][j]
for r in result:

    print(r)