import requests
from bs4 import BeautifulSoup


def get_quote(quote_type: str) -> (str, str):
    quote_soup = get_quote_soup()
    for item in quote_soup:
        if item.h2.get_text() == quote_type:
            quote = item.find("a", class_="b-qt").get_text()
            author = item.find("a", class_="bq-aut").get_text()
    return (quote, author)


def get_quote_soup() -> []:
    resp = requests.get("https://www.brainyquote.com/quote_of_the_day")
    assert resp.status_code == 200
    soup = BeautifulSoup(resp.text, features="html.parser")
    return soup.find_all(class_="qll-bg")
