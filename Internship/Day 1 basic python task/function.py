from ast import arguments


def area(Lenght,Width):
    return Lenght * Width

length = 10
width = 5
print(area(length, width))

length = 20
width = 8
print(area(length, width))

length = 50
width = 12
print(area(length, width))



def welcome():
    print("Welcome")

for i in range(2):
    welcome()


def greet(name):
    print("Hello", name)

greet("Saad")


def add(a, b):  # a and b are parameters
    print(a + b)

add(10, 20) # 10 and 20 are arguments

# we give values to the parameters when we call the function. These values are called arguments. 


