#Defining function hangman
def hangman(word):
	wrong = 0
	stages = ["				  ",
             "_________       ",
             "|        |      ",
             "|        |      ",
             "|        0/     ",
             "|       /|      ",
             "|       / \     ",
             "|               "]
	rletters = list(word)
	board = ["__"] * len(word)
	win = False
	print("Welcome to Hangman...!!")
	while wrong < len(stages) - 1:
		print("\n")
		char = input("Guess a letter : ").lower()
		if char in rletters:
			cind = rletters.index(char)
			board[cind] = char
			rletters[cind] = '$'
		else:
			wrong += 1
		print((" ".join(board)))
		e = wrong + 1
		print("\n".join(stages[0: e]))
		if "__" not in board:
			print("You win..!!")
			print(" ".join(board))
			win = True
			break
	if not win:
		print("\n".join(stages[0:wrong]))
		print("You lose..!! It was",word)
 

hangman("lion")
while True:
	cinp=input('Do you want to try again ? (y/n) :').lower()
	if cinp=='n':
		break
	elif cinp=='y':
		hangman("lion")
	else:
		print("\n>>Error..!! Enter correct input (y/n)<<\n")