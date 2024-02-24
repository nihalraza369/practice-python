
# Data types

# 1) String
name: str = "fawad"

# 2) Integer
age: int = 12

# 3) list
friends: list[str] = ["Fawad", "Huzair"]
print(friends[0])

# 4) Set
logged_user: set = {"fawad", "fawad", 1, 2, 2}
print(logged_user)

# 5) Complex
square: complex = 1+4j
print(square.conjugate())
print(square.imag)
print(square.real)

# 6) Float
percentage = 30.6

# age = percentage + 30
# print(type(age))

# Muteable and Immutaeable

# Muteable

# 1) List
students: list = ["Hammad", "Ahssan"]
students[0] = "bilal"

# 2) Sets


# Immutaeable
# 1)string
myName = "bilal"
print(myName[0])

# 2)Tuple

numbers_std: tuple[str, str] = ("bilal", "fawad")
# numbers_std[0]="Bilal" Shoe Error

data = f"""
name:{name}
"""

# F String with jinja
course1 = "web"
course2 = "app"
course3 = "graphic"
age = 12

peroperties_std = f"""
course1 : %s
course2 : %s
course3 : %s
age: %d
""" % (course1, course2, course3, 12)

peroperties_tea = f"""
course1 : {{course1}}
course2 : {{course1}}
course3 : {{course1}}
"""

print(peroperties_tea)

# F String
message = f" My name is {myName.upper()}"
print(message)

print(True + 4)
