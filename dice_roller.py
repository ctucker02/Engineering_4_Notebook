# Automatic Dice Roller
# Written By Caden Tucker
import random 
print ("Automatic Dice Roller")
val = input #value = your input
while val != "x": #will run intil x is pressed
    print("Press enter to roll and x to stop")
    val = input("") 
    if val == "x": #when x is pressed it stops running 
        quit()
    print (random.randint(1,6)) #prints a random number 1-6


