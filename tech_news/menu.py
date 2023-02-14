from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import search_by_title, search_by_date
from tech_news.analyzer.search_engine import search_by_category
from tech_news.analyzer.ratings import top_5_categories


# Requisitos 11 e 12
def analyzer_menu():
    response = input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por categoria;\n"
        " 4 - Listar top 5 categorias;\n"
        " 5 - Sair."
        )
    if response == "0":
        result = input("Digite quantas notícias serão buscadas:")
        get_tech_news(int(result))
    if response == "1":
        result = input("Digite o título:")
        print(search_by_title(result))
    if response == "2":
        result = input("Digite a data no formato aaaa-mm-dd:")
        print(search_by_date(result))
    if response == "3":
        result = input("Digite a categoria:")
        print(search_by_category(result))
    if response == "4":
        print(top_5_categories())
    if response == "5":
        print("Encerrando script")
        return
