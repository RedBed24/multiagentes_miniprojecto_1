"""Module for the Person domain model."""

from sqlalchemy import Column, Date, String

from ..persistance.creator import Base
from .scrape import people_scraper


class Person(Base):
    """Class representing a person."""

    __tablename__ = "people"

    id = Column(String(50), primary_key=True)  # wikipedia /wiki/{id}
    name = Column(String(100), nullable=False)
    born = Column(String(100), nullable=False)

    def __repr__(self):
        return f"<Person(name='{self.name}', born='{self.born})>"

    def get_description(self) -> str:
        """Returns a description of the person."""
        return people_scraper.get_description(self.id)


def get_all_people() -> list[Person]:
    """Returns all people."""
    return Base.session.query(Person).all()

def get_person_by_id(person_id: str) -> Person:
    """Returns a person by id."""
    return Base.session.query(Person).filter(Person.id == person_id).first()
