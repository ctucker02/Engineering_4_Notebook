# Python Program 1 - Calculator
# Written by Caden Tucker

def doMath (num1, num2, operation):
# defines do math function
# program will need 2 numbers entered to do operation
	if operation == 1:
		x = round((num1 + num2), 2)	
		return str(x)
	if operation == 2:
		x = round((num1 - num2), 2)
		return str(x)
	if operation == 3:
		x = round((num1 * num2), 2)
		return str(x)
	if operation == 4:
		x = round((num1 / num2), 2)
		return str(x)
	if operation == 5:
		x = round((num1 % num2), 2)
		return str(x)
# the operation adds, subtracts, multiplies, divides, and finds remainder
go = "y"
# this sets the variable for the whileloop
print("After calculations is complete, press Enter to go again")
print("Press x then Enter to quit program")
# prints the instructions to work the calculator
while go == "y":
# starts calculator
	a = float(input("Enter 1st Number: "))
	b = float(input("Enter 2nd Number: "))
# user is told to put in the two numbers
	print("Sum:\t\t" + doMath(a,b,1))
	print("Difference:\t" + doMath(a,b,2))
	print("Product:\t" + doMath(a,b,3))
	print("Quotient:\t" + doMath(a,b,4))
	print("Modulo:\t\t" + doMath(a,b,5))
# program runs and finds all the answers to the functions
	key = input(" ")
	if key == "x":
# the user can end the program by pressing x then enter
		break	
 

