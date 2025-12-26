

# 1 : create file

# 2 : read file

# 3 : write file

# 4 : append file 


# =========================

# 1 : create file 

# f = open("index.py","x")
# print("File Created")
# f.close()

# 2 : read file 

# f = open("index.html","r")
# data=f.read()
# data = f.readline()
# data = f.readlines()
# print(data)
# print(data[4])
# f.close()


# 3 : write file 

# f = open("index.py","w")
# f.write("print('Hello Python')")
# f.close()


# 4 : append file 

# f = open("index.py","a")
# for i in range(11,21):
#     f.write(f"\nprint('Hello Python') - {i}")
# f.close()


# ==========================================

# 1 : create file 

# with open("index.html","x") as a:
#     print("File Created")

# with open("index.py","x") as a:
#     print("File Created")


# 2 : read file : 

# with open("index.html") as a:
    # data=a.read()
    # data=a.readline()
    # data=a.readlines()
    # print(data)


# 3 : write file : 

# with open("index.py","w") as a:
#     a.write("print('Hello Python')")


# 4 : append file :


# with open("index.py","a") as a:
#     a.write("\nprint('Hello Python')")


# =================================

# f = open(r"C:\Users\bhvik\Desktop\file handling\home.html","x")
# print("File Created")
# f.close()               
    
# ===================

# import os

# os.remove("index.py")
