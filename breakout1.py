while True:
	word = str(input("Please enter a word in the sentence (enter . ! or ? to end.)"))
	sentence += word
	print('....current   ',sentence,sep=' ')
	if word in ('.','!','?'):
		break
	print('....current   ',sentence)