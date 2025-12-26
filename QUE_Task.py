



# # Task : 3 : Que Task 

# # Q1 : 10+10 
# # Q2 : 15-7
# # Q3 : 23*5
# # Q4 : 28/4
# # Q5 : 11*11
# # Q6 : 7**3
# # Q7 : 9//2
# # Q8 : 11==11
# # Q9 : 15>3
# # Q10 :27<56

# # ch a que number : 3
# # Q3 : 10*10 
# # A : 20
# # B : 30
# # C : 100
# # D : 200
# E : None

que = ["10+10","15-7","23*5","28/4","11*11","7**3","9//2","11==11","15>3","27<5"]
option = [{"A":10,"B":20,"C":30,"D":40,"E":None},
          {"A":8,"B":11,"C":5,"D":7,"E":None},
          {"A":125,"B":110,"C":115,"D":130,"E":None},
          {"A":9,"B":7,"C":14,"D":4,"E":None},
          {"A":121,"B":22,"C":110,"D":11,"E":None},
          {"A":49,"B":243,"C":21,"D":343,"E":None},
          {"A":4.5,"B":4,"C":5,"D":3,"E":None},
          {"A":10,"B":True,"C":11,"D":False,"E":None},
          {"A":15,"B":False,"C":True,"D":3,"E":None},
          {"A":5,"B":27,"C":True,"D":False,"E":None}]
ans = ["B","A","C","B","A","D","B","B","C","D"]

for i in range(len(que)):
    print(f"Q{i+1} : {que[i]}")    
number=1
b=0
asked=que

while number<=5:
    q_input = int(input("Enter A Q : "))
    if q_input<1 or q_input>len(que):
        print("Invalid Que")
        continue

    if q_input in asked:
        print("This question is already printed. Choose another.")
        continue

    asked.append(q_input)
    number+=1
    print(f"Q{q_input} : {que[q_input-1]}")
    for n in option[q_input-1].items():
            print(n)
        

    ans_input=str(input("Enter A Ans:"))
    if ans_input == ans[q_input-1]:
            print("Yes")
            b+=10
    else:
            print("No")     
            b-=5            
# else:
#     print("Invalid Que") 

print("total marks :",b)


            # b="Yes"
            # if b=="Yes":
            #     print(10)

# print(10)

# name = "mitul"
# age = 21
# print(name,age)

