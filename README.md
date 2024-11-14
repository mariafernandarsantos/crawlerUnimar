<h1>TradeMap WebCrawler</h1> 

<p align="center">
  <img src="http://img.shields.io/static/v1?label=Python&message=3.13.0&color=red&style=for-the-badge&logo=ruby"/>
  <img src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=RED&style=for-the-badge"/>
</p>

> Status do Projeto: :heavy_check_mark: :warning: (em desenvolvimento)

### Tópicos 

:small_blue_diamond: [Descrição do projeto](#descrição-do-projeto)

:small_blue_diamond: [Funcionalidades](#funcionalidades)

:small_blue_diamond: [Pré-requisitos](#pré-requisitos)

:small_blue_diamond: [Como rodar a aplicação](#como-rodar-a-aplicação-arrow_forward)

... 

Insira os tópicos do README em links para facilitar a navegação do leitor

## Descrição do projeto 

<p align="justify">
  Este projeto automatiza o processo de extração de dados comerciais de um site. O código coleta informações de comércio internacional
  específicas, como dados de exportação e importação do "Brasil", usando uma requisição à página e análise do conteúdo HTML.
  Após a extração, ele salva os dados em um arquivo CSV para facilitar análises e visualizações futuras.
  O código usa de parâmetros para que o usuário possa selecionar os filtros que deseja durante a pesquisa.
</p>

## Funcionalidades

:heavy_check_mark: Escolher o(s) país(es) utilizados para a pesquisa. 

:heavy_check_mark: Escolher o(s) produtos(s) utilizados para a pesquisa.

:heavy_check_mark: Salvar os dados em um arquivos csv para facilitação de análises e visualizações.

:heavy_check_mark: Nome dos arquivos salvos com base no horário de execução e código de produto selecionado.

## Pré-requisitos

:warning: [Python](https://www.python.org/downloads/)
:warning: [Módulo requests]
:warning: [Módulo bs4]
:warning: [Módulo pandas]
:warning: [Módulo os]
:warning: [Módulo datetime]
:warning: [Módulo time]

...

Liste todas as dependencias e libs que o usuário deve ter instalado na máquina antes de rodar a aplicação 

## Como rodar a aplicação :arrow_forward:

No terminal, clone o projeto: 

```
git clone https://github.com/React-Bootcamp-WoMarkersCode/certificate-generator
```

Execute os comandos no terminal para instalar os pacotes bs4

```
pip install bs4
pip install pandas
pip install requests

```
Depois, apenas rodar o código pela IDE utilizada.  

... 


## Casos de Uso

O programa pode ser usado em casos onde seja necessário analisar e comparar os valores e dados de compras internacionais para produtos específicos,
e também para países específicos.

## Tarefas em aberto

:memo: Realizar a busca em mais de uma página.

:memo: Realizar o login apenas uma vez para que o usuário tenha livre acesso.

## Desenvolvedores/Contribuintes :octocat:

Liste o time responsável pelo desenvolvimento do projeto

| [<img src="https://avatars2.githubusercontent.com/u/46378210?s=400&u=071f7791bb03f8e102d835bdb9c2f0d3d24e8a34&v=4" width=115><br><sub>Guilherme Yuji Tanaka</sub>](https://github.com/Diana-ops) |  [<img src="https://avatars2.githubusercontent.com/u/46378210?s=400&u=071f7791bb03f8e102d835bdb9c2f0d3d24e8a34&v=4" width=115><br><sub>Murilo Gonçalves Rocha Santana</sub>](https://github.com/Diana-ops) |  [<img src="https://avatars2.githubusercontent.com/u/46378210?s=400&u=071f7791bb03f8e102d835bdb9c2f0d3d24e8a34&v=4" width=115><br><sub>Maria Fernanda Rodrigues Santos</sub>](https://github.com/Diana-ops) | [<img 
src="https://avatars2.githubusercontent.com/u/46378210?s=400&u=071f7791bb03f8e102d835bdb9c2f0d3d24e8a34&v=4" width=115><br><sub>João Victor Guimarães Martins Tozato</sub>](https://github.com/Diana-ops) |  [<img 
src="https://avatars2.githubusercontent.com/u/46378210?s=400&u=071f7791bb03f8e102d835bdb9c2f0d3d24e8a34&v=4" width=115><br><sub>Pedro Henrique Arroio Quiqueto Franco</sub>](https://github.com/Diana-ops) |
| :---: | :---: | :---: 
