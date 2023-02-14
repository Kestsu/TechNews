from tech_news.database import find_news


# Requisito 10
def top_5_categories():
    lista_de_categories = []
    contagem = {}
    for new in find_news():
        lista_de_categories.append(new["category"])

    for category in lista_de_categories:
        contagem[category] = contagem.get(category, 0) + 1
    result = sorted(contagem, key=lambda x: (contagem[x], x), reverse=True)

    return result


if __name__ == "__main__":
    # amount = input("Digite um numero: ")
    # get_tech_news(15)
    print(top_5_categories())
