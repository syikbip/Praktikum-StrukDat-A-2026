# Python Strings

# Strings
print("Hello")
print('Hello')

a = "Hello"
print(a)

# Multiline Strings

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Slicing

b = "Hello, World!"
print(b[2:5])

# Slice From the Start

b = "Hello, World!"
print(b[:5])

# Slice To the End

b = "Hello, World!"
print(b[2:])

# Negative Indexing

b = "Hello, World!"
print(b[-5:-2])

# Modify Strings

# Upper Case

a = "Hello, World!"
print(a.upper())
#
# Lower Case

a = "Hello, World!"
print(a.lower())

# Remove Whitespace

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#Replace String

a = "Hello, World!"
print(a.replace("H", "J"))

# Split String
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# tring Concatenation

a = "Hello"
b = "World"
c = a + b
print(c)

# Format - Strings

age = 36
txt = f"My name is John, I am {age}"
print(txt)

#Placeholders and Modifiers

price = 59
txt = f"The price is {price} dollars"
print(txt)

# Escape Characters
txt = "We are the so-called \"Vikings\" from the north."
