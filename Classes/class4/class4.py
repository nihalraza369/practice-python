# Calculator Project

num_1 = int(input("Enter your first number: "))
num_2 = int(input("Enter your second number: "))
user_operator = input("Enter an operator (+, -, *, /): ")

value = f"{num_1}{user_operator}{num_2}"
print("Your Output is", eval(value))
