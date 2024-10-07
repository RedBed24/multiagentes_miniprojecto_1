from src.domain import scrape
from src.domain.person import Person

def test_people_scraper():
    raw_people = scrape.list_scraper.get_top("People")
    assert raw_people
    assert len(raw_people) > 0

    people = list(map(lambda x: Person(id = x[1], name = x[0], born = scrape.people_scraper.get_born(x[1])), raw_people[:5]))
    assert people
    assert len(people) > 0
