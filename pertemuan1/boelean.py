print(10 < 9)
print(10 == 9)
print(10 > 9)
print(100 >= 9)


a = 20000
b = 300

if b > a:
  print("b adalah bilangan prima ")
else:
  print("b adalah bilangan ganjil")

print(bool("saya"))
print(bool(15))

x = "hewan"
y = 150

print(bool(x))
print(bool(y))


bool(False)
print(bool(bool))

class myclass():
  def __len__(self):
    return 1

myobj = myclass()
print(bool(myobj))

x = 2
print(isinstance(x, float))