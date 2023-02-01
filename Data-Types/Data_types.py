# Data types in python

''' 
Text Type:	        str
Numeric Types:	    int, float, complex
Sequence Types:	    list, tuple, range
Mapping Type:	    dict
Set Types:	        set, frozenset
Boolean Type:	    bool
Binary Types:	    bytes, bytearray, memoryview
None Type:	        NoneType
'''

num = 12
num1 = 10
print(str(num) + str(num1))


num2 = "23"
num3 = "10"
print(int(num2) + int(num3))


num4 = 30
num5 = 5
print(float(num+num5))


num6 = 5
num7 = 10
print(complex(num6+num7))


x = 1,2,3,4,5,6
print(list(x))


y = [1,2,3,4,5]
print(tuple(y))


z = range(6)
print(z)


a = [12,43,12,45,67,32]
print(set(a))


b = [121,45,32,5,21,54,121,5,6,8,32,43,5,6,34]
print(frozenset(b))


c = 10
d = c>=10
print(bool(d))


g = 34
print(bytes(g))


h = 12,23,45
print(bytearray(h))


j = bytes(12)
print(memoryview(j))


v = None
print(v)