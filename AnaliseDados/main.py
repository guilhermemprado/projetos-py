import pandas as pd
import plotly.express as px


# Abre o arquivo.
# separa as colunas pelo caracter (;).
tabela = pd.read_csv("clientes.csv", encoding='latin', sep=';')

# Exclui coluna (Unnamed: 8), pois não tem utilizade.
# Axis = (0 = linha, 1 = coluna).
tabela = tabela.drop(['Unnamed: 8', 'ClienteID'], axis=1)

# Acerta informações que estão sendo reconhecidas de forma errada.
# Converte a coluna (Salário Anual (R$)), para numerico.
tabela['Salário Anual (R$)'] = pd.to_numeric(tabela['Salário Anual (R$)'], errors='coerce')

# Remove resultados que tenha pelo menos uma informação nula.
tabela = tabela.dropna()

# Visualiza as estatisticas dos dados restantes.
print(tabela.describe())

# Gerando graficos
# text_auto (Apresenta as informações nas barras).
# histfunc (avg = Faz o cálculo da média das notas para cada fatia de informação).
# nbins (Número de fatias de informações).
for coluna in tabela.columns:
    if coluna != 'Nota (1-100)': # Não fazer grafico da coluna Nota (1-100).
        grafico = px.histogram(tabela, x=coluna, y='Nota (1-100)', text_auto=True, histfunc='avg', nbins=10)
        grafico.show()
