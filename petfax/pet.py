from flask import (Blueprint, render_template, request, redirect)
import json
from . import models

pets = json.load(open('pets.json', encoding="utf-8"))
#print(pets)

bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route("/", methods=["GET","POST"])
def index():
    if request.method == 'POST':
        pet_name = request.form["petName"]
        pet_photo = request.form["petPhoto"]
        pet_fact= request.form["petFact"]

        new_pet = models.Pet(
            pet_name = pet_name, 
            pet_photo= pet_photo, 
            pet_fact=pet_fact)
        models.db.session.add(new_pet)
        models.db.session.commit()

        return redirect('/pets')

    results = models.Pet.query.all()

    return render_template('pets/index.html', pets=results)

@bp.route("/<int:id>")
def show(id):
    pet = models.Pet.query.get(id)
    return render_template('pets/show.html', pet = pet)

@bp.route("/new")
def new():
    return render_template('pets/new.html')