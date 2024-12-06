from flask import Flask
from models.dog import Dog
from models.cat import Cat
from models.boa import Boa
from models.ferret import Ferret

app = Flask(__name__, template_folder="views")

@app.route("/sound/<animal>")
def sound(animal: str):
    if animal == "dog":
        return Dog.make_sound()
    elif animal == "cat":
        return Cat.make_sound()
    elif animal == "boa":
        return Boa.make_sound()
    elif animal == "ferret":
        return Ferret.make_sound()
    else:
        return "El animal debe ser: dog, cat, boa o ferret."