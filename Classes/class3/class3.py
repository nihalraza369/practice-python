# import pandas as pd
import re

# table = pd.read_html("https://www.w3schools.com/python/python_operators.asp")
# Strin Methods

message1 = "nihal"

message = """
I am {0}
i am {2} years old
I am in {1}
""".format("nihal", "10", "class")
my_name="Ha,mmad"
print(my_name.casefold())
print(my_name.find("am"))
print(message.isalpha())
print(message.isalnum())
print(message.islower())
print(message.isupper())
print(my_name.split(","))
print([*message1])

# print(message.splitlines())

# print(message.split())
# information = "I    am    nihal"
# other_information = re.sub(" {2,10}", " ", information)
# print(other_information)
# print(information.strip())


# myName:str="nihal"
# print(myName.split(""))
# print(message)


# unPack
# print([*myName])
# a="b"
# print(a[0])

# a[0]="v"
# a:list=[]
# b:list=[]
# print(a is b)

user = "b"
user2 = user

print("ID" , id(user))
print(user == user2)
print(user > user2)
print(user < user2)
print(user <= user2)
print(user >= user2)

# print(ord("b"))
list1: list = []
list2: list = []
print(list1 is list2)

MAX_VALUE = "bilal"

boundary1 = 'I told my friend, "Python is my favorite language!"'
boundary2 = "The language 'Python' is named after Monty Python, not the snake."
boundary3 = "One of Python's strengths is its diverse and supportive community."

message = 'One of Python\'s strengths is its diverse community.'


# operators

# print(table[0])

#      Operator        Name      Example
# 0        +        Addition    x + y
# 1        -     Subtraction    x - y
# 2        *  Multiplication    x * y
# 3        /        Division    x / y
# 4        %         Modulus    x % y
# 5       **  Exponentiation   x ** y
# 6       //  Floor division   x // y
a: int = 7
b: int = 2

print(a + b)  # addtition
print(a - b)  # subtraction
print(a * b)  # multiplication
print(a / b)  # division
print(a // b)  # Floor division


print(2**1000)
print(0 == True)
print(1 == True)


# Operator	Description	Example	Try it
# 0	is	Returns True if both variables are the same ob...	x is y	Try it »
# 1	is not	Returns True if both variables are not the sam...	x is not y	Try it »

# 	Operator	Description	Example	Try it
# 0	in	Returns True if a sequence with the specified ...	x in y	Try it »
# 1	not in	Returns True if a sequence with the specified ...	x not in y	Try it »

student = "Hammad"
students = ["bilal", "hammad"]

print("bilal" in students)
# uinput: str = input("Enter your name")


# Rule of PEMDAS

# *) Parentheses/Brackets
# *) Exponents (ie Powers and Square Roots, etc.)/Orders (ie Powers and Square Roots, etc.)
# *) MD Multiplication and Division (left-to-right)
# *) AS Addition and Subtraction (left-to-right)


calc = (2+3/(4*3)-5**2)  # (2+3/12-25) =>(1+0.25-25)
print(calc)

a, b, c = 2, 7, 3.0
print(a)  # => "bilal"
print(b)  # => 7
print(c)  # => 3.0
print()

num1: int = 2
num2: float = 6.0
print(num2/num1)

#  copy by whole value
film: dict = {"name": "nihal"}
film2: dict = {"name": "huzi"}
print("FIlm", id(film))
print("FIlm", id(film2))
print(film == film2)  # True
print(film is film2)  # False
print(True is 1)
print(False == 0)

print("Short", 1 == True > 4)
print("Short", 1 == True and True > 4)
print(id("nihal"))

print("Short", id("nihall")==2588480746096 ==id("nihal") )


print(5>4 and True==0)
print(5>4 or True==0)