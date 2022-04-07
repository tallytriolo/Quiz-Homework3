from quizComponents.quizQuestions import questions
from quizComponents import vars, quizTally 

print("Welcome to the Marvel Quiz")
print("-----------------------------------------------------------------------")
print("  0000       0000                                             000      ")
print("  00000     00000    00000    00  00    0000   0000  000000   000      ")
print("  00 000   000 00        000   000'000   000   000  000  000  000      ")
print("  00  '00000'  00   000''000   00  00     00   00   00000000  000      ")
print("  00           00   000  000   00          00 00    000       000      ")
print(" 00000       00000   00000000  0000         000      000000  000000000 ")
print("-----------------------------------------------------------------------")

print("Answer the following questions! Or type to quit\n")

while start_quiz is True:

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

	answer7 = questions["q2"][input(questions["q2"]["question"])]
	print(answer7)

	vars.quizTotal += answer7
	print("+++++++++++\n")

	print("total so far: " + str(vars.quizTotal) + "\n")
	quizTally.total(vars.quizTotal)

	#after answer all the questions, figure out who your character is
	quizTally.total(vars.quizTotal)
