"""Module to scrape Wikipedia for a person's information."""

import requests
from bs4 import BeautifulSoup


def get_description(id: str) -> str:
    """Returns a description of a person from Wikipedia given it's /wiki/{id}.

    args:
        id: str - id of the person on Wikipedia

    returns:
        str - description of the person
    """
    page = requests.get(f"https://en.wikipedia.org/wiki/{id}", timeout=5)
    soup = BeautifulSoup(page.content, "html.parser")

    main_content = soup.find("div", {"class": "mw-content-ltr"})
    return main_content.find_all("p")[1].get_text()
