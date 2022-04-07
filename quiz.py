import emoji
from components.quizQuestions import questions
from components import vars, quizTally
from colorama import init, Fore, Style

init()
print("                                                                       ")
print(Fore.CYAN + ">>>>>>>>>>>>>>>>>>>> Welcome to the Marvel Quiz <<<<<<<<<<<<<<<<<<<<<<<")
print(Style.RESET_ALL)
result = emoji.emojize(':thumbs_up:')
print(result)
print("                                                                       ")
print(Fore.RED + "  0000       0000                                             000      ")
print("  00000     00000    00000    00  00    0000   0000  000000   000      ")
print("  00 000   000 00        000   000 000   000   000  000  000  000      ")
print("  00   00000   00   00000000   00  00     00   00   00000000  000      ")
print("  00           00   000  000   00          00 00    000       000      ")
print(" 00000       00000   00000000  0000         000      000000  000000000 ")
print(Style.RESET_ALL)
print("                                                                       ")
print("                                                                       ")
print("Think of one of the Marvel characters in this list below\n")
print("and answer the questions > yes < or > no <\n")
print("At the end your character will appear. Enjoy!\n")
print("                                                                       ")
print("__________________________ Captain America ____________________________")
print("______________________________ Iron Man _______________________________")
print("_____________________________ Spider-man ______________________________")
print("________________________________ Hulk _________________________________")
print("                                                                       ")

while vars.start is True:

	print("If you want to give up the game, type > quit < to exit the Marvel quiz.\n")

	vars.start = input("Type any key to start \n")

	if vars.start == "quit":
		print("Your chose to quit! See you next time!")
		exit()

	print("Let's play: ")
	print("\n")

	answer1 = questions["q1"][input(questions["q1"]["question"])]
	print(answer1)

	vars.quizTotal += answer1
	print("+++++++++++\n")

	answer2 = questions["q2"][input(questions["q2"]["question"])]
	print(answer2)

	vars.quizTotal += answer2
	print("+++++++++++\n")

	answer3 = questions["q3"][input(questions["q3"]["question"])]
	print(answer3)

	vars.quizTotal += answer3
	print("+++++++++++\n")

	answer4 = questions["q4"][input(questions["q4"]["question"])]
	print(answer4)

	vars.quizTotal += answer4
	print("+++++++++++\n")

	answer5 = questions["q5"][input(questions["q5"]["question"])]
	print(answer5)

	vars.quizTotal += answer5
	print("+++++++++++\n")

	answer6 = questions["q6"][input(questions["q6"]["question"])]
	print(answer6)

	vars.quizTotal += answer6
	print("+++++++++++\n")

	answer7 = questions["q7"][input(questions["q7"]["question"])]
	print(answer7)

	vars.quizTotal += answer7
	print("+++++++++++\n")

	print("total so far: " + str(vars.quizTotal))
	quizTally.total(vars.quizTotal)

	print("Would you like to start the Marvel Quiz again?\n")
	choice = input("Y / N?")
	if choice == "N" or choice == "n":
		print("End of the quiz for you!")
		exit()
	elif choice == "Y" or choice == "y":
		vars.quizTotal = 0
		vars.character = None
