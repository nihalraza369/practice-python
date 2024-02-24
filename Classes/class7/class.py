import math
# print(object.__instancecheck__([]))
# num1="bilal"
# li=num1.__iter__()
# print(next(li))
# print(li)
# print(next(li))
# print(next(li))
# print(li)
# print(next(li))
# print(next(li))
# print(next(li))

# fi=open("file.txt")
# print(fi.readline(), end="")
# print(fi.readline())
# print(fi.readline())
# print(fi.readline())


# PROBLEM 01
# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
# for num in numbers:
#     if num > 0:
#         print(num)


# PROBLEM 02

# user_num = 10
# start_num = 1
# sum_even: list = []

# while start_num <= user_num:
#     if start_num % 2 == 0:
#         sum_even.append(start_num)

#     start_num += 1

# print(f"Sum of Even Numbers {sum(sum_even)}")

# PROBLEM 03
# num1 = 3
# print(list(range(10)))

# # for i in range(1, 11):
# #     if i == 5:
# #         continue

# #     print(f"3 X{i} = {num1*i}")

# [print(num1*num) if num != 5 else print("5 is not valid")  for num in range(1,11)]

# list_abc=[i for i in ["a", "b", "c"]]
# print(list_abc)
# user_sent = "bilal"
# reverse_str = "ib"
# for chr in user_sent:
#     reverse_str = chr+reverse_str

# print(reverse_str)

# PROBLEM 05
# my_name = "bilal"
# for i in my_name:
#     if my_name.count(i) == 1:
#         print(i)
#         break

# PROBLEM 06
# fact_num=9
# num1=fact_num-1
# factorial_num=fact_num
# while num1>1:
# 	fact_num=fact_num*num1
# 	num1-=1

# print("Factorial of %d = %d "% (factorial_num,fact_num))
# print(math.factorial(9))

# PROBLEM 07
# user_condition = True
# while user_condition:
#     user_input = int(input("Enter a number"))
#     if user_input == 1 or user_input == 10:
#         print(f"You have entered {user_input}")
#         user_condition = False


# PROBLEM 08
num3=5
specific_condition=True

for num in range(num3-1,1,-1):
    if num3%num==0:
        specific_condition=False
        print(f"{num3} is not a Prime number")
        break

if specific_condition:
    print(f"{num3} is a Prime number")    
        