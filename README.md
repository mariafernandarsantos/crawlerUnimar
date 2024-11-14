<h1>TradeMap WebCrawler</h1> 

<p align="center">
  <img src="http://img.shields.io/static/v1?label=Python&message=3.13.0&color=red&style=for-the-badge&logo=ruby"/>
  <img src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=RED&style=for-the-badge"/>
</p>

> Status do Projeto: :warning: (em desenvolvimento)

### Tópicos 

:small_blue_diamond: [Descrição do projeto](#descrição-do-projeto)

:small_blue_diamond: [Funcionalidades](#funcionalidades)

:small_blue_diamond: [Pré-requisitos](#pré-requisitos)

:small_blue_diamond: [Como rodar a aplicação](#como-rodar-a-aplicação-arrow_forward)

... 

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
<br>:warning: [Módulo requests]
<br>:warning: [Módulo bs4]
<br>:warning: [Módulo pandas]
<br>:warning: [Módulo os]
<br>:warning: [Módulo datetime]
<br>:warning: [Módulo time]

...

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
<br>Guilherme Yuji Tanaka</br> 
<br>Murilo Gonçalves Rocha Santana</br>
<br>Maria Fernanda Rodrigues Santos</br>
<br>João Victor Guimarães Martins Tozato</br>
<br>Pedro Henrique Arroio Quiqueto Franco</br>
