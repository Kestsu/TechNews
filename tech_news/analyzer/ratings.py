from tech_news.database import find_news


# Requisito 10
def top_5_categories():
    lista_de_categories = []
    contagem = {}
    for new in find_news():
        lista_de_categories.append(new["category"])
    if len(lista_de_categories) > 0:
        for category in lista_de_categories:
            contagem[category] = contagem.get(category, 0) + 1
        contagem_sort = sorted(contagem.items(), key=lambda x: (-x[1], x[0]))
        contagem_dict = list(dict(contagem_sort).keys())
        if len(contagem) > 5:
            return contagem_dict[:5]
        return contagem_dict
    return lista_de_categories
