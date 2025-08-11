import os
import tkinter as tk
import json
from classes.produto import Produto
from manipuladores.produto_manipulador import salvar_produto

def janela_cadastrar_produto(janela):
    frame_produto = tk.Frame(janela)
    frame_produto.pack(fill='both', expand=True)

    label_nome_produto = tk.Label(frame_produto, text='Nome: ')
    label_nome_produto.grid(row=0, column=0, padx=5, pady=5)
    entrada_nome_produto = tk.Entry(frame_produto)
    entrada_nome_produto.grid(row=0, column=1, padx=5, pady=5)

    label_preco_produto = tk.Label(frame_produto, text='Preço: ')
    label_preco_produto.grid(row=1, column=0, padx=5, pady=5)
    entrada_preco_produto = tk.Entry(frame_produto)
    entrada_preco_produto.grid(row=1, column=1, padx=5, pady=5)

    label_descricao_produto = tk.Label(frame_produto, text='Descrição: ')
    label_descricao_produto.grid(row=0, column=2, padx=5, pady=5)
    descriçao_produto = tk.Entry(frame_produto)
    descriçao_produto.grid(row=0, column=3, padx=5, pady=5)

    lista_categoria = ['Ferramentas', 'Construção', 'Comida']

    label_categoria_produto = tk.Label(frame_produto, text='Categoria: ')
    label_categoria_produto.grid(row=2, column=0, padx=5, pady=5)
    categoria_produto = tk.Listbox(frame_produto, selectmode='extended', height=3)
    categoria_produto.grid(row=2, column=1)
    for categorias in lista_categoria:
        categoria_produto.insert(tk.END, categorias)

    def cadastrar_produtos():
        nome = entrada_nome_produto.get()
        preco = entrada_preco_produto.get()
        try:
            with open('arquivos/produto.json', 'r') as file:
                produtos = json.load(file)
        except:
            produtos = []

        for p in produtos:
            lista_produtos = []
            lista_produtos.append(p)
            id_janela = len(lista_produtos) + 1

        if preco.isdigit():
            novo = Produto(nome, preco, id_janela)
            if salvar_produto(novo):
                print('Cadastro realizado com sucesso!')
            else:
                print('Erro ao cadastrar produto.')
        else:
            print('Tem que ser em numeros o preco')
    
    botao = tk.Button(frame_produto, text='Salvar', command=cadastrar_produtos)
    botao.grid(row=4, column=1, padx=5, pady=5)
