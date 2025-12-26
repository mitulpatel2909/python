
#  1 condition syntax 

# if condition:
#     code

#  2 condition syntax

# if condition:
#     code
# else:
#     code    

#  3 condition syntax

# if condition:
#     code
# elif condition:
#     code
# elif condition:
#     code
# else:
#     code 
       
#  nested condition syntax

# if condition:
#     if condition:
#         if condition:
#             code
#         elif condition:
#             code
#     else:
#         code
# elif condition:
#     code
# else:
#     if condition:
#         code


# ================== 1 condition code ===============

# a=10
# if a==10:
#     print("Yes")


# a=10
# if a<=101:
#     print("Yes")


# a=10
# if a<=101 or a==102:
#     print("Yes")


# a=1,2,3,4,5,6,7,8,9,10
# if 100 in a:
#     print("Exists")



# ================== 2 condition code ===============

# a=101
# if a==10:
#     print("Yes")
# else:
#     print("No")    

# a=10
# if a==10 and a<=100:
#     print("Yes")
# else:
#     print("No") 

# a=1,2,3,4,5,6,7,8,9,10
# if 10 in a:
#     print("Exists")
# else:
#     print("Not Exists")



# ================== 3 condition code ===============

# a=5

# if a==10:
#     print("10 = 10")

# elif a<=15:
#     print("a <= 15")

# elif a>=16:
#     print("a >= 16")

# else:
#     print("No")



# age=int(input("Enter Your Age : "))
# if age>=1 and age<=6:
#     print("Age 1 To 6")
# elif age>=7 and age<=18:
#     print("Age 7 To 18")
# elif age>=19 and age<=50:
#     print("Age 19 To 50")
# elif age>=51 and age<=70:
#     print("Age 51 To 70")
# elif age>=71 and age<=100:
#     print("Age 71 to 100")
# elif age<=0:
#     print("Age 0 To Low")                
# else:
#     print("Age 100 To Up")                



# ================== nested condition code ===============


number=13

# if number>=1 and number<=20:
#     if number>=1 and number<=10:
#         print("Number 1 To 10")
#     else:
#         print("Number 11 To 20")
            

# elif number>=21 and number<=40:
#     if number>=21 and number<=30:
#         print("Number 21 To 30")
#     else:
#         print("Number 31 To 40")
    
# elif number>=41 and number<=60:
#     if number>=41 and number<=50:
#         print("Number 41 To 50")
#     else:
#         print("Number 51 To 60")    

# elif number>=61 and number<=80:
#      if number>=61 and number<=70:
#         print("Number 61 To 70")
#      else:
#         print("Number 71 To 80")
    
# elif number>=81 and number<=100:
#     if number>=81 and number<=90:
#         print("Number 81 To 90")
#     else:
#         print("Number 91 To 100")
    
# else:
#     print("Number 100 To Up")



# # ================== Task =================


# input 1 = 10
# input 2 = 20
# input 3 = 30
# input 4 = 40
# input 5 = 50

# 150

# 30


# 91 - 100 = A+
# 81 - 90  = A
# 71 - 80 =  B+
# 61 - 70 = B
# 51 - 60 = C
# 35 - 50 = D
# 35 to low = fail



# number1=int(input("Enter A Number 1 : "))
# number2=int(input("Enter A Number 2 : "))
# number3=int(input("Enter A Number 3 : "))
# number4=int(input("Enter A Number 4 : "))
# number5=int(input("Enter A Number 5 : "))
# # print(number1)
# print(number1+number2+number3+number4+number5)

# a = number1+number2+number3+number4+number5

# print(a/5)

# b = a/5


# if b>=35 and b<=50:
#     print("d")

# elif b>=51 and b<=60:
#     print("c")

# elif b>=61 and b<=70:
#     print("b")

# elif b>=71 and b<=80:
#     print("b+")

# elif b>=81 and b<=90:
#     print("a")

# elif b>=91 and b<=100:
#     print("a+")

# else:
#     print("fail")












