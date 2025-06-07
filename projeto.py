import tkinter as tk
from tkinter import messagebox, simpledialog

def cadastrarcontato():
    idcontato = simpledialog.askstring ("ID", "Escolha ID do seu contato:")
    nome = simpledialog.askstring ("Nome", "Escreva o nome do seu contato:")
    telefone = simpledialog.askstring ("Telefone", "Escreva o telefone do contato:")
    email = simpledialog.askstring ("E-mail", "Escreva o e-mail do contato:")
    if idcontato and nome and telefone and email:
        try:
            with open("agenda.txt", "a") as agenda:
                dados = f'{idcontato};{nome};{telefone};{email} \n'
                agenda.write(dados)
            messagebox.showinfo ("Sucesso", 'Contato gravado com sucesso !!!')
        except:
            messagebox.showinfo ("Erro", 'ERRO na gravação do contato.')

def listarcontato():
    try:
        with open("agenda.txt", "r") as agenda:
            contato = agenda.read()
            messagebox.showinfo ("Lista de Contatos", contato if contato else "Nenhum contato encontrado")
    except FileNotFoundError:
        messagebox.showwarning("Aviso", "Agenda não existe.")
    
def deletarcontato():
    nomedeletado = simpledialog.askstring ("Deletar", "Digite o nome a ser deletado:").lower()
    try:
        with open("agenda.txt","r") as agenda:
            aux = []
            aux2 = []
            for i in agenda:
                aux.append(i)
            for i in range(0, len(aux)):
                if nomedeletado not in aux[i].lower():
                    aux2.append(aux[i])
        with open("agenda.txt", "w") as agenda:
            for i in aux2:
                agenda.write(i)
        messagebox.showinfo("Sucesso", 'Contato deletado com sucesso')
    except FileNotFoundError:
        messagebox.showwarning("Aviso", "Contato não encontrado")

def buscarcontatopelonome():
    nome = simpledialog.askstring("Nome", 'Digite o nome a ser procurado:').upper()
    try:
        with open("agenda.txt", "r") as agenda:
            for contato in agenda: 
                if nome in contato.split(";")[1].upper():
                    messagebox.showinfo(f"Contato", contato)
    except FileNotFoundError:
        messagebox.showwarning("Aviso", "Contato não encontrado")

def fechar():
    root.destroy()

root = tk.Tk()
root.title ("Agenda")
root.geometry ("250x300")

tk.Label (root, text="Menu da Agenda", font = ("Arial", 15)).pack (pady = 15)
tk.Button (root, text="Cadastrar Contato", width= 30, command= cadastrarcontato).pack (pady = 3)
tk.Button (root, text="Listar Contato", width= 30, command= listarcontato).pack (pady = 3)
tk.Button (root, text="Deletar Contato", width= 30, command= deletarcontato).pack (pady = 3)
tk.Button (root, text="Buscar Contato Pelo Nome", width= 30, command= buscarcontatopelonome).pack (pady = 3)
tk.Button (root, text="Fechar", width= 30, command= fechar).pack (pady = 25)


root.mainloop()