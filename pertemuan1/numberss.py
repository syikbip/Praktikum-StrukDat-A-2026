# Python Numbers

a = 1    # int
y = 2.8  # float
z = 100j   # complex

print(type(a))
print(type(y))
print(type(z))

# Type Conversion

x = 1.7   # float
y = 2  # int
z = 10j   # complex
d = 5 # int
#convert from float to int:
a = float(x)

#convert from int to complex:
b = int(y)

#convert from complex to int:
c = complex(x)

#convert from complex
d = int (d)

print(a)
print(b)
print(c)
print(d)

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# Random Number
import random

print(random.randrange(7, 20))