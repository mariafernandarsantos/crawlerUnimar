import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import datetime

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 OPR/98.0.0.0'
}

def extrair_texto(link, pasta_destino):
    response = requests.get(link, headers=headers)
    if response.status_code == 200:
        content = response.content
        site = BeautifulSoup(content, 'html.parser')

        # Lista para armazenar os dados
        dados = []
        selecao = ["Brazil"]
        data_hora_atual = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        elementos = site.find_all('tr', {'align': 'right'})
        for elemento in elementos:
            colunas = elemento.find_all('td')
            if len(colunas) >= 12:
                exporters = colunas[1].get_text().strip()
                valor_2023 = colunas[2].get_text().strip()
                participacao_2023 = colunas[3].get_text().strip()
                quantidade_2023 = colunas[4].get_text().strip()
                crescimento_valor = colunas[5].get_text().strip()
                crescimento_quantidade = colunas[6].get_text().strip()
                valor_unitario = colunas[7].get_text().strip()
                balanca_comercial = colunas[8].get_text().strip()
                crescimento_exportacoes = colunas[9].get_text().strip()
                participacao_importacoes = colunas[10].get_text().strip()
                participacao_exportacoes = colunas[11].get_text().strip()
                ranking_mundial = colunas[12].get_text().strip()

                if exporters in selecao:
                    # Adiciona os dados na lista
                    dados.append([
                        exporters, valor_2023, participacao_2023, quantidade_2023,
                        crescimento_valor, crescimento_quantidade, valor_unitario,
                        balanca_comercial, crescimento_exportacoes, participacao_importacoes,
                        participacao_exportacoes, ranking_mundial
                    ])


        # Cria um DataFrame com os dados
        df = pd.DataFrame(dados, columns=[
            'Exporters', 'Value 2023 (USD thousand)', 'Trade balance 2023 (USD thousand)',
            'Share in Brazil\'s imports (%)', 'Growth 2019-2023 (%)', 'Growth 2022-2023 (%)',
            'Ranking in world exports', 'Share in world exports (%)',
            'Total exports growth 2019-2023 (%)', 'Distance to markets (km)',
            'Concentration of importing countries', 'Tariff applied by Brazil (%)'
        ])

        # Cria o caminho completo do arquivo CSV
        nome_arquivo = f'dados_comercio_{data_hora_atual}.csv'
        caminho_arquivo = os.path.join(pasta_destino, nome_arquivo)

        # Exporta para o arquivo CSV no caminho especificado
        df.to_csv(caminho_arquivo, index=False)
        print(f"Dados exportados com sucesso para '{caminho_arquivo}'")

# URL do site
url = 'https://www.trademap.org/Country_SelProductCountry.aspx?nvpm=1%7c076%7c%7c%7c%7c01%7c%7c%7c2%7c1%7c1%7c1%7c1%7c%7c2%7c1%7c1%7c1'

# Caminho da pasta onde o arquivo será salvo
pasta_destino = r'D:\Faculdade'

# Extrai o texto e salva o arquivo CSV na pasta especificada
extrair_texto(url, pasta_destino)