#python variables
#creating variables
aku = 55373687
kamu = "teknik"
print(aku)
print(kamu)

x = "aku"      # x is of type str
x = "Sally" # x is of type str
x = 2.3 # x is now of type float
print(x)

#casting
nilai1 = float(88)    # x will be 88.0
nilai2 = int(100)    # y will be 100
nilai3 = str(20)  # z will be '20'

print(nilai1)
print(nilai2)
print(nilai3)

#get the type
x = 8.888
y = "mama"
g = 'iloveyou'
m = 20
print(type(x))
print(type(y))
print(type(g))
print(type(m))

#sigle or double quotes

s = "John"
# waluapun beda tanda tapi outputnya sama dan tipe data nya sama
e = 'John'
print(x)

#case sensitive
nama = 555
dia = "Rudi"
Aku = 'syikbi'
print(nama)
print(dia)
print(Aku)

#camel case
myNameIs = "Syikbi"
print(myNameIs)

#pascal case
MyNameIs = "syikbi"
print(MyNameIs)

#snake case
my_name_is = 'syikbi'
print(my_name_is)

# Many Values to Multiple Variables

data1, data2, data3 = "alfamart", "indomaret", "ayam geprek"
print(data1)
print(data2)
print(data3)

# One Value to Multiple Variables
x = y = z = "orang","rudi",'mandi'
print(x)
print(y)
print(z)

# Unpack a Collection
makanan = ["apple", "banana", "cherry"]
makanann = ['siomay','sup','ikan']
x, y, z = makanan
a, b, c = makanann
print(x)
print(y)
print(z)
print(a)
print(b)
print(c)

#Output Variables
variable = "saya suka makan 'futsal"
print(variable)

x = "saya suka"
y = "makan"
z = "dan futsal"
print(x, y, z)

x = "aku "
y = "dan "
z = "kamu "
print(x + y + z)

# Global Variables
x = "sholat daan tidur"

def myfunc():
  print("saya akan " + x)

myfunc()

# The global Keyword

def myfunc():
  global x
  x = "wangkitogalo"

myfunc()

print("Palembang is " + x)