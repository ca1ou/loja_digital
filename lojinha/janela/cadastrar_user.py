import os
import tkinter as tk
import json
from classes.user import User
from manipuladores.user_manipulador import salvar_user

def janela_cadastrar_user(janela):
    frame_user = tk.Frame(janela)
    frame_user.pack(fill='both', expand=True)

    label_nome = tk.Label(frame_user, text='Nome:')
    label_nome.grid(row=0, column=0, padx=5, pady=5)
    entrada_nome = tk.Entry(frame_user)
    entrada_nome.grid(row=0, column=1, padx=5, pady=5)

    label_cpf = tk.Label(frame_user, text='CPF:')
    label_cpf.grid(row=1, column=0, padx=5, pady=5)
    entrada_cpf = tk.Entry(frame_user)
    entrada_cpf.grid(row=1, column=1, padx=5, pady=5)

    label_senha = tk.Label(frame_user, text='Senha:')
    label_senha.grid(row=2, column=0, padx=5, pady=5)
    entrada_senha = tk.Entry(frame_user)
    entrada_senha.grid(row=2, column=1, padx=5, pady=5)

    def cadastro_usuario():
        nome_usuario = entrada_nome.get()
        cpf_usuario = entrada_cpf.get()
        senha_usuario = entrada_senha.get()
        if cpf_usuario.isdigit():
            novo = User(nome_usuario, senha_usuario, cpf_usuario)
            if verificar():
                if salvar_user(novo):
                    print('Cadastro realizado com sucesso!')
                    limpar_campos()
                else:
                    print('Erro ao cadastrar usuário.')
        else:
            print('Tem que ser em numeros o cpf')

    def logar_usuario(arquivo = 'arquivos/user.json'):
        nome_usuario = entrada_nome.get()
        cpf_usuario = entrada_cpf.get()
        senha_usuario = entrada_senha.get()
        try:
            with open(arquivo, 'r') as f:
                usera = json.load(f)
            for u in usera:
                if cpf_usuario == str(u['cpf']) and senha_usuario == u['senha'] and nome_usuario == u['nome']:
                    print('deu crt!')
                    limpar_campos()
                    return True
            print('deu errado!')
            return False
        except:
            return False
        
    def verificar(arquivo = 'arquivos/user.json'):
        cpf_usuario = entrada_cpf.get()
        with open(arquivo, 'r') as file:
            usuarios = json.load(file)
            for u in usuarios:
                if str(u['cpf']) == cpf_usuario:
                    print('cpf em uso')
                    return False
                if cpf_usuario == '':
                    print('cpf nao pode ser nulo')
                    return False
            return True
        return True

    def limpar_campos():
        entrada_nome.delete(0 ,'end')
        entrada_senha.delete(0 ,'end')
        entrada_cpf.delete(0 ,'end')

    botao1 = tk.Button(frame_user, text='Cadastrar', command=cadastro_usuario)
    botao1.grid(row=3, column=1, padx=5, pady=5)
    botao2 = tk.Button(frame_user, text='Logar', command=logar_usuario)
    botao2.grid(row=3, column=2, padx=5, pady=5)
