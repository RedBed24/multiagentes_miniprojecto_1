from src.domain.scrape.list_scraper import get_categories, get_top


def test_get_categories():
    categories = list(get_categories())
    assert len(categories) > 0
    assert "Sources" not in categories
    assert "See also" not in categories
    assert "References" not in categories


def test_get_top():
    top = get_top("People")
    assert len(top) > 0
