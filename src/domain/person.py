from sqlalchemy import Column, Date, String

from ..persistance.creator import Base


class Person(Base):
    __tablename__ = "people"

    id = Column(String(50), primary_key=True)
    name = Column(String(100), nullable=False)
    birth_date = Column(Date, nullable=False)

    def __repr__(self):
        return f"<Person(name='{self.name}', birth_date='{self.birth_date}')>"
