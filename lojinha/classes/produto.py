import json
import os

class Produto():
    def __init__(self, nome_produto, preco_produto=0, id_produto = 0, disponivel=True):
        self.nome_produto = nome_produto
        self.preco_produto = int(preco_produto)
        self.id_produto = id_produto
        self.disponivel = disponivel
        
    def dicionario_produto(self):
        return {
            "nome": self.nome_produto,
            "preco": self.preco_produto,
            "id": self.id_produto,
            "disponivel": self.disponivel
        }
            