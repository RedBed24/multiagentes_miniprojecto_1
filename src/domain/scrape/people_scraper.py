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


def get_born(id: str) -> str:
    """Returns the birth date of a person from Wikipedia given it's /wiki/{id}.

    args:
        id: str - id of the person on Wikipedia

    returns:
        str - birth date of the person
    """
    page = requests.get(f"https://en.wikipedia.org/wiki/{id}", timeout=5)
    soup = BeautifulSoup(page.content, "html.parser")

    table = soup.find("table", {"class": "vcard"}).find("tbody")

    trs = table.find_all("tr")
    born_idx = None
    for i, tr in enumerate(trs):
        th = tr.find("th")
        if th is None:
            continue
        th = th.get_text().lower()
        if "born" in th or "birth" in th:
            born_idx = i
            break

    return trs[born_idx].find("td").get_text()
