import csv
import enum
import os

pessoa = {}

def cliente():
    def menu(ops):
        print("-" * 30)
        for op in ops:
            print(op)
        print("-" * 30)
        op = int(input("Qual opção deseja escolher: "))
        return op

    def cadastrar_pessoa():
        

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

    def editar_pessoa():
        alguem = pesquisar_pessoa()
        if alguem == None:
            print("Pessoa não localizada.")
            op = input("Gostaria de cadastrá-la? (s/n)")
            if op == "s":
                return cadastrar_pessoa()
            else:
                return None
        else:
            for i in range(len() - 1):
                if [i] == alguem:
                    del([i])
            cadastrar_pessoa()

    def excluir_pessoa():
        alone = pesquisar_pessoa()
        if alone == None:
            print("Pessoa não localizadas.")
        else:
            # excluindo pessoa
            for i in range(len()):  # para i dentro da lista 
                if [i] == alone:
                    conf = input("Deseja confirmar exclusão? (s/n)")
                    if conf in "Ss":
                        del([i])

    def pesquisar_pessoa():
        cpf = input("Qual pessoa deseja localizar? (Digite o cpf)")
        with open('clientes.csv') as clientes_csv:
            reader_obj = csv.reader(clientes_csv, delimiter=';')
      
            # Iterate over each row in the csv file
            # using reader object
            linhas = 0
            
            for coluna in reader_obj:
                if linhas == 0:
                    linhas += 1
                else:
                    if coluna[0] == cpf:
                        print(f"Nome: {coluna[1]}")

                
        
        


    def start(ops):
        while True:
            op = menu(ops)
            if op == 1:
                cadastrar_pessoa()
            elif op == 2:
                editar_pessoa()
            elif op == 3:
                excluir_pessoa()
            elif op == 4:
                alguem = pesquisar_pessoa()
                if alguem != None:
                    print(alguem)
            elif op == 5:
                break

    ops = ("1. Cadastrar pessoa",
           "2. Editar pessoa",
           "3. Excluir pessoa",
           "4. Pesquisar pessoa",
           "5. Sair")
    start(ops)
