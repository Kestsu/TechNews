# TechNews: Um exemplo de raspagem de dados!

<img src="https://github.com/Kestsu/TechNews/assets/99990041/0ab0fc94-9209-4e7c-a9a6-fa08d6485382" width="400px">

<img src="https://github.com/Kestsu/TechNews/assets/99990041/59f834d1-8654-4b7f-82c8-e66d5c502250" width="400px">

<img src="https://github.com/Kestsu/TechNews/assets/99990041/0450daed-af33-4809-bed9-8c8eb3b04e12" width="700px">


<br/>
<details>
  As notícias a serem raspadas estarão disponíveis no _Blog da Trybe_: https://blog.betrybe.com.
  Essas notícias seram salvas no banco de dados utilizando as funções python no módulo `database.py`
    
  Para a realização deste projeto, foram utilizado um banco de dados chamado `tech_news`.
  As notícias serão armazenadas em uma coleção chamada `news`.

</details>

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

Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando "deactivate". Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.

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

  <strong>MongoDB</strong>


## Caso não tenha o docker instalado, acesse:

Para linux:
https://docs.docker.com/engine/install/ubuntu/

Para Mac:
https://www.docker.com/

Caso queira instalar e rodar o servidor MongoDB nativo na máquina, siga as instruções no tutorial oficial:

Ubuntu: <https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/>
<br/>
MacOS:  <https://docs.mongodb.com/guides/server/install/>

## Caso não tenha o MongoDB instalado, acesse:

https://www.mongodb.com/


