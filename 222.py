from datetime import datetime
import csv
import os


# -----------------------------------------------------------------------------
# Função para cadastro de novos clientes
def cadastrar_cliente():
    dados = {}

    nome = input("Nome.......: ")
    cpf = input("CPF........: ")
    rg = input("RG.........: ")

    dados[cpf] = [nome, rg]

    colunas = ['cpf', 'nome', 'rg']
    file_exists = os.path.isfile('clientes.csv')
    with open('clientes.csv', 'a', newline='') as clientes_csv:
        cadastrar = csv.DictWriter(clientes_csv, fieldnames=colunas, delimiter=';', lineterminator='\r\n')
        if not file_exists:
            cadastrar.writeheader()
        cadastrar.writerow({'cpf': cpf, 'nome': nome.title(), 'rg': rg})

    print('Cadastro realizado com sucesso!')

    print('Cadastro realizado com sucesso!')


# -----------------------------------------------------------------------------
# Função para listar todos os clientes
def listar_clientes():
    clientes_csv = open('clientes.csv')
    dados = csv.DictReader(clientes_csv, delimiter=';')

    os.system('cls') or None
    print('-------------------------------------------------------')
    print('LISTAGEM DE CLIENTES')
    print('-------------------------------------------------------')
    print(f'{"CPF":15}', f'{"NOME":25}', "RG")
    for cliente in dados:
        print(f'{cliente["cpf"]:15}', f'{cliente["nome"]:25}', cliente["rg"])
    clientes_csv.close()
    print('-------------------------------------------------------')


# -----------------------------------------------------------------------------
# Função para cadastro de novos filmes
def cadastrar_filme():
    os.system('cls') or None
    print('\n------ CADASTRO DE FILMES/TÍTULOS ------\n')
    cadastro = {}
    codigo = input("Codigo.......: ")
    tipo = input("DVD/Fita.....: ")
    nome_filme = input("Titulo.......: ")
    ano_lancamento = input("Ano..........: ")

    cadastro[codigo] = [tipo, nome_filme, ano_lancamento]  # Salva os dados em um dicionário

    filmes_csv = open("filmes.csv", "a")
    filmes_csv.write(f"{codigo};{tipo.upper()};{nome_filme.title()};{ano_lancamento}\n")
    filmes_csv.close()


# -----------------------------------------------------------------------------
# Função para listar todos os filmes
def listar_filmes():
    os.system('cls') or None
    filmes_csv = open('filmes.csv')
    dados = csv.DictReader(filmes_csv, delimiter=';')

    print('----------------------------------------------------------------')
    print('LISTAGEM DE FILMES/TÍTULOS')
    print('----------------------------------------------------------------')
    print(f'{"CODIGO":10}', f'{"TIPO":10}', f'{"NOME DO FILME":30}', "ANO")
    print('----------------------------------------------------------------')
    for filme in dados:
        print(f'{filme["codigo"]:10}', f'{filme["tipo"]:10}', f'{filme["nome_filme"]:30}', filme["ano_lancamento"])
    filmes_csv.close()
    print('----------------------------------------------------------------')


# -----------------------------------------------------------------------------
# Função para realizar locação/emprestimos de filmes
def realizar_emprestimo():
    os.system('cls') or None
    print('\n------ EMPRÉSTIMOS ------\n')
    cadastro = {}
    nome_usuario = input("Nome do Cliente.......................: ")
    codigo_filme = input("Codigo do Filme.......................: ")
    data_emprestimo = input("Data de Emprestimo (dd/mm/aaaa).......: ")

    cadastro = {'nome_usuario': nome_usuario.title(), 'codigo_filme': codigo_filme, 'data_emprestimo': data_emprestimo}
    emprestimos_csv = open("emprestimos.csv", "a")
    emprestimos_csv.write(f"{nome_usuario};{codigo_filme};{data_emprestimo}\n")
    emprestimos_csv.close()


