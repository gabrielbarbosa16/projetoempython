def menu ():
    opcao = input('''
=================================================
          PROJETO AGENDA EM PYTHON

MENU: 
          
[1]CADASTRAR CONTATO
[2]LISTAR CONTATO
[3]DELETAR CONTATO
[4]BUSCAR CONTATO PELO NOME
[5]SAIR

=================================================
ESCOLHA UMA OPÇÃO ACIMA:
''')
    if opcao == '1':
        cadastrarcontato()
    elif opcao == '2':
        listarcontato()
    elif opcao == '3':
        deletarcontato()
    elif opcao == "4":
        buscarcontatopelonome()
    else:
        sair()

def cadastrarcontato():
    idcontato = input('Escolha ID do seu contato: ')
    nome = input('Escreva o nome do seu contato: ')
    telefone = input('Escreva o telefone do contato: ')
    email = input('Escreva o e-mail do contato: ')
    try:
        agenda = open("agenda.txt", "a")
        dados = f'{idcontato};{nome};{telefone};{email} \n'
        agenda.write(dados)
        agenda.close()
        print(f'Contato gravado com sucesso !!!')
    except:
        print('ERRO na gravação do contato')

def listarcontato():
    agenda = open("agenda.txt", "r")
    for contato in agenda: 
        print(contato)
    agenda.close()
    
def deletarcontato():
    nomedeletado = input("Digite o nome a ser deletado: ")
    agenda = open("agenda.txt","r")
    aux = []
    aux2 = []
    for i in agenda:
        aux.append(i)
    for i in range(0, len(aux)):
        if nomedeletado not in aux[i]:
            aux2.append(aux[i])
    agenda = open("agenda.txt", "w")
    for i in aux2:
        agenda.write(i)
    print(f'Contato deletado com sucesso')
    listarcontato()

def buscarcontatopelonome():
    nome = input(f'Digite o nome a ser procurado: ')
    agenda = open("agenda.txt", "r")
    for contato in agenda: 
        if nome in contato.split(";")[1]:
            print(contato)
    agenda.close()

def sair():
    print(f'Até mais.....!!!')
    exit()

def main():
    menu()

main()