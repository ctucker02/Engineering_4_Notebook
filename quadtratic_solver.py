# Python Program 2 - Quadratic Solver
# Written by Caden Tucker

from math import sqrt
# imports square root function from  math module

roots = []
# creates a root function

def quadratic (a, b, c):
# defines the function
	disc = ((b ** 2) - (4*a*c))
# calculates the discriminant of the function
	if disc >= 0:
# if the discriminant is greater than or equal to 0, there will be at least 1  root
		roots.append (round(((-b + sqrt(disc)) / (2*a)), 2))
# finds the -b + root of the quadratic (if disc = 0, this root will be the same as the -b - root)
# rounded the root to decimal places
# added (appends) it to the roots array
	if disc > 0:
# if the discriminant is greater than 0 there will be 2 roots:
		roots.append (round(((-b - sqrt(disc)) / (2*a)), 2))

go = "y"
# sets the variable to start the while loop

print("After calculation is complete, press Enter to go again,")
print("press x then Enter to stop program")
# prints user instructions

while go == "y":
	a1 = float(input("Enter coefficient a: "))
	b1 = float(input("Enter coefficient b: "))
	c1 = float(input("Enter coefficient c: "))
# the user is told to enter the 3 variables of their quadratic
	quadratic (a1, b1, c1)
# program runs the quadratic function with the users variables
	numRoots = len(roots)
# counts the number of roots
	if numRoots == 0:
# if there are no roots
		print ("There are no real roots")
	if numRoots > 0:
# if there are roots
		print ("The roots are:")
		print (roots)
	roots.clear()
# this clears the roots so the program can run again
	key = input(" ")
# the program continues with user input
	if key == "x":
# user can press x to quit the program
		break
