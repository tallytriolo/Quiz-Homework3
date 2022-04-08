import emoji
from components.quizQuestions import questions
from components import vars, quizTally
from colorama import init, Fore, Style, Back

init()
print("                                                                       ")
print(Fore.CYAN + ">>>>>>>>>>>>>>>>>>>> Welcome to the Marvel Quiz <<<<<<<<<<<<<<<<<<<<<<<")
print(Style.RESET_ALL)
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
print(Fore.YELLOW + "Think one of the Marvel characters in this list below\n and answer the questions with > yes < or > no <.\n At the end your character will appear. Enjoy! =) \n")
print(Style.RESET_ALL)
print(Back.RED + "__________________________ Captain America ____________________________")
print(Style.RESET_ALL)
print(Back.BLUE + "______________________________ Iron Man _______________________________")
print(Style.RESET_ALL)
print(Back.YELLOW + "_____________________________ Spider-man ______________________________")
print(Style.RESET_ALL)
print(Back.GREEN + "________________________________ Hulk _________________________________")
print(Style.RESET_ALL)
print("                                                                       ")
print("Let's play: \n")
print(Style.RESET_ALL)

while vars.start is True:

	answer1 = questions["q1"][input(questions["q1"]["question"])]
	print(answer1)

	vars.quizTotal += answer1
	result = emoji.emojize(':star:')
	print(result)
	print(Fore.CYAN + "__________________________________________________\n")
	print(Style.RESET_ALL)

	answer2 = questions["q2"][input(questions["q2"]["question"])]
	print(answer2)

	vars.quizTotal += answer2
	result = emoji.emojize(':star:'':star:')
	print(result)
	print(Fore.CYAN + "__________________________________________________\n")
	print(Style.RESET_ALL)

	answer3 = questions["q3"][input(questions["q3"]["question"])]
	print(answer3)

	vars.quizTotal += answer3
	result = emoji.emojize(':star:'':star:'':star:')
	print(result)
	print(Fore.CYAN + "__________________________________________________\n")
	print(Style.RESET_ALL)

	answer4 = questions["q4"][input(questions["q4"]["question"])]
	print(answer4)

	vars.quizTotal += answer4
	result = emoji.emojize(':star:'':star:'':star:'':star:')
	print(result)
	print(Fore.CYAN + "__________________________________________________\n")
	print(Style.RESET_ALL)

	answer5 = questions["q5"][input(questions["q5"]["question"])]
	print(answer5)

	vars.quizTotal += answer5
	result = emoji.emojize(':star:'':star:'':star:'':star:'':star:')
	print(result)
	print(Fore.CYAN + "__________________________________________________\n")
	print(Style.RESET_ALL)

	answer6 = questions["q6"][input(questions["q6"]["question"])]
	print(answer6)

	vars.quizTotal += answer6
	result = emoji.emojize(':star:'':star:'':star:'':star:'':star:'':star:')
	print(result)
	print(Fore.CYAN + "__________________________________________________\n")
	print(Style.RESET_ALL)

	answer7 = questions["q7"][input(questions["q7"]["question"])]
	print(answer7)

	vars.quizTotal += answer7
	result = emoji.emojize(':star:'':star:'':star:'':star:'':star:'':star:'':star:')
	print(result)
	print(Fore.CYAN + "__________________________________________________\n")
	print(Style.RESET_ALL)

	print(Fore.RED + "YOUR FINAL SCORE: " + str(vars.quizTotal))
	quizTally.total(vars.quizTotal)
	print(Style.RESET_ALL)

	print(Fore.CYAN + "Would you like to start the Marvel Quiz again?\n")
	print(Style.RESET_ALL)
	choice = input("Y / N?")
	if choice == "N" or choice == "n":
		print(Fore.YELLOW + "Quiz end for you!")
		print(Style.RESET_ALL)
		exit()
	elif choice == "Y" or choice == "y":
		vars.quizTotal = 0
		vars.character = None
