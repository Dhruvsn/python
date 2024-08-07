
# my_dict= {
#   'name': 'Alice',
#   'age' : 25,
#   'city' : 'New York'
# }

# # for key in my_dict:
# #     print(key)

# # print("")

# # for value in my_dict.values():
# #     print(value)

# for key,value in my_dict.items():
#     print(key,value)

# for key in my_dict.get(key):
#     print(key)

#-----------------------------------------------------------------------------------------------------------------

#WAP to perform the basic mathematical operation.
#I/p: A String with the methamatical expression
# O/p: result of the methamatical operation
#sample I/P : 2.5+3.6 | 2*6 | 9/3
#expected o/p : 6.1 | 12 | 3



# str = input("enter a mathematical expression:")
# print(eval(str))

# op= ''
# for i in str:
#    if i in '+-/*':
#     op = i
  

# operand = str.split(op) # return list of operand ex: [2,4]


# operand1 = float(operand[0])
# operand2 = float(operand[1])

# if op == '+':
#     result = operand1 + operand2
# elif op == '-':
#     result = operand1 - operand2
# elif op == '*':
#     result = operand1 * operand2

# elif op == '/':
#     result = operand1 / operand2
# else:
#     result = "Invalid operator"


# print(f"The result of the expression '{str}' is: {result}")

#---------------------------------------------------------------------------------------

# original_dict = {'S1':'A','S2':'B','S3':'A','S4':'A'}


# count_dict = {}

# for value in original_dict.values():
#     if value in count_dict.keys(): 
#         count_dict[value] += 1
#     else:
#         count_dict[value] = 1

# print("Value counts:", count_dict)

#----------------------------------------------------------------------------------------------------------------

#functions

# 4 important things of function: 
# 1.Name - Identifers
# 2 . return 
# 3. Parameters -> 
# 4.Defination

# syntax to write function
# def Name(parameter1, parameter2):
     # ......
    # return statement


# def addNumber(a,b):
#   c = a+b 
#   print(c)
#   return 

# if __name__ == "__main__":
#     addNumber(2,4)

# result = addNumber(2,3)
# print(result)

#------------------------------------------------------------------------------

# def addnum():
#    a = int(input("enter the first number: "))
#    b = int(input("enter the secon number: "))
#    c = a+b
#    print(c)
#    return

# if __name__ == "__main__":
#     addnum()

#------------------------------------------------------------------------------------------------
# import math

# def isprime(n):
#   if n <= 1:
#     return False
#   elif n == 2:
#      return True
#   elif n > 2 & n%2==0:
#      False
#   else:
#      for i in range(3, int(math.sqrt(n)) + 1, 2):
#         if n % i == 0:
#             return False 
     
   
#   return True


# if __name__ == "__main__":
   
#    n = int(input("Enter the number: "))
#    if isprime(n):
#      print(f"{n} is a prime number")
#    else:
#       print(f"{n} is not a prime number")


# def is_palindrome(number):
#   str_number = str(number)
#   reverse_str = ""
#   # reverse_str = str_number[::-1]
#   for char in str_number:
#       reverse_str = char + reverse_str

#   return str_number == reverse_str
      
# if __name__ == "__main__":

#  number = int(input("Enter the number: "))
# if is_palindrome(number):
#     print(f"{number} is a palindrome number")
# else:
#     print(f"{number} is not a palindrome number")

#-----------------------------------------------------------------------------------------------------
#class



class A:
   
  def __init__(self):
      self.a = 2

  def fun1(self):
       print("This is public function 1 frm class A")

  def _fun2_(self):
       print("This is protected function 2 from class A")


class B:
   
  def __init__(self):
      self.a = 3

  def fun3(self):
       print("This is public function 1 frm class B")

  def _fun4_(self):
       print("This is protected function 2 from class B")
    

class C:
   
  def __init__(self):
      self.a = 4

  def fun5(self):
       print("This is public function 1 frm class C")

  def _fun6_(self):
       print("This is protected function 2 from class C")
    

if __name__ =="__main__":

   obj = A()
   obj2 = B()
   obj3 = C()

   obj.fun1()
   obj._fun2_()

   obj2.fun1()
   obj2._fun2_()




      
     

