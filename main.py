from taipy.gui import Gui

animal_list = ["Dog", "Cat", "Rabbit", "Hamster", "Horse", "Bird", "Snake", "Turtle", "Fish", "Lizard"]
selected_animal = ""

color_list = ["Red", "Green", "Blue", "Yellow", "Black", "White", "Purple", "Orange", "Pink", "Brown"]
selected_colors = []

page = """
# Pet Name Generator

<|{selected_animal}|selector|lov={animal_list}|type=str|adapter={lambda u: u}|dropdown|>

<|{selected_colors}|selector|lov={color_list}|type=str|adapter={lambda u: u}|multiple|>

<|Generate Names|button|on_action|>

"""
print(selected_colors)

Gui(page).run(use_reloader=True)
