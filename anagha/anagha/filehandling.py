# file=open("demo.txt","a")
# file.write("hello team")
# # file.close
# s=file.readlines()
# print(s)
# file.close

# file=open("demo.txt","w")
# file.write("hello team")
# # file.close
# # s=file.readlines()
# # print(s)
# file.close

with open("demo.txt","r")as file:
    s=file.read()
    print(s)