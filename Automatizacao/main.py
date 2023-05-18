# -*- coding: utf-8 -*-
# -*- coding: utf8 -*-
import webbrowser
import pyautogui
import pandas as pd
import time


# Abre o navegar ou adiciona uma aba.
webbrowser.open('https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema')

# Aguarda 3 segundos para abrir o navegador.
time.sleep(3)

# Clica no text usuario.
pyautogui.click(x=642, y=569)

# Escreve o usuário.
pyautogui.write('guilherme', interval=0.1)

# Aperta o TAB, vai o text de senha.
pyautogui.press('tab')

# Escreve a senha.
pyautogui.write('senha123', interval=0.1)

# Clica no botão de login.
pyautogui.click(x=687, y=735)

# Aguarda 5 segundo para abrir a pagina.
time.sleep(5)

# Seleciona o arquivo
pyautogui.click(x=436, y=545)

# Aguarda 3 segundo para abrir a pagina.
time.sleep(3)

# Clica transferir(download) o arquivo.
pyautogui.click(x=575, y=400)

# Aguarda 5 segundo para transferir o arquivo
time.sleep(5)

# Pega todo o arquivo e armazena.
tabela = pd.read_csv(r"/home/prado/Transferências/Compras.csv", sep=";")

# Soma os valores da coluna Valor Final, e armazena.
total_gasto = tabela["ValorFinal"].sum()

# Soma os valores da coluna Quantidade, e armazena.
quantidade = tabela["Quantidade"].sum()

# Divide o total gasto pela quantidade.
preco_medio = total_gasto / quantidade

# Apresenta os dados.
"""
    print(total_gasto)
    print(quantidade)
    print(preco_medio)
"""

# Acessa o e-mail.
pyautogui.hotkey("ctrl", "t")
pyautogui.write("gmail.com")
pyautogui.press("enter")

# Aguarda 5 segundo para transferir o arquivo
time.sleep(5)

# Clica no botar compor.
pyautogui.click(x=132, y=395)

# Aguarda 2 segundo para transferir o arquivo
time.sleep(2)

# Preenche o destinatario.
pyautogui.write('guimattos1983@gmail.com', interval=0.1)

# Escolhe o destinatario.
pyautogui.press('tab')

# Passa para o campo assunto.
pyautogui.press('tab')

# Preenche o assunto.
pyautogui.typewrite('Relatório automatizado de vendas.'.encode().decode('utf-8'))

time.sleep(.01)

# Passa para o campo corpo do e-mail.
pyautogui.press('tab')

# Preenche o corpo do e-mail.
texto = f"""
Prezados,
Segue o relatório de compras

Total Gasto:  R$ {total_gasto:,.2f}
Quantidade de Produtos:  {quantidade:,}e
Preço Médio:  R$ {preco_medio:,.2f}

Qualquer dúvida, é só falar.guilherme   senha1
Att., Guilherme Mattos
"""

pyautogui.typewrite(texto.encode().decode('utf8'))

# Aguarda 2 segundo para transferir o arquivo
time.sleep(2)

# Clica no botao enviar.
pyautogui.hotkey("ctrl", "enter")
