from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501


mock = [
  {
    "_id": {
      "$oid": "63e6d325b33b82cc86e13cde"
    },
    "url": "https://blog.betrybe.com/novidades/noticia-bacana",
    "title": "Notícia bacana",
    "writer": "Eu",
    "summary": "Algo muito bacana aconteceu",
    "reading_time": 4,
    "timestamp": "04/04/2021",
    "category": "Ferramentas"
  },
  {
    "_id": {
      "$oid": "63eab380d0533ae4d961b6ba"
      },
    "url": "https://blog.betrybe.com/novidades/noticia_3.htm",
    "title": "noticia_3",
    "timestamp": "23/11/2020",
    "writer": "Escritor_3",
    "reading_time": 1,
    "summary": "Sumario da noticia_3",
    "category": "Ferramentas"
  }
]


def test_reading_plan_group_news():
    pass
