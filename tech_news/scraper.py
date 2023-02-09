import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
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
    links = "div.post-inner > div.entry-thumbnail > div > a ::attr(href)"
    return Selector(html_content).css(links).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    next_link = "nav > div > a.next.page-numbers ::attr(href)"
    return Selector(html_content).css(next_link).get()


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
