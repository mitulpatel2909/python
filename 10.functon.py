

# function type 

# 1 : pre define function     : len , max , min , sum , type , input etc.
# 2 : user define function    : name , mitul  etc.

# =========================


# for i in range(1,11):
#     print(i)

# print()
# for i in range(11,21):
#     print(i)



# simple function 

# def number_1_10():
#     for i in range(1,11):
#         print(i)

# def number_11_21():
#     for i in range(11,21):
#         print(i)


# number_11_21()


# peramiter function 

# def user(name):
#     print(f"Hello {name}")

# user("mitul")


# def number_print(number):
#     for i in range(number,21):
#         print(i)

# number_print(15)


# default peramiter function

# def user(name="mitul",age=21):
#     print(name,age)

# user("python",22)


# local variable

# def user():
#     name="mitul"
#     print(name) 
# user()    


# global variable 


# name="mitul"
# def user():
#     print("user function",name) 
# def user1():
#     print("user 1 function",name) 
# user() 
# user1() 

# print(name)



# a=10
# b=10
# c=10
# def number_plus():
#     global b
#     num=a+b+c
#     print(num)
# number_plus()


# args 

# def user(a,b,c,d,e):
#     print(a,b,c,d,e)
# user(1,2,3,4,5)    


# def user(*args):
#     print(args)
# user(1,2,3,4,5,6,7)   

# def user(*args):
#     print(max(args))
# user(1,2,3,4,5)   

# def user(*args):
#     for i in args:
#         print(i)
# user(1,2,3,4,5)   



# kwargs

# def user(**kwargs):
#     print(kwargs)
# user(name="python",age=21)    

# def user(**kwargs):
#     print(kwargs.keys())
# user(name="python",age=21)    


# def user(**kwargs):
#     print(kwargs.values())
# user(name="python",age=21)    

# def user(**kwargs):
#     print(kwargs.items())
# user(name="python",age=21)    


# map function 

# l1 = [1,2,3,4,5,6,7,8,9,10]
# # output : [1,4,9,16,25,36,49,64,81,100] 
# l2=[]
# for i in l1:
#     l2.append(i*i)
# print(l2)


# def fun(l1):
#     return l1*l1
# l1 = [1,2,3,4,5,6,7,8,9,10]

# a = map(fun,l1)
# print(list(a))


# filter function 

# l1 = [1,2,3,4,5,6,7,8,9,10]
# # output : [2,4,6,8,10]

# l2=[]

# for i in l1:
#     if i % 2 == 0:
#         l2.append(i)
# print(l2)


# def fun(l1):
#     if l1 % 2 == 0:
#         return l1

# l1 = [1,2,3,4,5,6,7,8,9,10]

# a=filter(fun,l1)
# print(list(a))





