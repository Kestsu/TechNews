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
    # Vai calcular quantas paginas serão necessarias
    if amount > 12:
        pages_need = math.ceil(amount / 12)
    #  Vai acessas todas as paginas e salvar todos os links em uma so lista
    for quantity in range(pages_need):
        links.extend(scrape_updates(res))
        res = fetch(scrape_next_page_link(res))
    #  Vai entrar em todos os links, pegas as info e depois salvar na lista
    for url in links:
        info_pages.append(scrape_news(fetch(url)))
    #  Vai salvar no banco so a quantidade pedida
    create_news(info_pages[:amount])
    #  Vai retornar so a quantidade que pediu
    return info_pages[:amount]


# def get_tech(amount):
#     count_notices = 0
#     next_count = 0
#     list_dict = []
#     # while amount < count_notices:
#     html_content = fetch("https://blog.betrybe.com/")
#     page_notices = scrape_updates(html_content)
#     count_notices += len(page_notices)
#     next_page = scrape_next_page_link(html_content)
#     for index in range(0, amount):
#         if index <= 11:
#             dict_notices = scrape_news(fetch(page_notices[index]))
#             list_dict.append(dict_notices)
#         if index >= 12:
#             if next_count >= 12:
#                 next_count = 0
#             next_html = fetch(next_page)
#             next_notices = scrape_updates(next_html)
#             dict_notices = scrape_news(fetch(next_notices[next_count]))
#             list_dict.append(dict_notices)
#             next_count += 1

#     # print(len(list_dict[:amount]))
#     # create_news(list_dict[:amount])
#     return list_dict[:amount]


# if __name__ == '__main__':
#     a = get_tech(20)
#     b = get_tech_news(20)


# if __name__ == "__main__":
#     amount = input("Digite um numero: ")
#     get_tech_news(int(amount))
