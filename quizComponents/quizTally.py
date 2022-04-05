from components import vars

def total(value):
    # do some logic to see which character you selected

    if value <= 10:
        vars.character = vars.characters[0]

        print("It's " + vars.character)
        # add some emoji icons, or show the character image using the Pillow package
