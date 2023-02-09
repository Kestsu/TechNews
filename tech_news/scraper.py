import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    headers = {"user-agent": "Fake user-agent"}
    try:
        time.sleep(1)
        res = requests.get(url, headers=headers, timeout=3)
        if res.status_code == 200:
            return res.text
        return None
    except requests.exceptions.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    res = fetch(html_content)
    selec = Selector(res)
    result = []
    a = "article > div > div:nth-child(1) > div > div > a ::attr(href)"
    for links in selec.css(a).getall():
        result.append(links)
    return result


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