# -----------------------------------------------------------------------------
# Função para listagem de locações
def listar_emprestimos():
    emprestimos_csv = open('emprestimos.csv')
    dados = csv.DictReader(emprestimos_csv, delimiter=';')

    os.system('cls') or None
    print('----------------------------------------------------------------')
    print('FILMES EMPRESTADOS')
    print('----------------------------------------------------------------')
    print(f'{"CLIENTE":25}', f'{"CODIGO FILME":20}', "DATA EMPRESTIMO")
    for emprestimo in dados:
        print(f'{emprestimo["nome_usuario"]:25}', f'{emprestimo["codigo_filme"]:20}', emprestimo["data_emprestimo"])
    emprestimos_csv.close()
    print('----------------------------------------------------------------')


# -----------------------------------------------------------------------------
# Função para pesquisar o CPF de um CLIENTE dado seu NOME
def pesquisar_cliente(nome_cliente):
    clientes_csv = open('clientes.csv')
    dados_clientes = csv.DictReader(clientes_csv, delimiter=';')

    for cliente in dados_clientes:
        if cliente["nome"] == nome_cliente:
            cpf = cliente["cpf"]
            return cpf
            break
    clientes_csv.close()


# -----------------------------------------------------------------------------
# Função para pesquisar o NOME de um FILME dado seu CÓDIGO
def pesquisar_filme(codigo_filme):
    filmes_csv = open('filmes.csv')
    dados_filmes = csv.DictReader(filmes_csv, delimiter=';')

    for filme in dados_filmes:
        if filme['codigo'] == codigo_filme:
            nome_filme = filme['nome_filme']
            return nome_filme
            break
    filmes_csv.close()


# -----------------------------------------------------------------------------
# Função para consulta aos dados de empréstimos e montagem do relatório de atrasados
def relatorio_atrasados():
    emprestimos_csv = open('emprestimos.csv')
    dados_emprestimos = csv.DictReader(emprestimos_csv, delimiter=';')
    relatorio = {}

    os.system('cls') or None
    print('------------------------------------------------------------------------------------------------')
    print('RELATÓRIO DE FILMES ATRASADOS NA DEVOLUÇÃO')
    print('------------------------------------------------------------------------------------------------')
    print(f'{"CPF":15}', f'{"NOME":15}', f'{"TITULO":25}', f'{"EMPRESTIMO":15}', f'{"SITUACAO":10}', "DIAS")
    print('------------------------------------------------------------------------------------------------')
    for emprestimo in dados_emprestimos:
        data_emprestimo = datetime.strptime(emprestimo["data_emprestimo"], '%d/%m/%Y')
        data_hoje = datetime.today()
        dias = (data_hoje - data_emprestimo).days

        if dias > 7:
            situacao = 'Atrasado'
            cpf = str(pesquisar_cliente(emprestimo["nome_usuario"]))
            nome_filme = pesquisar_filme(emprestimo['codigo_filme'])

            print(f'{cpf:15}',
                  f'{str(emprestimo["nome_usuario"]):15}',
                  f'{str(nome_filme):25}',
                  f'{emprestimo["data_emprestimo"]:15}',
                  f'{situacao:10}',
                  f'{str(dias - 7):5}')
    print('------------------------------------------------------------------------------------------------')


# -----------------------------------------------------------------------------
# Início do Programa Principal
resposta = 's'
while resposta == 's':
    os.system('cls') or None

    # ---------- Menu Principal --------------
    menu = '''------ LOCADORA LAZYWAX ------\n
	\r[1] Cadastrar Cliente
	\r[2] Lista de Clientes
	\r[3] Cadastrar Filme
	\r[4] Lista de Filmes
	\r[5] Realizar Empréstimo
	\r[6] Lista de Empréstimos
	\r[7] Relatório de Atrasados		   
	'''
    print(menu)
    opcao = int(input('\nEscolha uma opção: '))

    if opcao == 1:
        cadastrar_cliente()
    elif opcao == 2:
        listar_clientes()
    elif opcao == 3:
        cadastrar_filme()
    elif opcao == 4:
        listar_filmes()
    elif opcao == 5:
        realizar_emprestimo()
    elif opcao == 6:
        listar_emprestimos()
    elif opcao == 7:
        relatorio_atrasados()
    else:
        print('Opção Inválida!')

    resposta = str(input('\n\nDeseja continuar? [s/n] '))

print('\nObrigado!\n')