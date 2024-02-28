import os
import fnmatch
list_file = os.scandir("class11")

# for file in list_file:
#     if file.is_file():
#         print(file)

# with os.scandir("class11") as f1:
#     for file in f1:
#         if file.is_file():
#             print(file)    

# for file in list_file:
#     print("Name FIle", file.name)    
#     print(file.path)    
#     # fnmatch.fnmatch(file,"class.*")
#     print(file.stat().st_mtime)
#     # os.remove(file)
#     # os.mkdir("class11/Ui")
#     os.makedirs("class11/utils/cn")
#     break    

# mather = fnmatch.fnmatch("*","class")
# print(mather) 
   
   
   
  
pattern = 'class.*'
print ('Pattern :', pattern ) 
# print() 
  
files = os.listdir('.')  
for name in files:  
    print ('Filename: %-25s %s' % (name, fnmatch.fnmatch(name, pattern))) 
    
for file in list_file:
    if fnmatch.fnmatch(file,"main.*"):
        print("")  