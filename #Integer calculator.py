#Integer calculator
def add(num1,num2):
  return num1+num2
def subtract(num1,num2):
 return num1 - num2
def multiply(num1,num2):
  return num1 * num2    
def divide(num1, num2):
  return num1 / num2
print("pick an operation")
print("1 for add")
print("2 for subtraction") 
print("3 for Multiply") 
print("4 for divide")
oper=int(input("enter an operation: 1,2,3 or 4"))
number1=int(input("enter a number"))
number2=int(input("Enter another number"))
if oper == 1:
  print(number1,"+",number2,"=",add(number1,number2))
elif oper==2:
  print(number1,"-",number2,"=",subtract(number1,number2))
elif oper==3:
  print(number1,"*",number2,"=",multiply(number1,number2))
elif oper==4:
  print(number1,"/",number2,"=",divide(number1,number2)) 
else :
  print("invalid operation")  
