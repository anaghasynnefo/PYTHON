# n=5
# for i in range(1,n+1):
#     for j in range(n-1):

# for i in range(1,6):
#   for j in range(1,i+1):
#        print(i)
# print("\n")

# ls=[]
# for i in range(2,101,2):
#     ls.append(i)
# print(ls)
    
    
# ls=[]
# for i in range(1,51):
#     ls.append(i)
# print(ls)

for i in range(1,101):
  if i%3==0 and i%5==0:
    print ("fizzbuzz")
  elif i % 3==0:
   print("fizz")
  elif i%5==0:
    print("buzz")
else:
  print(i)

