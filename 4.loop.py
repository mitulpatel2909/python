


# loop type : 

# 1 : for loop
# 2 : while loop  


# 1 : for loop syntax

# for variable_name in range(start_number,end_number,step_number):
#     code


# 2 : while loop syntax

# variable_name=start_number

# while variable_name<=end_number:
#     code
#     variable_name+=1/variable_name-=1


# ====================== for loop ==================

# for i in range(1,11):
#     print("Hello")

# ========

# 1 To 10 print

# for i in range(1,11):
    # print(i)

# ========


# hello - 1
# hello - 2

# for i in range(1,11):
#     print("Hello",i)

# ========


# without start_number provide time start_number is 0

# for i in range(11):
#     print(i)


# ========

# number=10

# for i in range(1,number+1):
#     print(i)


# ========

# number=int(input("Enter A Number : "))

# for i in range(1,number+1):
#     print(i)


# ========

# step number

# for i in range(1,11,3):
#     print(i)

# ========

# 10 to 1 print

# for i in range(10,0,-1):
#     print(i)

# ========

# f function 


# name="mitul"
# age=20
# # ouput : my name is mitul and my age is 20
# print(f"my name is {name} and my age is {age}")


# ============

# # end = " " function

# a=10
# b=20

# print(a,end=" ")
# print(b,end=" ")
# print(b)

# ===================

# multipication table 


# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 3 = 15
# 5 * 4 = 20
# 5 * 5 = 25
# 5 * 6 = 30
# 5 * 7 = 35
# 5 * 8 = 40
# 5 * 9 = 45
# 5 * 10 = 50

# number=int(input("Enter A Number : "))
# for i in range(1,11):
#     print(f"{number} * {i} = {number*i}")


# =========

# Break

# for i in range(1,11):
#     if i==6:
#         break
#     print(i)

  
# continue

# for i in range(1,11):
#     if i==5 or i==8:
#         continue
#     print(i)

# pass

# for i in range(1,11):
#     pass




# ============

# nested for loop

# for variable_name_a in range(start_number,end_number,step):
#     for variable_name_b in range(start_number,end_number,step):
#         code
#     print()



# for i in range(1,6):
#     for n in range(1,11):
#        print(f"{i} * {n} = {i*n}")



"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *

"""

# for i in range(1,6):
#     for n in range(1,6):
#         print("*",end=" ")
#     print()    


"""
* * * * *
*       *
*       *
*       *
* * * * *

"""

# for i in range(1,6):
#     for n in range(1,6):
#         if i==1 and (n>=1 or n<=5):
#             print("*",end=" ")
#         elif i==5 and (n>=1 or n<=5):
#             print("*",end=" ")
#         elif i==2 and (n==1 or n==5):
#             print("*",end=" ")    
#         elif i==3 and (n==1 or n==5):
#             print("*",end=" ")  
#         elif i==4 and (n==1 or n==5):
#             print("*",end=" ")  
#         else:
#             print(" ",end=" ")

#     print()    


# task : 1 

# input_1 = 20
# input_2 = 30
# 20,21,22,23,24.....30


# task : 2

# find even and odd number inside 1 to 20

# ouput  : odd number - 1
# ouput  : even number - 2
# .
# .
# .
# .
# ouput  : even number - 20

# task : 3 

"""

* * * * *
*   *   *
* * * * *
*   *   *
* * * * * 

"""

# task : 4

"""
*       *
* *   * *
*   *   * 
*       *
*       *

"""


# ======= task 1 code ==========


# number1=int(input("Enter A Number 1 : "))
# number2=int(input("Enter A Number 2 : "))

# for i in range(number1,number2+1):
#     print(i)


# ========= task 2 code ==========


# for i in range(1,20):
#     if i%2 == 0:
#      print(f"{i} even")
     
#     else:
#      print(f"{i} odd") 


# ========= task 3 code =========


# for i in range(1,6):
#     for n in range(1,6):
#         if i==1 and (n>=1 or n<=5):
#             print("*",end=" ")
#         elif i==5 and (n>=1 or n<=5):
#             print("*",end=" ")
#         elif i==2 and (n==1 or n==3 or n==5):
#             print("*",end=" ")    
#         elif i==3 and (n>=1 or n<=5):
#             print("*",end=" ")  
#         elif i==4 and (n==1 or n==3 or n==5):
#             print("*",end=" ")  
#         else:
#             print(" ",end=" ")

#     print()   


# ========== task 4 code ==========


# for i in range(1,6):
#     for n in range(1,6):
#         if i==1 and (n==1 or n==5):
#             print("*",end=" ")
#         elif i==5 and (n==1 or n==5):
#             print("*",end=" ")
#         elif i==2 and (n==1 or n==2 or n==4 or n==5):
#             print("*",end=" ")    
#         elif i==3 and (n==1 or n==3 or n==5):
#             print("*",end=" ")  
#         elif i==4 and (n==1 or n==5):
#             print("*",end=" ")  
#         else:
#             print(" ",end=" ")

#     print() 


# ======================================================

# ====================== while loop ==================


# 1 to 10 print

# i=1
# while i<=10:
#     print(i)
#     i+=1

# step number

# i=1
# while i<=10:
#     print(i)
#     i+=3


# 10 to 1 print

# i=10
# while i>=1:
#     print(i)
#     i-=1


# multipicaton table


"""
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50
"""

# i=1
# number=int(input("Enter A Number : "))

# while i<=10:
#     print(f"{number} * {i} = {number*i}")
#     i+=1


# nested while loop 

# i=11
# while i<=20:
#     n=1
#     while n<=10:
#         print(f"{i} * {n} = {i*n}")
#         n+=1
#     i+=1
#     print()    



"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""
# i=1
# while i<=5:
#     n=1
#     while n<=5:
#         print("*",end=" ")
#         n+=1
#     i+=1
#     print()    


# ====

i=True

while i:
    print("Yes")
    ch=input("Y For Yes And N for No(stop) : ")
    if ch == "Y":
        i=True
    elif ch == "N":
        i=False
    else:
         print("Invalid Input")        



