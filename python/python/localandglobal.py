# def asd():
#   a=10
#   def bsd():
#     print("inside asd()",a)
#   bsd()
# asd()
# print ("outside asd()",a)


# a=10
# def asd():
#     print("inside asd()",a)
# asd()
# print("outside asd()",a)

a=1
def asd(b):
    b=b+1

    if b<=10:
        print(b)
        asd(b)
asd(a)