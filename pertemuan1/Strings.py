# Python Strings

# Strings
print("saya syikbi")
print('Hallloooo')

a = "syikbi sp"
b = 'makan'
print(a)
print(b)

# Multiline Strings

a = """nama saya syikbi,umur saya 19 th,saya dari kuansing
3beradik,dan saya kuliah di unri."""
print(a)

# Slicing

b = "Haiii, mengapa???"
print(b[2:7])

# Slice From the Start

b = "yessss!!!!, hmm???!"
print(b[:9])

# Slice To the End

b = "m,syikbi,,, septa,putra"
print(b[8:])

# Negative Indexing

b = "Hayoo,,loo, ngapainnn!"
print(b[-7:-3])

# Modify Strings

# Upper Case

a = "Hello, aaakuuuUUU!"
print(a.upper())
#
# Lower Case

a = "HAIIIII,,KAMUUUuuu, CCCantikkkK"
print(a.lower())

# Remove Whitespace

a = "kamu bagus,dan,pintar     "
print(a.strip()) # returns "strip"

#Replace String

a = "Hello, World!"
print(a.replace("o", "c"))

# Split String
a = ",,,,saya,kamu,,dia"
print(a.split(",")) # returns ['Hello', ' World!']

# tring Concatenation

a = "mengabungkan"
b = "string"
c = a + b
print(c)

# Format - Strings

age = 9
txt = f"saya ulang tahun bulan {age}"
print(txt)

#Placeholders and Modifiers

price = 1000
txt = f"saya punya uang {price} dollars"
print(txt)

# Escape Characters
txt = "cita cita saya \"polisi\" AU."
print(txt)
