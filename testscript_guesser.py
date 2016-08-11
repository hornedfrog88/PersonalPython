import random
def main():
	randomnumber = random.randint(1,1000)
	TotNumberofGuesses = 1 
	Found = False
	while not Found:
		userGuess = int(input("Guess a number between 1 and 1000: "))
		if userGuess == randomnumber:
			print("YOU GUESSED IT!")
			Found = True
		elif userGuess > randomnumber:
			print("GUESS LOWER!")
			TotNumberofGuesses = TotNumberofGuesses+1		
		else:
			print ("GUESS HIGHER!")
			TotNumberofGuesses = TotNumberofGuesses+1
	print ("THE TOTAL NUMBER OF GUESSES IT TOOK: ",TotNumberofGuesses)		
	print ("THANK YOU FOR PLAYING THE GUESSING GAME")
main()