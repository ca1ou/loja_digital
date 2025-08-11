import json
import os

class User():
    def __init__(self, nome_user,  senha_user, cpf_user=0, dinheiro_user = 100):
        self.nome_user = nome_user
        self.cpf_user = int(cpf_user)
        self.senha_user = senha_user
        self.dinheiro_user = dinheiro_user

    def dicionario_user(self):
        return {
            "nome": self.nome_user,
            "cpf": self.cpf_user,
            "senha": self.senha_user,
            "dinheiro": self.dinheiro_user
        }
    