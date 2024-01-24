# Python Home and Intro
print("Hello World")

#Python Syntax
if 5 > 2:
    print("Five is greater than two!")
# If we use without TAB it will be send mistake
# You have to make 4 spaces but it can be more
#This is comment
print("Hello World")

print("Hello World") # This is comment

#print("Hello, World!")
print("Cheers, Mate!")

#This is a comment
#written in
#more than just one line
print("Hello, World!")
#Creating Variables
x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#Get the type
x = 5
y = "Jonh"
print(type(x))
print(type(y))

#Single or Double Quotes
x = "John"
# is the same as
x = 'John'


#Case-Sensitive
a = 4
A = "Sally"
#A will not overwrite a

# Variable Names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output Variables
x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print(x + y)

x = 5
y = "John"
print(x, y)


# Global Variables
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#The global Keyword
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)
#Getting the datatype
x = 5
print(type(x))
#Python Numbers
x = 1 #int
y = 2.8 #float
j = 1j #complex


#Python casting
x = int(1) # will be 1
y = int(2.8) # will be 2
z = int("3") # will be
#Float
x = float(1)     #will be 1.0
y = float(2.8)   #will be 2.8
z = float("3")   #will be 3.0
w = float("4.2") #will be 4.2

#String
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
# Assign String to a Variable
a = "Hello"
print(a)
#Multyline
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# Strings are Arrays
a = "Hello, World!"
print(a[1])

# Looping Through a String
for x in "banana":
  print(x)

# String Length
a = "Hello, World!"
print(len(a))

# Check String
txt = "The best things in life are free!"
print("free" in txt)

#actually we can use 'in' with if

# Slicing
b = "Hello, World!"
print(b[2:5])

#Slice from the Start
b = "Hello, World!"
print(b[:5])

#Slice to the end
b = "Hello, World!"
print(b[2:])

#Upper
a = "Hello, World!"
print(a.upper())

#Lower
a = "Hello, World!"
print(a.lower())

#Remove Whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#Replace String
a = "Hello, World!"
print(a.replace("H", "J"))

#Split String
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

# String Format
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# We can use index
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# Escape Character
txt = "We are the so-called \"Vikings\" from the north."