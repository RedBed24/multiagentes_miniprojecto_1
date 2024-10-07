from src.domain.scrape.people_scraper import get_description, get_born


def test_get_description():
    description = get_description("Barack_Obama")
    assert len(description) > 0
    assert "Barack" in description

def test_get_born():
    born = get_born("Barack_Obama")
    assert len(born) > 0
    assert "August" in born
