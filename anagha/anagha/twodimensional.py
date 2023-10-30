m=int(input("enter the number of rows(m)"))
n=int(input("enter the number of columns(n)"))
array=[[i*j for j in range(n)]for i in range(m)]
for row in array:
    print(row)