import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title('Aula do módulo 6')
lista_moedas = ['REAL','DOLAR','BTC']

def processar():
    print('Botão clicado')

titulo_principal = tk.Label(janela, text='Exemplo de interface', font=('Arial',18), borderwidth=2, relief='solid')
titulo_principal.grid(row=0 , column=0, padx= 10 , pady= 10, sticky='nswe', columnspan=4)

label_exemplo = tk.Label(janela, text='Este é um exemplo de label')
label_exemplo.grid(row=1 , column=0, padx= 10 , pady= 10)

entry_exemplo = tk.Entry(janela)
entry_exemplo.grid(row=1 , column=1, padx= 10 , pady= 10)

combobox_exemplo = ttk.Combobox(janela, values=lista_moedas)
combobox_exemplo.grid(row=1 , column=2, padx= 10 , pady= 10)

botao_exemplo = tk.Button(janela, text='Clique Aqui', command=processar)
botao_exemplo.grid(row=1 , column=3, padx= 10 , pady= 10)





janela.mainloop()