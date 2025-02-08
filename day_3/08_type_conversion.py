# all below examples belongs to Implicit conversion type

x = 10
y = 10.5
z = "Hello World"

q = x+y
print(q, type(q))

q = x-y
print(q, type(q))

q = x*y
print(q, type(q))

q = x/y
print(q,"type of q is:" , type(q))


# all below examples belongs to Explicit conversion type

age = input("what is your age?")
print(age, type (int(age))) # explicit conversion of string to integer

age = input("what is your age?")
print(age, type (float(age))) # explicit conversion of string to float

age = input("what is your age?")
print(age, type (str(age))) # explicit conversion of string to string



