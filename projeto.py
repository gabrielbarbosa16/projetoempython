def menu ():
    opcao = input('''
=================================================
          PROJETO AGENDA EM PYTHON

MENU: 
          
[1]CADASTRAR CONTATO
[2]LISTAR CONTATO
[3]DELETAR CONTATO
[4]BUSCAR CONTATO PELO ID

=================================================
ESCOLHA UMA OPÇÃO ACIMA:
''')
    if opcao == '1':
        cadastrarcontato()
    elif opcao == '2':
        listarcontato()
    elif opcao == '3':
        deletarcontato()
    else:
        buscarcontato()

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
    print(f'Listar contato')

def deletarcontato():
    print(f'Deletar contato')

def buscarcontato():
    print(f'Buscar contato pelo ID')

def main():
    menu()

main()