from flask import Flask, render_template, request
from requests import get

from ..domain.person import Person
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
    ...
