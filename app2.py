import tkinter as tk
from tkinter import ttk 
from tkcalendar import DateEntry # Usamos esta biblioteca para criar o calendário --> pip install tkcalendar
import requests # Fazer requisição da URL.

requisicao = requests.get('https://economia.awesomeapi.com.br/all')

dicionario_requisicao = requisicao.json()

lista_moedas = list(dicionario_requisicao)
#dicionario_requisicao = list(requisicao.json())
lista_moedas = list(dicionario_requisicao.keys())

"""
Somente cria as funções quando for necessário.
    Somente chama as funções quando for necessário.
anchor --> Serve para posicionar os botões
borderwidth --> Criar a bordar no lebel
relief --> Parametro para criar a borda sólida
columnspan --> Colocar o elemento em mais de 1 coluna
command --> Dar funcinalidade ao botão
row --> Está posicionado na linha 0 da grade
column --> Está posicionado na Coluna 0 da grade
padx --> --> Define o espaço vertical (margem) de 10 pixels do widget. Isso também cria um espaçamento ao redor do widget.
pady --> Define o espaço vertical (margem) de 10 pixels do widget. Isso também cria um espaçamento ao redor do widget. 
sticky --> Define como o widget deve se "expandir" dentro da célula da grade.
                'n' significa norte (parte superior).
                's' significa sul (parte inferior).
                'w' significa oeste (lado esquerdo).
                'e' significa leste (lado direito)
columnspan --> Define que o widget ocupará 3 colunas na grade, começando na coluna 0. O widget ocupe mais espaço horizontal.

"""

janela = tk.Tk()
janela.resizable(False,False)
janela.title('Ferramenta de cotações de moedas')

def pegar_cotacao():
    moeda = combobox_selecionar_moeda.get()
    data = calendario_selecionar_dia.get()
    
    print(moeda)
    print(data)
    
    dia = data[:2]
    mes = data[3:5]
    ano = data[6:]
    
    data_completa = mes,dia,ano
    
    link = f'https://economia.awesomeapi.com.br/json/daily/{moeda}/?start_date={ano}{mes}{dia}&end_date={ano}{mes}{dia}'
    print(link)
    
    requisicao_moeda = requests.get(link)
    cotacao = requisicao_moeda.json()
    
    """ O zero representa o indice da coluna e o bid representa a chave do dicionaraio"""
    valor_moeda = cotacao[0]["bid"]
    label_resultado_cotacao['text'] = f'A moeda {moeda} na data {data} fechou com o valor de R${valor_moeda}'
    
def selecionar_excel():
    
    pass

def atualizar_cotacoes():
    
    pass


""" Primeira linha """
label_cotacao_moeda = tk.Label(text='Cotação de 1 moeda específica', borderwidth=2, relief='solid')
label_cotacao_moeda.grid(row=0, column=0, padx=10, pady=10, sticky='nswe', columnspan=3)

""" Segunda linha """
label_selecionar_moeda = tk.Label(text='Selecione a moeda que desejar consultar',anchor='e')
label_selecionar_moeda.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

combobox_selecionar_moeda = ttk.Combobox(values=lista_moedas)
combobox_selecionar_moeda.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

""" Terceira linha """
label_selecionar_dia = tk.Label(text='Selecione o dia que deseja pegar a cotação',anchor='e')
label_selecionar_dia.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

calendario_selecionar_dia = DateEntry(locale='pt_br')
calendario_selecionar_dia.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

""" Quarta linha """
label_resultado_cotacao = tk.Label(text='') # Irá começar com texto vazio e atualizado quando consultar o valor da moeda
label_resultado_cotacao.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

botao_resultado_cotacao = tk.Button(text='Pegar cotação', command=pegar_cotacao)
botao_resultado_cotacao.grid(row=3, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

""" Quinta linha """
label_cotacao_multiplas_moeda = tk.Label(text='Cotação de múltiplas moeda específica', borderwidth=2, relief='solid')
label_cotacao_multiplas_moeda.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=3)

""" Sexta linha """
label_selecionar_excel = tk.Label(text='Selecione o arquivo em Excel')
label_selecionar_excel.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

botao_selecionar_excel = tk.Button(text='Clique aqui para selecionar', command=selecionar_excel)
botao_selecionar_excel.grid(row=5, column=2, padx=10, pady=10, sticky='nswe')

""" Sétima linha """
label_exel_selecionado = tk.Label(text='Nenhum arquivo selecionado', anchor='e')
label_exel_selecionado.grid(row=6, column=0, padx=10, pady=10, sticky='nswe', columnspan=3)

""" Oitava linha """
label_data_inicial = tk.Label(text='Data Inicial', anchor='e')
label_data_inicial.grid(row=7, column=0, padx=10, pady=10, sticky='nswe')

calendario_data_inicial = DateEntry(locale='pt_br')
calendario_data_inicial.grid(row=7, column=1, padx=10, pady=10, sticky='nswe')

""" Nona linha """
label_data_final = tk.Label(text='Data final',anchor='e')
label_data_final.grid(row=8, column=0, padx=10, pady=10, sticky='nswe')

calendario_data_final = DateEntry(locale='pt_br')
calendario_data_final.grid(row=8, column=1, padx=10, pady=10, sticky='nswe')

""" Décima linha """
botao_atualizar_contacao = tk.Button(text='Atualizar cotações', command=atualizar_cotacoes)
botao_atualizar_contacao.grid(row=9, column=0, padx=10, pady=10, sticky='nswe')

label_atualizar_contacao = tk.Label(text='TEXTO VAZIO',  anchor='e')
label_atualizar_contacao.grid(row=9, column=1, padx=10, pady=10, sticky='nswe', columnspan=2)

""" Décima primeira linha """
botao_fechar = tk.Button(text='Fechar', command=janela.quit)
botao_fechar.grid(row=10, column=2, padx=10, pady=10, sticky='nswe')

""" Rodar programa """
janela.mainloop()