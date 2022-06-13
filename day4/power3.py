#program4
number1 =int(input("Enter the first number"))
number2 =int(input("Enter the second number"))


def power(num1,num2):
  prod=1
  for x in range(num2):
     prod*=num1
  return prod
	
result=power(number1,number2)
print(result) 
