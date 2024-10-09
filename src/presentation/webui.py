from flask import Flask, redirect, render_template, request, url_for
from requests import get

from ..domain.person import Person, update_db_person
from ..domain.scrape.list_scraper import get_top
from ..domain.scrape.people_scraper import get_born
from . import API_URL

app = Flask(__name__)


@app.route("/")
def list_all():
    # FIXME: raw_people = get(API_URL).json()["people"]
    raw_people = get_top("People")

    # Validate the data
    people = list(
        map(
            # FIXME: lambda x: Person(id=x["id"], name=x["name"], born=x["born"]),
            lambda x: Person(id=x[1], name=x[0], born=get_born(x[1])),
            raw_people,
        )
    )
    return render_template("people.html", people=people)


@app.get("/<person_id>")
def get_person(person_id: str):
    # FIXME: person = get(f"{API_URL}/{person_id}").json()["person"]
    person = Person(id=person_id, name="John Doe", born="01-01-1970")
    return render_template("person.html", person=person)


@app.post("/<person_id>")
def update_person(person_id: str):
    person = Person(
        id=person_id,
        name=request.form["name"],
        born=request.form["born"],
    )
    update_db_person(person)
    # Post/Redirect/Get pattern
    # to avoid resubmission of the form
    return redirect(url_for("get_person", person_id=person_id))
