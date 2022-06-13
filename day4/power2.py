#program3
number1 =int(input("Enter the first number"))
number2 =int(input("Enter the second number"))
def power(number1,number2):
multi = number1
for i in range(number2-1):
number1*= multi
return number1
result=power(number1,number2)
print(result)
