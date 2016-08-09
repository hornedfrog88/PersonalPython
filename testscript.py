def add(num1,num2):
	return num1+num2
def sub(num1,num2):
	return num1-num2
def mul(num1,num2):
	return num1*num2
def div(num1,num2):
	return num1/num2
######################
def main():
	operator = input("What is your operator +, -, *, /?")
	if operator not in ('+','-','*','/'):
		print("YOU MUST CHOOSE A VALID OPERATOR")
	else:
		var1 = int(input("Enter first value"))
		var2 = int(input("Enter second value"))
		if operator == '+':
			print(add(var1,var2))
		elif operator == '-':
			print(sub(var1,var2))
		elif operator == '*':
			print(mul(var1,var2))
		else:
			print(div(var1,var2))
			
			
	
		

main()