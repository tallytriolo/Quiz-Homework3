from quizComponents import vars

    # do some logic to see which character you selected

def total(value):
    if value == 160:
        vars.character = vars.characters[0]
    elif value == 230:
        vars.character = vars.characters[1]
    elif value == 340:
        vars.character = vars.characters[2]
    elif value == 460:
    	vars.character = vars.characters[3]

    print("It's " + vars.character)
        # add some emoji icons, or show the character image using the Pillow package
