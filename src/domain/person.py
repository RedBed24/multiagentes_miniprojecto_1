"""Module for the Person domain model."""

from pydantic import BaseModel
from sqlalchemy import Column, String

from ..persistance.creator import Base
from .scrape import people_scraper


class Person(BaseModel):
    """Class representing a person."""

    id: str
    name: str
    born: str

    def __repr__(self):
        return f"<Person(name='{self.name}', born='{self.born})>"

    def get_description(self) -> str:
        """Returns a description of the person."""
        return people_scraper.get_description(self.id)


# Shuoldn't this be in persistance/person? Cyclical imports?
class DBPerson(Base):
    """Class representing a person."""

    __tablename__ = "people"

    id = Column(String(50), primary_key=True)  # wikipedia /wiki/{id}
    name = Column(String(100), nullable=False)
    born = Column(String(100), nullable=False)

    def __repr__(self):
        return f"<Person(name='{self.name}', born='{self.born})>"

    def to_person(self) -> Person:
        """Converts the DBPerson to a Person."""
        return Person(id=self.id, name=self.name, born=self.born)


def get_all_people() -> list[Person]:
    """Returns all people."""
    dbpeople = Base.session.query(DBPerson).all()
    return list(map(lambda x: x.to_person(), dbpeople))


def get_person_by_id(person_id: str) -> Person:
    """Returns a person by id."""
    return Base.session.query(DBPerson).filter(DBPerson.id == person_id).first().to_person()


def update_person(person: Person) -> None:
    """Updates a person."""
    db_person = Base.session.query(DBPerson).filter(DBPerson.id == person.id).first()
    db_person.name = person.name
    db_person.born = person.born
    Base.session.commit()

def delete_person(person_id: str) -> None:
    """Deletes a person."""
    db_person = get_person_by_id(person_id)
    Base.session.delete(db_person)
    Base.session.commit()
