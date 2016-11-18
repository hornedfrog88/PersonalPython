import random
def main():
    x = 1
    y = 25
    randomnumber = random.randint(x,y)
    TotNumberofGuesses = 1 
    Found = False
    while not Found:
        userGuess = input("Guess a number between "+str(x)+" and "+str(y)+"   ");
        if int(userGuess) == randomnumber:
            print("YOU NAILED IT!")
            Found = True
            
        elif int(userGuess) > randomnumber:
            print("GUESS LOWER!")
            TotNumberofGuesses = TotNumberofGuesses+1		
        else:
            print ("GUESS HIGHER!")
            TotNumberofGuesses = TotNumberofGuesses+1
    print ("THE TOTAL NUMBER OF GUESSES IT TOOK: ",TotNumberofGuesses)
    print()
    print ("THANK YOU FOR PLAYING THE GUESSING GAME!!!!!!")
main()