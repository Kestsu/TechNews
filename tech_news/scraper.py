import requests
import time
from parsel import Selector
import math
from tech_news.database import create_news


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
    url_schema = "head > link[rel = canonical] ::attr(href)"
    url = Selector(html_content).css(url_schema).get()
    title = Selector(html_content).css("div > h1.entry-title ::text").get()
    timestamp = Selector(html_content).css("ul > li.meta-date ::text").get()
    writer_schema = "li.meta-author > span.author > a ::text"
    writer = Selector(html_content).css(writer_schema).get()
    time_schema = "li.meta-reading-time ::text"
    #  Vai pegar so o primeiro elemento/ No caso so quero o numero
    time = Selector(html_content).css(time_schema).get().split()[0]
    summary_schema = "div.entry-content > p:nth-child(1) ::text"
    summary = ''.join(Selector(html_content).css(summary_schema).getall())
    if summary == '':
        summary_schema = "div.entry-content > p:nth-child(2) ::text"
        summary = ''.join(Selector(html_content).css(summary_schema).getall())
    category_sch = 'div.meta-category > a.category-style > span.label ::text'
    category = Selector(html_content).css(category_sch).get()
    return {
        "url": url,
        "title": title.strip(),  # remover espaço do final
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": int(time),
        "summary": summary.strip(),
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    res = fetch("https://blog.betrybe.com/")
    pages_need = 1
    links = []
    info_pages = []
    if amount > 12:
        pages_need = math.ceil(amount / 12)
    for quantity in range(pages_need):
        links.extend(scrape_updates(res))
        res = fetch(scrape_next_page_link(res))
    for url in links:
        info_pages.append(scrape_news(fetch(url)))
    create_news(info_pages[:amount])
    return info_pages[:amount]


if __name__ == "__main__":
    amount = input("Digite um numero: ")
    get_tech_news(int(amount))
