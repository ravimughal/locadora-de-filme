import csv
import os
import pandas as pd


def filmes():
    def menu(ops):
        print("-" * 30)
        for op in ops:
            print(op)
        print("-" * 30)
        op = int(input("Qual opção deseja escolher: "))
        return op

    def cadastrar_filme():
        filme = {}

        nome = input("Digite seu nome: ")
        ano = input("Digite seu ano: ")
        categoria = input("Digite sua categoria: ")

        # buscar cliente cadastrado através de ano
        filme[ano] = [nome, categoria]

        colunas = ['ano', 'nome', 'categoria']  # colunas da tabela .csv
        file_exists = os.path.isfile('filmes.csv')
        with open('filmes.csv', 'a', newline='') as filmes_csv:
            # DictWriter grava dados no formato de dicionário
            cadastrar = csv.DictWriter(
                filmes_csv, fieldnames=colunas, delimiter=',', lineterminator='\r\n')  # fieldnames = nome de campos, ou seja -> colunas, divisor de dados sendo ',', lineterminator \r\n serve para quebrar a linha
            # caso não existe o arquivo 'file_exist', faz o fieldnames funcionar, visto que há o 'writeheader()'
            if not file_exists:
                # writeheader grava a primeira linha de arquivo csv usando os nomes de campo pré-especificados.
                cadastrar.writeheader()
            # escrever nas linhas em respectivas 'keys' e 'values', title() -> deixar letra maiuscula
            cadastrar.writerow(
                {'ano': ano, 'nome': nome.title(), 'categoria': categoria})

        print('Cadastro realizado com sucesso!')
        return filme

    def editar_filme(filmes):
        alguem = pesquisar_filme(filmes)
        if alguem == None:
            print("filme não localizada.")
            op = input("Gostaria de cadastrá-la? (s/n)")
            if op == "s":
                return cadastrar_filme()
            else:
                return None
        else:
            for i in range(len(filmes) - 1):
                if filmes[i] == alguem:
                    del(filmes[i])
            cadastrar_filme()

    def excluir_filme(filmes):
        alone = pesquisar_filme(filmes)
        if alone == None:
            print("filme não localizadas.")
        else:
            # excluindo filme
            for i in range(len(filmes) - 1):  # para i dentro da lista filmes
                if filmes[i] == alone:
                    del(filmes[i])

    def pesquisar_filme(filmes):
        nome = input("Qual filme deseja localizar? (Digite o nome)")
        for filme in filmes:
            if filme["nome"] == nome:
                return filme
        return None

    def listar_filme():
        url = './filmes.csv'
        df = pd.read_csv(url)

        print(df)

    def realizar_emprestimo():
        print('\n------ EMPRÉSTIMOS ------\n')
        cpf = input("Digite o cpf do cliente: ")
        with open('clientes.csv') as clientes_csv:
            reader_obj = csv.reader(clientes_csv, delimiter=',')

            linhas = 0
            for coluna in reader_obj:
                if linhas == 0:
                    linhas += 1
                else:
                    if coluna[0] == cpf:
                        pesquisado = coluna[1]
                        print(f"cpf: {pesquisado} | idade: {coluna[2]}")
                        codigo_filme = input("Digite seu codigo_filme: ")
                        data = input("Digite a data do filme: ")

                        colunas = ['codigo do filme', 'cpf', 'nome', 'data']  # colunas da tabela .csv
                        file_exists = os.path.isfile('emprestimo.csv')
                        with open('emprestimo.csv', 'a', newline='') as emprestimo_csv:
                            # DictWriter grava dados no formato de dicionário
                            cadastrar = csv.DictWriter(
                                emprestimo_csv, fieldnames=colunas, delimiter=',', lineterminator='\r\n')  # fieldnames = cpf de campos, ou seja -> colunas, divisor de dados sendo ';', lineterminator \r\n serve para quebrar a linha
                            # caso não existe o arquivo 'file_exist', faz o fieldnames funcionar, visto que há o 'writeheader()'
                            if not file_exists:
                                # writeheader grava a primeira linha de arquivo csv usando os cpfs de campo pré-especificados.
                                cadastrar.writeheader()
                            # escrever nas linhas em respectivas 'keys' e 'values', title() -> deixar letra maiuscula
                            cadastrar.writerow(
                                {'codigo do filme': codigo_filme, 'cpf': cpf, 'nome': pesquisado ,'data': data})

                        print('Cadastro realizado com sucesso!')
                        return pesquisado
                    else:
                        linhas += 1
            print("pessoa não localizada")
            return None

        
    
    def listar_emprestimos():
        url = './emprestimo.csv'
        df = pd.read_csv(url)
        print(df)


    def checkout():
        pass
        cpf = input("Digite o cpf do cliente: ")
        print('\n------ EMPRÉSTIMOS ------\n')
        cpf = input("Digite o cpf do cliente: ")
        with open('clientes.csv') as clientes_csv:
            reader_obj = csv.reader(clientes_csv, delimiter=',')

            linhas = 0
            for coluna in reader_obj:
                if linhas == 0:
                    linhas += 1
                else:
                    if coluna[0] == cpf:
                        pesquisado = coluna[1]
                        print(f"cpf: {pesquisado} | idade: {coluna[2]}")
                        codigo_filme = input("Digite seu codigo_filme: ")
                        #colocar situaçao de devolvido
                        #se nao emprestaram, puxar para emprestimo

    def calc_valor_final():
        pass
        # ligar com no emprestimo
        valor = 0
        days = int(input('Quantos dias sera alugado: '))
        if days <= 7:
            valor += 15
        elif days > 7:
            valor += 15 + days * 1.5

    def start(ops, filmes):
        while True:
            op = menu(ops)
            if op == 1:
                filme = cadastrar_filme()
                filmes.append(filme)
            elif op == 2:
                filme = editar_filme(filmes)
            elif op == 3:
                alone = excluir_filme(filmes)
            elif op == 4:
                alguem = pesquisar_filme(filmes)
                if alguem != None:
                    print(alguem)
            elif op == 5:
                listar_filme()
            elif op == 6:
                realizar_emprestimo()
            elif op == 7:
                listar_emprestimos()
            elif op == 8:
                checkout()
            elif op == 9:
                calc_valor_final()
            elif op ==10:
                break

    filmes = []
    ops = ( "1. Cadastrar filme",
            "2. Editar filme",
            "3. Excluir filme",
            "4. Pesquisar filme",
            "5. Listar filmes",
            "6. Registrar empréstimo",
            "7. Listar Empréstimos",
            "8. Checkout",
            "9. Valor do Empréstimo",
            "10. Sair")
    start(ops, filmes)
