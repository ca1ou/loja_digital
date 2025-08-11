import os
import json

CAMINHO_ARQUIVO = 'arquivos/user.json'
def salvar_user(novo):
    try:
        if os.path.exists(CAMINHO_ARQUIVO):
            with open(CAMINHO_ARQUIVO, 'r') as file:
                usuarios = json.load(file)
        else:
            usuarios = []
        usuarios.append(novo.dicionario_user())
        with open(CAMINHO_ARQUIVO, 'w') as f:
            json.dump(usuarios, f, indent=4)
            return True
    except:
        return False