import os

list_file = os.scandir("class11")

for file in list_file:
    if file.is_file():
        print(file)

# with os.scandir("class11") as f1:
#     for file in f1:
#         if file.is_file():
#             print(file)    

      