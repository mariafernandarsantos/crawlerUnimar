import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import datetime
import time


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 OPR/98.0.0.0'
}

# Lista de códigos de produto
codigos_produto = ['0901', '1201', '1005']
country = ['Brazil', 'Mexico', 'United States of America']

tempo_inicio = time.time()

# Função para obter a URL do produto
def obter_url_produto(codigo_produto):
    return f'https://www.trademap.org/Country_SelProductCountry.aspx?nvpm=1%7c076%7c%7c%7c%7c{codigo_produto}%7c%7c%7c2%7c1%7c1%7c1%7c1%7c1%7c2%7c1%7c1%7c1'

# Função para extrair os dados
def extrair_texto(link, pasta_destino, nome_arquivo):
    response = requests.get(link, headers=headers)
    if response.status_code == 200:
        content = response.content
        site = BeautifulSoup(content, 'html.parser')

        # Lista para armazenar os dados
        dados = []
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

                if exporters in country:
                    # Adiciona os dados na lista
                    dados.append([exporters, valor_2023, participacao_2023, quantidade_2023,
                                  crescimento_valor, crescimento_quantidade, valor_unitario,
                                  balanca_comercial, crescimento_exportacoes, participacao_importacoes,
                                  participacao_exportacoes, ranking_mundial])

        # Cria um DataFrame com os dados
        df = pd.DataFrame(dados, columns=[
            'Exporters', 'Value 2023 (USD thousand)', 'Trade balance 2023 (USD thousand)',
            'Share in Brazil\'s imports (%)', 'Growth 2019-2023 (%)', 'Growth 2022-2023 (%)',
            'Ranking in world exports', 'Share in world exports (%)',
            'Total exports growth 2019-2023 (%)', 'Distance to markets (km)',
            'Concentration of importing countries', 'Tariff applied by Brazil (%)'
        ])

        # Cria o caminho completo do arquivo CSV
        caminho_arquivo = os.path.join(pasta_destino, nome_arquivo)

        # Exporta para o arquivo CSV
        df.to_csv(caminho_arquivo, index=False)
        print(f"Dados exportados com sucesso para '{caminho_arquivo}'")

# Caminho da pasta onde o arquivo será salvo
pasta_destino = r'C:\Users\muril\OneDrive\Desktop\trabalho paulinho'

# Itera sobre os códigos de produto e chama a função para cada um, gerando arquivos separados
for codigo_produto in codigos_produto:
    url1 = obter_url_produto(codigo_produto)
    nome_arquivo1 = f'TRADE_INDICATORS_dados_comercio_{codigo_produto}{datetime.datetime.now().strftime("%Y-%m-%d%H-%M-%S")}.csv'
    extrair_texto(url1, pasta_destino, nome_arquivo1)

tempo_fim = time.time()
tempo_execucao = tempo_fim - tempo_inicio
print(f"Tempo de execução: {tempo_execucao:.2f} segundos")