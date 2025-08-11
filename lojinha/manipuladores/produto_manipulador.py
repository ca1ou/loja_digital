import os
import json

CAMINHO_ARQUIVO = 'arquivos/produto.json'
def salvar_produto(novo):
    try:
        if os.path.exists(CAMINHO_ARQUIVO):
            with open(CAMINHO_ARQUIVO, 'r') as file:
                produtos = json.load(file)
        else:
            produtos = []
        #aqui vai
        produtos.append(novo.dicionario_produto())
        #apartir daq nao vai
        with open(CAMINHO_ARQUIVO, 'w') as f:
            json.dump(produtos, f, indent=4)
            return True
    except:
        return False

def comprar_produto(self):
    produtos = []
    usuarios = []
    if os.path.exists('user.json') and os.path.exists('produto.json'):
        with open('user.json') as f:
            usuarios = json.load(f)
        with open('produto.json') as f:
            produtos = json.load(f)

    with open('user.json', "w") as f:
        json.dump(usuarios, f, indent=4)

    with open('produto.json', "w") as f:
        json.dump(produtos, f, indent=4)
        return True
