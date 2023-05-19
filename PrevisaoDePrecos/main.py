import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

# Le a tabela e armazena.
tabela = pd.read_csv('Aulas/barcos_ref.csv')

# Mostra tabela.
#print(tabela)

# Mostra preçoes
#print(tabela.corr()[['Preco']])

# Cria gráfico
sns.heatmap(tabela.corr()[['Preco']], annot=True, cmap='Blues')

# Mostra o gráfico.
plt.show()

# Armazena o preço.
y = tabela['Preco']

# Armazena a tabela sem a coluna Preço.
x = tabela.drop('Preco', axis=1)

# Dividi a tabela em subconjunto aleatório de trem e teste.
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3, random_state=1)

# Cria as inteligencias aritificiais.
modelo_regressaolinear = LinearRegression()
modelo_arvoredecisao = RandomForestRegressor()

# Treina as inteligencias artificias.
modelo_regressaolinear.fit(x_treino, y_treino)
modelo_arvoredecisao.fit(x_treino, y_treino)

# Criar as previsoes.
previsao_regressaolinear = modelo_regressaolinear.predict(x_teste)
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)

# Comparar os modelos.
#print(metrics.r2_score(y_teste, previsao_regressaolinear))
#print(metrics.r2_score(y_teste, previsao_arvoredecisao))  

# Cria uma tabela vazia.
tabela_auxiliar = pd.DataFrame()

# Cria a coluna y_teste.
tabela_auxiliar["y_teste"] = y_teste

# Cria a coluna Previsoes ArvoreDecisao.
tabela_auxiliar["Previsoes ArvoreDecisao"] = previsao_arvoredecisao

# Cria a coluna Previsoes Regressao Linear.
tabela_auxiliar["Previsoes Regressao Linear"] = previsao_regressaolinear

# Cria gráfico.
sns.lineplot(data=tabela_auxiliar)

# Mostra gáfico.
plt.show()

# Le a tabela e armazena.
nova_tabela = pd.read_csv("Aulas/novos_barcos.csv")

# Mostra nova tabela
print(nova_tabela)

# Armazena a previsão
previsao = modelo_arvoredecisao.predict(nova_tabela)

# Mostra a previsão.
print(previsao)
