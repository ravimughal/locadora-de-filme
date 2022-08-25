import csv
import os
import pandas as pd
from pip import main

pessoa = {}


def cpf_validate(numbers):
    cpf = [int(char) for char in numbers if char.isdigit()]
    if len(cpf) != 11:
        return False
    if cpf == cpf[::-1]:
        return False

    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True


def cliente():

    def cadastrar_pessoa(): 

        nome = input("Digite seu nome: ")
        while True:
            cpf = input('Digite seu cpf: ')
            cpf = cpf if cpf_validate(cpf) else False
            if not cpf:
                print('DIGITE UM CPF VALIDO!')
            if cpf:
                break

        while True:  
            idade = input("Digite sua idade: ")            
            try:
                int(idade)
                it_is = True
            except ValueError:
                it_is = False
                print('Digite uma idade valida!')

            if it_is == True:
                numidade = int(idade)
                if numidade > 119:
                    print('Digite uma idade valida!')
                else:
                    break
            
        pessoa[cpf] = [nome, idade] #buscar cliente cadastrado através de cpf

        colunas = ['cpf', 'nome', 'idade'] #colunas da tabela .csv
        file_exists = os.path.isfile('clientes.csv')
        with open('clientes.csv', 'a', newline='') as clientes_csv:
            #DictWriter grava dados no formato de dicionário
            cadastrar = csv.DictWriter(
                clientes_csv, fieldnames=colunas, delimiter=',', lineterminator='\r\n') #fieldnames = nome de campos, ou seja -> colunas, divisor de dados sendo ';', lineterminator \r\n serve para quebrar a linha
            #caso não existe o arquivo 'file_exist', faz o fieldnames funcionar, visto que há o 'writeheader()'
            if not file_exists:
                #writeheader grava a primeira linha de arquivo csv usando os nomes de campo pré-especificados.
                cadastrar.writeheader()
            # escrever nas linhas em respectivas 'keys' e 'values', title() -> deixar letra maiuscula
            cadastrar.writerow(
                {'cpf': cpf, 'nome': nome.title(), 'idade': idade})

        print('Cadastro realizado com sucesso!')
        return

    def editar_pessoa():  
        url = './clientes.csv'
        df = pd.read_csv(url)
        print(df) #IMPRIME A LISTA DE CLIENTES NO TERMINAL, PRA PESSOA SABER O ID

        line_count = 0      
        idClient = int(input("Digite o id do cliente que vc quer ditar:"))  #PERGUNTA O ID QUE A PESSOA QUER EDITAR
        idClient += 2
        newName = (input("Digite o novo nome: "))
        newCpf= int(input("Digite o novo cpf: "))  #ARMAZENA AS NOVAS INFORMACOES EM VARIAVEIS
        newAge = (input("Digite a nova idade: "))


        with open("clientes.csv", 'r') as f: #ABRE O CSV
            reader = csv.reader(f, delimiter=',')

            lines = [] #VETOR LINES
            for line in reader:
                    line_count += 1
                    if idClient == line_count: #CHECA SE O ID E IGUAL A LINHA DO CSV
                        line[0] = newCpf #SETA AS NOVAS INFORMACOES NO VETOR LINE
                        line[1] = newName
                        line[2] = newAge
                    lines.append(line) #VETOR LINES PUXA O LINE

        with open("clientes.csv", 'w', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerows(lines)  #ESCREVE AS NOVAS INFORMACOES DO LINES NO CSV
        return #VOLTA PARA O MENU CLIENTES


    def excluir_pessoa():
        url = './clientes.csv'
        df = pd.read_csv(url)
        print(df) #IMPRIME A LISTA DE CLIENTES NO TERMINAL, PRA PESSOA SABER O ID

        line_count = 0      
        idClient = int(input("Digite o id do cliente que vc deseja excluir: "))  #PERGUNTA O ID QUE A PESSOA QUER EXCLUIR
        idClient += 2

        with open("clientes.csv", 'r') as f: #ABRE O CSV
            reader = csv.reader(f, delimiter=',')

            lines = [] #VETOR LINES
            for line in reader:
                    line_count += 1
                    if idClient == line_count: #CHECA SE O ID E IGUAL A LINHA DO CSV
                        contador = line_count -1
                    lines.append(line) #VETOR LINES PUXA O LINE
                    
        del lines[contador]
        with open("clientes.csv", 'w', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerows(lines)  #ESCREVE AS NOVAS INFORMACOES DO LINES NO CSV
        return #VOLTA PARA O MENU
                


    def pesquisar_pessoa():
        cpf = input("Qual pessoa deseja localizar? (Digite o cpf): ")
        with open('clientes.csv') as clientes_csv:
            reader_obj = csv.reader(clientes_csv, delimiter=',')

            linhas = float
            linhas = 0
            for coluna in reader_obj:
                if linhas == 0:
                    linhas += 1
                else:
                    if coluna[0] == cpf:
                        pesquisado = coluna[1]
                        print(f"Nome: {pesquisado} | idade: {coluna[2]}")
                        return
                    else:
                        linhas += 1
            print("Pessoa não localizada")
            return


    def lista_de_clientes():
        url = './clientes.csv'
        df = pd.read_csv(url)

        print(df)
        return

    def isnumber(value):
        try:
            float(value)
        except ValueError:
            return False
        return True

    def start(ops):
        while True:

            print("-" * 30)
            for op in ops:
                print(op)
            print("-" * 30)
            
            try:    
                opt = int(input("Qual opção deseja escolher: "))
                if isnumber(opt):
                    if opt == 1:
                        cadastrar_pessoa()
                    elif opt == 2:
                        editar_pessoa()
                    elif opt == 3:
                        excluir_pessoa()
                    elif opt == 4:
                        alguem = pesquisar_pessoa()
                        if alguem != None:
                            print(alguem)
                    elif opt == 5:
                        lista_de_clientes()
                    elif opt == 6:
                        break
            except ValueError:
                print('\033[31mERRO!\033[m')
            

    ops = ("1. Cadastrar pessoa",
           "2. Editar pessoa",
           "3. Excluir pessoa",
           "4. Pesquisar pessoa",
           "5. Lista de clientes",
           "6. Sair")

    start(ops)

