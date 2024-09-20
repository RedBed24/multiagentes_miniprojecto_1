"""This module contains functions to scrape the list of popular pages on Wikipedia."""

import requests
from bs4 import BeautifulSoup


def get_categories() -> list[str]:
    """Returns a list of categories of popular pages on Wikipedia.

    returns:
        list of categories
    """
    page = requests.get(
        f"https://en.wikipedia.org/wiki/Wikipedia:Popular_pages", timeout=5
    )
    soup = BeautifulSoup(page.content, "html.parser")

    main_content = soup.find("div", {"class": "mw-content-ltr"})
    found_category = main_content.find_all("div", {"class": "mw-heading"})

    categories = []
    # exclude non category headings
    for category in found_category:
        if category.get_text() in ["Sources", "See also", "References"]:
            continue
        categories.append(category.get_text())

    return categories


def get_top(category: str) -> list:
    """Returns a list of top pages in a given category.
    The list contains tuples with page title, id and number of views in millions.
    The category should be one of the categories in the popular pages list of Wikipedia.

    args:
        category: str - category of popular pages

    returns:
        list of tuples with page title, id and number of views
    """
    category_idx: int = get_categories().index(category)

    page = requests.get(
        f"https://en.wikipedia.org/wiki/Wikipedia:Popular_pages", timeout=5
    )
    soup = BeautifulSoup(page.content, "html.parser")

    main_content = soup.find("div", {"class": "mw-content-ltr"})
    table_rows = main_content.find_all("table", {"class": "wikitable"})[
        category_idx
    ].find_all("tr")

    # find index of page and views columns
    th = table_rows[0].find_all("th")
    page_idx = -1
    views_idx = -1
    for i, th in enumerate(th):
        if th.get_text() == "Page":
            page_idx = i
        if th.get_text() == "Views":
            views_idx = i

    # get the top pages in the format (title, link, views)
    # link is the string that goes after /wiki/ in the url
    top_pages = []
    for row in table_rows[1:]:
        td = row.find_all("td")
        link = td[page_idx].find("a").get("href").split("/")[-1]
        title = td[page_idx].get_text()[:-1]
        views = int(td[views_idx].get_text())
        top_pages.append((title, link, views))

    return top_pages
