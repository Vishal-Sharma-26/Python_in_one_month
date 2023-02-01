# a = 34
# b = 10
# a,b=b,a
# print(b)
# print(a)

a = 4
def polynomial(a, b, c, x):
    return a*x**2 + b*x + c

b = a
b *= a
c = 1
result = polynomial(a, b, c, 0)
a += 3
a = 0    