import requests
from tkinter import *
from tkinter import ttk
import datetime
from PIL import Image, ImageTk


# Inicializa variavel nova imagem
nome_imagem = ''

# Referencia Tk
interface = Tk()

# Cor de de fundo da tela.
interface.configure(bg='#c4dee3')

# Titulo da tela.
interface.title('Previsão do tempo')

# Tamanho da tela.
interface.geometry('320x350')

# Deixa o tamanho da tela fixo.
interface.resizable(width=False, height=False)

# cria um separador entre pesquisa e resultados
ttk.Separator(interface, orient=HORIZONTAL).grid(row=0, column=1, ipadx=157)

# criando frames
frame_top = Frame(interface, width=320, height=70,
                  bg='#c4dee3', padx=0, pady=0)
frame_top.grid(row=1, column=0)

frame_corpo = Frame(interface, width=320, height=280,
                    bg='white', padx=12, pady=0)
frame_corpo.grid(row=2, column=0, sticky=NW)


def dia_semana_extenso(dia):
    ''' retorna o dia da sema por extenso '''
    if dia == 0:
        return 'Segunda-feira'

    elif dia == 1:
        return 'Terça-feira'

    elif dia == 2:
        return 'Quarta-feira'

    elif dia == 3:
        return 'Quinta-feira'

    elif dia == 4:
        return 'Sexta-feira'

    elif dia == 5:
        return 'Sabado'

    elif dia == 6:
        return 'Domingo'


def informacao(cidade):
    ''' Função busca e apresenta dados '''
    if cidade != '':
        # Chave da api.
        API_KEY = "a945e5f3a1149f6c1135955c816bd11a"

        # Link com devidos parâmetros para pesqueisa do tempo.
        link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt"

        # Seta dados do linhk.
        requisicao = requests.get(link)

        # Armazena dados em json.
        requisicao = requisicao.json()

        # Altera a primeira letra para maiuscula.
        l_cidade['text'] = cidade.capitalize()

        # Imagem tempo.
        nome_imagem = requisicao['weather'][0]['icon']
        imagem_temp[
            'file'] = f'/home/prado/Documentos/Projetos-py/SistemaBanco/Aulas/PrevisaoTempo/imagens/{nome_imagem}.png'

        # Temperaturas.
        temperatura = round(requisicao['main']['temp'] - 273.15)
        l_temp['text'] = f'{temperatura}'
        temp_min = round(requisicao['main']['temp_min'] - 273.15)
        temp_max = round(requisicao['main']['temp_max'] - 273.15)
        l_temp_min['text'] = f'Min: {temp_min}°C  Max: {temp_max}°C'

        # Dia da semana e hora.
        dia = dia_semana_extenso(datetime.date.today().weekday())
        hora = datetime.datetime.now().strftime("%H:%M")
        l_dia_hora['text'] = f'{dia}  {hora}'

        # Descrição do dia.
        l_descricao_dia['text'] = requisicao['weather'][0]['description']

        # Humidade.
        humidade = requisicao['main']['humidity']
        l_humidade['text'] = f'Humidade: {humidade}%'

        # Vento.
        vento = requisicao['wind']['speed']
        l_vento['text'] = f'Vento: {vento}km/h'


# configurando frame top.
l_info = Label(frame_top, text="Confira o clima da uma cidade:", anchor='center',
               bg='#c4dee3', font=('Arial', 12))
l_info.place(x=10, y=10)
e_local = Entry(frame_top, width=27, justify='left', font=(
    'Arial', 14), highlightthickness=1, relief='solid')
e_local.place(x=10, y=35)
e_local.insert(0, 'Goiânia')

# Abrindo imagem do botão.
url_imagem_pesq = Image.open(
    '/home/prado/Documentos/Projetos-py/SistemaBanco/Aulas/PrevisaoTempo/imagens/lupa.ico')
resize_img_pesq = url_imagem_pesq.resize((20, 20), Image.BICUBIC)
new_image_pesq = ImageTk.PhotoImage(resize_img_pesq)

# Botão pesquisa tempo da cidade.
b_ver = Button(frame_top, command=lambda: informacao(e_local.get()), image=new_image_pesq,
               bg='white', font=('Arial', 12), relief='raised', overrelief=RIDGE)
b_ver.place(x=285, y=35)

# Configurando frame corpo.
# Cidade pesquisada.
l_cidade = Label(frame_corpo, text="Goiânia", width=25,
                 bg='white', font=('-weight bold', 14))
l_cidade.place(x=0, y=4)

# Imagem tempo.
imagem_temp = PhotoImage(file='')
l_imagem_temp = Label(frame_corpo, bg='white', image=imagem_temp)
l_imagem_temp.place(x=0, y=50)

# Temperatura media.
l_temp = Label(frame_corpo, text="17", anchor='center',
               bg='white', font=('Arial', 30))
l_temp.place(x=160, y=60)
Label(frame_corpo, text="°C", anchor='center',
      bg='white', font=('Arial', 12)).place(x=210, y=65)

# Temperatura minima e maxima.
l_temp_min = Label(frame_corpo, text="Min.", anchor='center',
                   bg='white', font=('Arial', 10))
l_temp_min.place(x=160, y=110)

# Linha.
Label(interface, text='________________________________________',
      bg='white').place(x=20, y=220)

Label(interface, text='________________________________________',
      bg='white').place(x=20, y=275)

# Dia e hora.
l_dia_hora = Label(frame_corpo, text="Dia e Hora", anchor='center',
                   bg='white', font=('Arial', 11))
l_dia_hora.place(x=10, y=180)

# Descricao do tempo.
l_descricao_dia = Label(frame_corpo, text="Descricao tempo", anchor='center',
                        bg='white', font=('Arial', 11))
l_descricao_dia.place(x=170, y=180)

# Humidade.
l_humidade = Label(frame_corpo, text="Humidade", anchor='center',
                   bg='white', font=('Arial', 11))
l_humidade.place(x=10, y=235)

# Vento.
l_vento = Label(frame_corpo, text="Vento", anchor='center',
                bg='white', font=('Arial', 11))
l_vento.place(x=170, y=235)

# Chama função para buscar os dados da cidade padrão.
informacao(e_local.get())

# Mostra tela.
interface.mainloop()
