# s=lambda a,b:a*b
# z=s(5,3)
# print(z)

# s=lambda a,b:a+b
# z=s(15,30)
# print(z)

# def fun(a):
#     return lambda b:a+b
# x=fun(3)
# print(x)

# def fun(a):
#     return lambda b:a+b
# x=fun(3)
# print(x(6))

# def fun(a):
#     return lambda b:a*b
# x=fun(3)
# print(x(3))

# def fun(a):
#     return lambda b:a/b
# x=fun(3)
# print(x(25))


"""functional programming"""

def add(a,b):
    return a+b

def sqr(x):
    return x**2
z=sqr(add(5,3))
print(z)