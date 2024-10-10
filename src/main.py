import logging

from fastapi import FastAPI

from .domain.person import (
    DBPerson,
    Person,
    get_all_people,
    get_person_by_id,
    update_db_person,
    delete_person,
)
from .domain.scrape.list_scraper import get_top
from .domain.scrape.people_scraper import get_born
from .persistance.creator import Base, create_database
from .persistance.initializator import initialize_database


def main():
    try:
        create_database()
        initialize_database()
        raw_people = get_top("People")
        # Validate the data
        people = list(
            map(
                lambda x: Person(id=x[1], name=x[0], born=get_born(x[1])),
                raw_people,
            )
        )
        dbpeople = list(
            map(
                lambda x: DBPerson(id=x.id, name=x.name, born=x.born),
                people,
            )
        )
        Base.session.add_all(dbpeople)
    except Exception as e:
        logging.error(e)
        exit(1)


app = FastAPI(
    on_startup=[main],
    on_shutdown=[lambda: Base.session.close()],
)


# FIXME: PERSON ID NOT FOUND???

@app.get("/people")
async def people() -> dict:
    return {"people": get_all_people()}


@app.get("/people/{person_id}")
async def get_person(person_id: str) -> dict:
    return {"person": get_person_by_id(person_id)}


@app.put("/people/{person_id}")
async def put_person(person_id: str, person: Person) -> dict:
    assert person.id == person_id
    update_db_person(person)
    return {"person": person}


@app.delete("/people/{person_id}")
async def delete_person(person_id: str) -> dict:
    delete_person(person_id)
    return {}
