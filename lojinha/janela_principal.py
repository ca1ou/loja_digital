import tkinter as tk
import os
from janela.cadastrar_user import janela_cadastrar_user
from janela.cadastrar_produto import janela_cadastrar_produto

def janela_principal_tk():
    def ao_fechar():
        limpar_frame_conteudo()
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Você fechou a janela!")
        janela.destroy()

    def abrir_produtos():
        limpar_frame_conteudo()
        janela_cadastrar_produto(janela)

    def abrir_user():
        limpar_frame_conteudo()
        janela_cadastrar_user(janela)
        
    def limpar_frame_conteudo():
        if len(janela.winfo_children()) > 1:
            janela.winfo_children()[1].destroy()
            
    janela = tk.Tk()
    janela.title('Loja_Digital')
    janela.geometry('450x450')
    janela.protocol("WM_DELETE_WINDOW", ao_fechar)

    menu_bar = tk.Menu(janela)
    janela.config(menu=menu_bar)

    menu_principio = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label='Cadastro e login', menu=menu_principio)

    menu_principio.add_command(label='Usuario', command=abrir_user)
    menu_principio.add_command(label='Produto', command=abrir_produtos)
    menu_principio.add_separator()
    menu_principio.add_command(label='Sair', command=ao_fechar)

    frame_conteudo = tk.Frame(janela)
    frame_conteudo.pack(fill="both", expand=True)
    frame_conteudo.pack(pady=10)

    janela.mainloop()
