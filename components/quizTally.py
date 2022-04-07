from components import vars

def total(value):
    if value == 160:
        vars.character = vars.characters[0]
    elif value == 230:
        vars.character = vars.characters[1]
    elif value == 340:
        vars.character = vars.characters[2]
    elif value == 460:
        vars.character = vars.characters[3]
    else:
        vars.character = "any of the characters!"

    print("It's " + vars.character)
