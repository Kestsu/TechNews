from tech_news.database import search_news
from tech_news.scraper import get_tech_news
# import datetime


# Requisito 7
def search_by_title(title):  # N sei pq ta falhando
    list_all = search_news({"title": {"$regex": title.lower()}})
    list_tuple = []
    for dic in list_all:
        list_tuple.append((dic["title"], dic["url"]))

    return list_tuple


# Requisito 8
def search_by_date(date):
    try:  # n ta funcionando a query
        # data_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
        # date_formatted = data_obj.date()
        list_all = search_news({"timestamp": {f"$eq: new Date({date})"}})

        return list_all
        # list_tuple = []
        # for dic in list_all:
        # list_tuple.append((dic["title"], dic["url"]))
        # return list_tuple
    except ValueError:
        return "Data inválida"


# Requisito 9
def search_by_category(category):
    list_all = search_news({"category": category})
    list_tuple = []
    for dic in list_all:
        list_tuple.append((dic["title"], dic["url"]))
    return list_tuple


def popular_banco(date):
    get_tech_news(date)
