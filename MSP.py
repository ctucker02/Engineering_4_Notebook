import random
health = 5 #amount of health
letterInput = " "
word = ["cool", "soccer", "food", "crazy", "iphone", "water"] #options 
answer = word[random.randint(0,len(word)-1)] #picks random word above
answers = [] #guesses
win = None #end game
guess = 0 #correct guesses
letter=len(set(answer))
for x in range(len(answer)):
    answers.extend('_') 
print("Hangman")

def hangman(health):   #prints hangman shape
    if health==0:
        print("---0")
    if health==1:
        print("---0")
        print("   |")
    if health==2:
        print("---0")
        print("   |")
        print("   |")
    if health==3:
        print("---0")
        print("   |")
        print("   |")
        print(" --|--")
    if health==4:
        print("---0")
        print("   |")
        print("   |")
        print(" --|--")
        print("   |")
    if health==5:
        print("---0")
        print("   |")
        print("   |")
        print(" --|--")
        print("   |")
        print("  | |")


while health>0: 
    letterInput = input("Guess: ") #asks for guess
    if letterInput in answer: #checks if letter is correct
        print("Correct!")
        for x in range(len(answer)):
            if letterInput == answer[x]:
                answers[x] = letterInput
        print(answers)
        guess = guess + 1
        if guess == letter: #if all letters guessed you win
            win = True
            break
    else:   
        health = health-1 #subtracts health and asks to try again
        print("Incorrect, try again")
        print("You have " + str(health) + " health")
        hangman(health)

if win == True:
    print("You Won!")
else:
    print("You Lost")
