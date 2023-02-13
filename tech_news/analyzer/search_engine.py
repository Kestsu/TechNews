# import dateutil.parser
from tech_news.database import search_news
from tech_news.scraper import get_tech_news
from datetime import datetime


# Requisito 7
def search_by_title(title):  # N sei pq ta falhando
    list_all = search_news({"title": {"$regex": title.lower()}})
    list_tuple = []
    for dic in list_all:
        list_tuple.append((dic["title"], dic["url"]))

    return list_tuple

# inputs = [
#             "21-12-1980",
#             "2001-02-31",
#             "2020-31-02",
#             "1988-14-25",
#             "1997-02-31",
#         ]


# Requisito 8
def search_by_date(data):
    try:
        dia, mes, ano = data.split("-")
        # print(len(dia), mes, ano)
        diaMaior = int(dia) > 2
        mesMaior = int(mes) > 12
        if len(dia) == 2 & len(mes) == 2:
            if diaMaior > mesMaior:
                list_all = search_news({"timestamp": data.replace('-', '/')})
            elif diaMaior < mesMaior:
                list_all = search_news({"timestamp": data.replace('-', '/')})
            else:
                raise ValueError("Data inválida")
        else:
            data_formatada = datetime.strptime(
                data, "%Y-%m-%d").strftime("%d/%m/%Y")
            list_all = search_news({"timestamp": data_formatada})
        list_tuple = []
        for dic in list_all:
            list_tuple.append((dic["title"], dic["url"]))
        return list_tuple
    except ValueError:
        raise TypeError("Data inválida")


# Requisito 9
def search_by_category(category):
    # print(category.lower().title())
    list_all = search_news({"category": category.lower().title()})
    list_tuple = []
    for dic in list_all:
        list_tuple.append((dic["title"], dic["url"]))
    return list_tuple
    # return category


def popular_banco(date):
    get_tech_news(date)
