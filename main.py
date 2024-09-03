import requests
from bs4 import BeautifulSoup


def fetch_html(url):
    response = requests.get(url)
    response.raise_for_status()  # Will raise an HTTPError for bad requests
    return response.text


print(fetch_html("https://github.com/topics/django"))

