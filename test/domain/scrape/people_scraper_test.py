from src.domain.scrape.people_scraper import get_description


def test_get_description():
    description = get_description("Barack_Obama")
    assert len(description) > 0
    assert "Barack" in description
