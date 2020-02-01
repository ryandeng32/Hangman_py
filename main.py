import random

def generate_the_word(infile):
    with open(infile) as f:
        contents_of_file = f.read()
    lines = contents_of_file.splitlines()
    line_number = random.randrange(0, len(lines))
    return lines[line_number]

def display(score):
	print(f"The word is currently: ",end = "")
	for char in secret: 
		if char in guessed_word: 
			print(f'{char}', end = "")
		else:
			print("-", end = "")
	print()
	if score == 0:
		print('''
  +---+
  |   |
      |
      |
      |
      |
=========''')			
	elif score == 1:
		print('''
  +---+
  |   |
  0   |
      |
      |
      |
=========''')
	elif score == 2:
		print('''
  +---+
  |   |
  0   |
  |   |
      |
      |
=========''')
	elif score == 3:
		print('''
  +---+
  |   |
  0   |
 /|   |
      |
      |
=========''')
	elif score == 4:
		print('''
  +---+
  |   |
  0   |
 /|\  |
      |
      |
=========''')
	elif score == 5:
		print('''
  +---+
  |   |
  0   |
 /|\  |
  |   |
      |
=========''')
	elif score == 6:
		print('''
  +---+
  |   |
  0   |
 /|\  |
  |   |
 /    |
=========''')
	elif score >= 7:
		print('''
  +---+
  |   |
  0   |
 /|\  |
  |   |
 / \  |
=========''')

def cls():
	print('\n' * 100)

def complete(secret, guessed_word):
	isComplete = True
	for i in secret: 
		if i not in guessed_word: 
			isComplete = False
	return isComplete
	

replay = True
while replay:
	# variable initialization 
	score = 0
	isPlaying = True
	secret = generate_the_word("words.txt")
	guessed_word = []
	other_word = []
		
	
	cls()
	while isPlaying:
		display(score)
		if score >= 20:
			print("You Lost!")
			print(f"The secret word is {secret}")
			break
		guess = input("Please enter your guess -> ")
		cls()
		if guess in guessed_word or guess in other_word:
			print("You already guessed that!")
			continue
		else:
			if guess in secret: 
				guessed_word.append(guess)
			else:
				other_word.append(guess)
				score += 1
		if complete(secret, guessed_word):
			display(score)
			print("You Won!")
			print("棒棒～")
			break
	
	char = input("Enter y to replay, n to exit")
	if char != "y": 
		replay = False
	


cls()
print("Goodbye~")
print("Ryan 💕💕💕❤️🧡💛❤️🧡💛💞💓💗💘💖💝🥰😍😘 Ying")
		
	
		
