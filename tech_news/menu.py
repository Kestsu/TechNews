import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import search_by_title, search_by_date
from tech_news.analyzer.search_engine import search_by_category
from tech_news.analyzer.ratings import top_5_categories


def zero():
    result = input("Digite quantas notícias serão buscadas:")
    get_tech_news(int(result))


def one():
    result = input("Digite o título:")
    print(search_by_title(result))


def two():
    result = input("Digite a data no formato aaaa-mm-dd:")
    print(search_by_date(result))


def three():
    result = input("Digite a categoria:")
    print(search_by_category(result))


def four():
    print(top_5_categories())


def five():
    print("Encerrando script")
    return


def analyzer_menu():
    response = input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por categoria;\n"
        " 4 - Listar top 5 categorias;\n"
        " 5 - Sair.\n"
        " "
    )
    try:
        dict_options = {
            "0": zero,
            "1": one,
            "2": two,
            "3": three,
            "4": four,
            "5": five,
        }
        dict_options[response]()
    except (ValueError, KeyError):
        print("Opção inválida", file=sys.stderr)
        # sys.stderr.write("Opção inválida") #  Faz a mesma coisa da linha 59
