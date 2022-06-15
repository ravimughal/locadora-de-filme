import csv
import os

def cliente():
    def menu(ops):
        print("-" * 30)
        for op in ops:
            print(op)
        print("-" * 30)
        op = int(input("Qual opção deseja escolher: "))
        return op

    def cadastrar_pessoa():
        pessoa = {}

        nome = input("Digite seu nome: ")
        cpf = input("Digite seu cpf: ")
        idade = input("Digite sua idade: ")

        pessoa[cpf] = [nome, idade] #buscar cliente cadastrado através de cpf

        colunas = ['cpf', 'nome', 'idade'] #colunas da tabela .csv
        file_exists = os.path.isfile('clientes.csv')
        with open('clientes.csv', 'a', newline='') as clientes_csv:
            #DictWriter grava dados no formato de dicionário
            cadastrar = csv.DictWriter(
                clientes_csv, fieldnames=colunas, delimiter=';', lineterminator='\r\n') #fieldnames = nome de campos, ou seja -> colunas, divisor de dados sendo ';', lineterminator \r\n serve para quebrar a linha
            #caso não existe o arquivo 'file_exist', faz o fieldnames funcionar, visto que há o 'writeheader()'
            if not file_exists:
                #writeheader grava a primeira linha de arquivo csv usando os nomes de campo pré-especificados.
                cadastrar.writeheader()
            # escrever nas linhas em respectivas 'keys' e 'values', title() -> deixar letra maiuscula
            cadastrar.writerow(
                {'cpf': cpf, 'nome': nome.title(), 'idade': idade})

        print('Cadastro realizado com sucesso!')
        return pessoa

    def editar_pessoa(pessoas):
        alguem = pesquisar_pessoa(pessoas)
        if alguem == None:
            print("Pessoa não localizada.")
            op = input("Gostaria de cadastrá-la? (s/n)")
            if op == "s":
                return cadastrar_pessoa()
            else:
                return None
        else:
            for i in range(len(pessoas) - 1):
                if pessoas[i] == alguem:
                    del(pessoas[i])
            cadastrar_pessoa()

    def excluir_pessoa(pessoas):
        alone = pesquisar_pessoa(pessoas)
        if alone == None:
            print("Pessoa não localizadas.")
        else:
            # excluindo pessoa
            for i in range(len(pessoas)):  # para i dentro da lista pessoas
                if pessoas[i] == alone:
                    conf = input("Deseja confirmar exclusão? (s/n)")
                    if conf in "Ss":
                        del(pessoas[i])

    def pesquisar_pessoa(pessoas):
        cpf = input("Qual pessoa deseja localizar? (Digite o cpf)")
        for pessoa in pessoas:
            if pessoa["cpf"] == cpf:
                return pessoa
        return None

    def start(ops, pessoas):
        while True:
            op = menu(ops)
            if op == 1:
                pessoa = cadastrar_pessoa()
                pessoas.append(pessoa)
            elif op == 2:
                pessoa = editar_pessoa(pessoas)
            elif op == 3:
                alone = excluir_pessoa(pessoas)
            elif op == 4:
                alguem = pesquisar_pessoa(pessoas)
                if alguem != None:
                    print(alguem)
            elif op == 5:
                break

    pessoas = []
    ops = ("1. Cadastrar pessoa",
           "2. Editar pessoa",
           "3. Excluir pessoa",
           "4. Pesquisar pessoa",
           "5. Sair")
    start(ops, pessoas)
    print(pessoas)