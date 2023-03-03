from unittest.mock import patch
from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
from tech_news.database import find_news

mock_data = [
    {"title": "noticia_0", "reading_time": 2},
    {"title": "Notícia bacana", "reading_time": 4},
    {"title": "Notícia bacana 2", "reading_time": 1},
    {"title": "noticia_3", "reading_time": 1},
    {"title": "noticia_4", "reading_time": 1},
]

response = {
    "readable": [
        {"unfilled_time": 1, "chosen_news": [("noticia_0", 2)]},
        {
            "unfilled_time": 1,
            "chosen_news": [("Notícia bacana 2", 1), ("noticia_3", 1)],
        },
        {"unfilled_time": 2, "chosen_news": [("noticia_4", 1)]},
    ],
    "unreadable": [("Notícia bacana", 4)],
}


def test_reading_plan_group_news():
    with patch.object(
        ReadingPlanService.group_news_for_available_time, "cls._db_news_proxy",
            return_value=mock_data
    ) as mocked:
        result = ReadingPlanService.group_news_for_available_time(3)

    mocked.assert_awaited_with(3)
    assert result == response


def test_pegar_mock():
    a = [
        {"title": news["title"], "reading_time": news["reading_time"]}
        for news in find_news()
    ]
    print(a[:5])
    assert "" == ""
