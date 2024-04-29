# CALCULATOR_
#This is simple calculator for calculate Addition, Subtraction, Multiplication, division, Exponential
print("-----------------------------------Your most welcome to my own made calculator---------------------------------------")
b = input("--------------------------------Enter any symbol +,_,%,/,*-----------------------------------------------------------\n:-")


if b == "+":    #-------------------------------------------Addition
  a = int(input("Enter first input:-"))
  c = int(input("Enter second number:"))
  print(a, "+", c ,"=", a+c) 
elif b == "-":  #''''''''''''''''''''''---------------------------------Subtraction'''''
 a = int(input("Enter first input:-"))
 c = int(input("Enter second number:"))
 print(a, "-", c, "=", a - c)
elif b == "*":  #'''''''''''                 ---------------------------multiplication '''''
   a = int(input("Enter first input:-"))
   c = int(input("Enter second number:")) 
   print(a, "*", c ,"=", a*c)
elif b == "/": #'''''''--------------------------------------------------Division'''
  a = int(input("Enter first input:-"))
  c = int(input("Enter second number:")) 
  print(a, "/", c ,"=", a/c)
elif b == "%": #'''''---------------------------------Modulas'''''''''
  a = int(input("Enter first input:-"))
  c = int(input("Enter second number:")) 
 print(a, "%", c ,"=", a%c)
elif b == "**": 
  a = int(input("Enter first input:-"))
  c = int(input("Enter second number:")) 
  print(a, "**", c ,"=", a**c)
else : 
 print("You have entered wrong Symbol")
 


   







