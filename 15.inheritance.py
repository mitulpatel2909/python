


# Inheritance in Python is a core principle of object-oriented programming (OOP) that allows a new class to inherit attributes and methods from an existing class.


# 1.  Single Inheritance : A child class inherits from a single parent class.

# 2. Multiple Inheritance : A child class inherits from multiple parent classes. Python uses a Method Resolution Order (MRO) to manage potential conflicts.

# 3. Multilevel Inheritance : A class inherits from a parent that already inherits from another parent.

# 4. Hierarchical Inheritance : Multiple child classes inherit from a single parent class.

# 5. Hybrid Inheritance : A combination of two or more inheritance types.


# 1.  Single Inheritance : 

# class A():
#     def display_A(self):
#         print("Class A")

# class B(A):
#     def display_B(self):
#         print("Class B")

# obj_b=B()
# obj_b.display_A()
# obj_b.display_B()



# 2. Multiple Inheritance :

# class A():
#     def display_A(self):
#         print("Class A")

# class B():
#     def display_B(self):
#         print("Class B")
# class C():
#     def display_C(self):
#         print("Class C")
# class D(A,B,C):
#     def display_D(self):
#         print("Class D")

# obj_d=D()
# obj_d.display_A()
# obj_d.display_B()
# obj_d.display_C()
# obj_d.display_D()



# 3. Multilevel Inheritance :

# class A():
#     def display_A(self):
#         print("Class A")
# class B(A):
#     def display_B(self):
#         print("Class B")
# class C(B):
#     def display_C(self):
#         print("Class C")
# class D(C):
#     def display_D(self):
#         print("Class D")

# obj_b=B()
# obj_b.display_A()
# obj_b.display_B()
# obj_c=C()
# obj_c.display_A()
# obj_c.display_B()
# obj_c.display_C()
# obj_d=D()
# obj_d.display_A()
# obj_d.display_B()
# obj_d.display_C()
# obj_d.display_D()


# 4. Hierarchical Inheritance :


# class A():
#     def display_A(self):
#         print("Class A")

# class B(A):
#     def display_B(self):
#         print("Class B")
# class C(A):
#     def display_C(self):
#         print("Class C")

# obj_b=B()
# obj_b.display_A()
# obj_b.display_B()
# obj_c=C()
# obj_c.display_A()
# obj_c.display_C()

# 5. Hybrid Inheritance :

# class A():
#     def display_A(self):
#         print("Class A")

# class B(A):
#     def display_B(self):
#         print("Class B")

# class C(B,A):
#     def display_C(self):
#         print("Class C")


# obj_b=B()
# obj_b.display_A()
# obj_b.display_B()
# obj_c=C()
# obj_c.display_A()
# obj_c.display_B()
# obj_c.display_C()

