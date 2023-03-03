from tech_news.database import search_news
from tech_news.scraper import get_tech_news
from datetime import datetime


def search_by_title(title): 
    list_all = search_news({"title": {"$regex": title.lower()}})
    list_tuple = []
    for dic in list_all:
        list_tuple.append((dic["title"], dic["url"]))

    return list_tuple


def search_by_date(data):
    try:
        data_formatada = datetime.strptime(
            data, "%Y-%m-%d").strftime("%d/%m/%Y")
        list_all = search_news({"timestamp": data_formatada})
        list_tuple = []
        for dic in list_all:
            list_tuple.append((dic["title"], dic["url"]))
        return list_tuple
    except ValueError:
        raise ValueError("Data inválida")


def search_by_category(category):

    list_all = search_news({"category": category.lower().title()})
    list_tuple = []
    for dic in list_all:
        list_tuple.append((dic["title"], dic["url"]))
    return list_tuple


def popular_banco(date):
    get_tech_news(date)
