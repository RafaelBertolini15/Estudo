# API GRUPOS DA COPA DO MUNDO

Este documento tem a finalidade de **documentar** a nossa API, com o objetivo de **esclarecer o uso e estrutura** da API. Para acesso de dados de jogos e grupos da copa do mundo foi usado a API do *[football-data](https://www.football-data.org)* utilizando FastAPI.

>A API do football-data possui versões pagas, porém, a versão utilizada por nós na nossa API fornece os dados 100% gratuitos, apenas sendo necessário a criação de uma conta para o acesso ao TOKEN.

## Tecnologias

Nossas tecnologias usadas na construção do projeto são:

> - Python
> - FastAPI
> - SQLite
> - SQLAlchemy
> - Requests
> - dotenv

## Execução do código

Antes da execução do código, é necessário fazer as instalações das tecnologias usadas, que estão anotadas em *requerimentos.txt*

### Execute: 
> pip install -r requerimentos.txt

Após isso, para subir o servidor da nossa API, deve-se executar o seguinte comando no terminal:

### Execute:
> uvicorn app.main:app --reload

Após disso, antes de rodarmos os nossos endpoints, é necessário rodar o endpoint de ***update***, para poder consumir os dados atualizados da API do football-data.

### Execute no navegador:

> http://127.0.0.1:8000/update
>> O endpoint tem que ser executado com o servidor no ar

## Swagger

O Swagger é uma ferramenta para construção de uma documentação automática da nossa API, ela pode ser acessada através do navegador pelo seguinte endereço:

### Execute no navegador:

> http://127.0.0.1:8000/docs
>> O endpoint tem que ser executado com o servidor no ar

## Endpoints

Os nossos endpoints são os seguintes:

### /update
> Atualiza o banco de dados consumindo novamente a API externa, sendo necessário ser o primeiro endpoint rodado para ter os dados 100% atualizados

### / 
> Retorna uma mensagem informando que o servidor está de pé.

### /jogos
> Retorna todos os jogos armazenados.

### /grupos
> Retorna os grupos da Copa do Mundo.

### /jogos/grupo/{grupo}
> Retorna os jogos de um grupo específico.

### /jogos/selecao/{selecao}
> Retorna os jogos de uma seleção específica.

## Armazenamento 

Armazenamos todos os dados tratados usados pela API de forma local, utilizando o SQLite. O nosso banco de dados é o **banco.db**

> A persistência dos dados é feita utilizando SQLAlchemy ORM.

## Transformação de dados

Todos os dados recebidos pela API do Football-data passam por um processo de tratamento antes de armazenamos eles, as transformações incluem:

- tratamento de valores nulos;
- padronização dos grupos;
- seleção apenas dos campos necessários;
- formatação das informações dos jogos.

## Fluxo do sistema

Por último, estamos trazendo o fluxo da API, que é o que acontece por baixo dos panos na execução da nossa API.

> Football-Data API ➡️ Requests ➡️ Transformação dos dados ➡️ SQLite ➡️ FastAPI ➡️ Swagger