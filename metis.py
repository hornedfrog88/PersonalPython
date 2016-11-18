import random
secret_number = random.randint(0,100) 
guess = -1 
nbrofguesses = 1    
while (secret_number != guess) and (nbrofguesses <= 10): 
    guess = int(input("Guess a number between 0 and 100: "))   
    if guess < secret_number:   
        print("your guess is low")    
    elif guess > secret_number:    
        print("your guess is high")   
    else:  
        print("you guessed right!")   
    nbrofguesses = nbrofguesses+1 

