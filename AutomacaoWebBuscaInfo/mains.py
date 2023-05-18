import pandas as pd
from selenium import webdriver
import textwrap

navegador = webdriver.Chrome()

tabela = pd.read_excel('AutomacaoWebBuscaInfo/commodities.xlsx')
print(tabela)

# Percorre todas as linhas.
for linha in tabela.index:
    # Armazena o produto.
    produto = tabela.loc[linha, 'Produto']

    # Mostra o produto.
    print(produto)

    # Retira os acentos.
    produto = produto.replace('ó', 'o').replace('ã', 'a').replace('á', 'a').replace(
        'ç', 'c').replace('ú', 'u').replace('é', 'e').replace('í', 'i')

    # Armazena a url.
    link = f'https://www.melhorcambio.com/{produto}-hoje'

    # Mostra a url.
    print(link)

    # Chama o navegador na url armazenada.
    navegador.get(link)

    # Procura o preço do produto na pagina do navegador.e
    preco = navegador.find_element(
        'xpath', "//*[@id='comercial']").get_attribute('value')

    # Retira o ponto do preço, e troca virgula por ponto.
    preco = preco.replace('.', '').replace(',', '.')

    # Mostra o preço
    print(preco)

    # Coloca o preço no produto da tabela.
    tabela.loc[linha, 'Preço Atual'] = float(preco)


# Preencher a coluna comprar
tabela['Comprar'] = tabela['Preço Atual'] < tabela['Preço Ideal']

opcao = """\n
        ===== Exportar para ======
        [c]  Csv
        [e]  Excel
        [h]  Html
        => """

opcao_escolhida = input(textwrap.dedent(opcao))

print('Acabou')
print(tabela)

# exportar a base
if opcao_escolhida == 'c':  # Csv
    tabela.to_csv('AutomacaoWebBuscaInfo/commodities_atualizado.csv', index=False)
elif opcao_escolhida == 'e':  # Excel
    tabela.to_excel('AutomacaoWebBuscaInfo/commodities_atualizado.xlsx', index=False)
elif opcao_escolhida == 'h':  # Html
    tabela.to_html('AutomacaoWebBuscaInfo/commodities_atualizado.html', index=False)

# Fecha o navegador
navegador.quit()
