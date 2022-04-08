from components import vars
from PIL import Image

def total(value):
    if value == 160:
        vars.character = vars.characters[0]
        im = Image.open("images/captain.jpeg")
        im.show()
    elif value == 230:
        vars.character = vars.characters[1]
        im = Image.open("images/iron.jpeg")
        im.show()
    elif value == 340:
        vars.character = vars.characters[2]
        im = Image.open("images/spider.png")
        im.show()
    elif value == 460:
        vars.character = vars.characters[3]
        im = Image.open("images/hulk.jpeg")
        im.show()
    else:
        vars.character = "NONE OF THE CHARACTERS!!! =("

    print("IT'S " + vars.character)
