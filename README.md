# TechNews: Um exemplo de raspagem de dados!

#### Site raspado:

https://blog.betrybe.com/

## Conhecimento envolvido: 

- Python
- Crawlers + POO
- MongoDB
- Docker

## Execução da aplicação localmente


1. Crie o ambiente virtual para o projeto.

```bash
python3 -m venv .venv && source .venv/bin/activate
```

2. Instale as dependências.

```bash
python3 -m pip install -r dev-requirements.txt
```

3. Rode o docker.

```bash
docker-compose up -d
```

4. Para abrir o menu, acesse o terminal e execute o comando abaixo.

```bash
tech-news-analyzer
```


## Buscar notícias por:

### Título:

```bash
conheça os 10 melhores
```
```bash
firewall
```

### Data:

```bash
2023-02-27
```

### Categoria:

```bash
Tecnologia
```

## Caso não tenha o docker instalado, acesse:

Para linux:
https://docs.docker.com/engine/install/ubuntu/

Para Mac:
https://www.docker.com/

## Caso não tenha o MongoDB instalado, acesse:

https://www.mongodb.com/
