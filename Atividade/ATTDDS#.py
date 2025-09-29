import os
import sys
def menu():
    print ("--- Menu ---")
    print("1. Cadastrar Aluno")
    print("2. Atualizar Dados do Aluno")
    print("3. Remover Aluno")
    print("4. Consultar Dados do Aluno")
    print("5. Dados Gerais")
    print("6. Sair")
    
    escolha=input ("Selecione a ação desejada: ")
    
    match escolha:
        case "1":
            cadastroAlunos()
        case "2":
            Atualizar_dados()
        case "3":
            removerPorId()
        case "4":
            procurarPorId()
        case "5":
            dados_gerais()
        case "6":
            os.system('cls')
            print ("Saindo do programa...")
            sys.exit()
        case _:
            os.system('cls')
            print("Selecione uma opção válida\n")
            menu()
menu()     


def cadastroAlunos(nome, serie):
    print('==========CADASTRO DE ALUNO==========\n')
    nome = str(input('Insira o nome do aluno:'))

    os.system('cls')

    print('==========CADASTRO DE ALUNO==========\n')
    print('\n[1] 1º Série   [2] 2º Série   [3] 3º Série')
    serie = int(input('Insira a sua série: '))
    '''XXXXXXX(nome, serie)'''

def removerPorId():
    id = input("Digite o id do aluno que deseja remover: ")
    
    """XXXXXXX(id)"""
    
def procurarPorId():
    id = input("Digite o id do aluno que deseja buscar: ")

    """XXXXXXX(id)"""

def procurarPorSerie
    serie = input("Digite a serie que deseja buscar: ")
    if serie > 3 or serie < 1:
         print("Serie invalida")
         menu()
    else:
         '''XXXXX(serie)'''

