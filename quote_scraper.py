import requests
from bs4 import BeautifulSoup

quote_map = {
    "main": "Quote of the Day",
    "love": "Love Quote of the Day",
    "art": "Art Quote of the Day",
    "nature": "Nature Quote of the Day",
    "funny": "Funny Quote of the Day",
}


def get_quote(quote_type: str) -> (str, str):
    quote_soup = _get_quote_soup()
    for item in quote_soup:
        if item.h2.get_text() == quote_map[quote_type]:
            quote = item.find("a", class_="b-qt").get_text()
            author = item.find("a", class_="bq-aut").get_text()
    return (quote, author)


def _get_quote_soup() -> []:
    resp = requests.get("https://www.brainyquote.com/quote_of_the_day")
    assert resp.status_code == 200
    soup = BeautifulSoup(resp.text, features="html.parser")
    return soup.find_all(class_="qll-bg")
