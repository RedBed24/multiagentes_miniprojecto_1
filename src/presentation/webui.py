from flask import Flask, redirect, render_template, request, url_for
from requests import get, put

from ..domain.person import Person
from . import API_URL

app = Flask(__name__)


@app.route("/")
def list_all():
    raw_people = get(API_URL).json()["people"]

    # Validate the data
    people = list(
        map(
            lambda x: Person(id=x["id"], name=x["name"], born=x["born"]),
            raw_people,
        )
    )
    return render_template("people.html", people=people)


@app.get("/<person_id>")
def get_person(person_id: str):
    person = get(f"{API_URL}/{person_id}").json()["person"]
    return render_template("person.html", person=person)


@app.post("/<person_id>")
def update_person(person_id: str):
    person = Person(
        id=person_id,
        name=request.form["name"],
        born=request.form["born"],
    )
    put(f"{API_URL}/{person_id}", data=person.model_dump_json())
    # Post/Redirect/Get pattern
    # to avoid resubmission of the form
    return redirect(url_for("get_person", person_id=person_id))
