import csv
import os
from time import sleep
import pandas as pd
from pip import main

filme = {}

def filmes():

    def cadastrar_filme(): 

        nome = input("Digite seu nome: ")
        ano = input("Digite seu ano: ")
        categoria = input("Digite a categoria: ")

        filme[nome] = [ano, categoria]

        colunas = ['ano', 'nome', 'categoria']
        file_exists = os.path.isfile('filme.csv')
        with open('filme.csv', 'a', newline='') as filme_csv:
            cadastrar = csv.DictWriter(
                filme_csv, fieldnames=colunas, delimiter=',', lineterminator='\r\n') 
            if not file_exists:
                cadastrar.writeheader()
            cadastrar.writerow(
                {'ano': ano, 'nome': nome.title(), 'categoria': categoria})

        print('Cadastro realizado com sucesso!')
        return


    def editar_filme():  
        url = './filme.csv'
        df = pd.read_csv(url)
        print(df) #IMPRIME A LISTA DE FILMES NO TERMINAL, PRA PESSOA SABER O ID

        line_count = 0      
        idFilme = int(input("Digite o id do filme que vc quer ditar: "))  #PERGUNTA O ID QUE A PESSOA QUER EDITAR
        idFilme += 2
        newName = (input("Digite o novo filme: "))
        newYear= int(input("Digite o ano: "))  #ARMAZENA AS NOVAS INFORMACOES EM VARIAVEIS
        newCate = (input("Digite a categoria: "))


        with open("filme.csv", 'r') as f: #ABRE O CSV
            reader = csv.reader(f, delimiter=',')

            lines = [] #VETOR LINES
            for line in reader:
                    line_count += 1
                    if idFilme == line_count: #CHECA SE O ID E IGUAL A LINHA DO CSV
                        line[0] = newYear #SETA AS NOVAS INFORMACOES NO VETOR LINE
                        line[1] = newName
                        line[2] = newCate
                    lines.append(line) #VETOR LINES PUXA O LINE

        with open("filme.csv", 'w', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerows(lines)  #ESCREVE AS NOVAS INFORMACOES DO LINES NO CSV
        return #VOLTA PARA O MENU FILMES


    def excluir_filme():
        url = './filme.csv'
        df = pd.read_csv(url)
        print(df) #IMPRIME A LISTA DE filme NO TERMINAL, PRA PESSOA SABER O ID

        line_count = 0      
        idFilme = int(input("Digite o id do filme que vc deseja excluir: "))  #PERGUNTA O ID QUE A PESSOA QUER EXCLUIR
        idFilme += 2

        with open("filme.csv", 'r') as f: #ABRE O CSV
            reader = csv.reader(f, delimiter=',')

            lines = [] #VETOR LINES
            for line in reader:
                    line_count += 1
                    if idFilme == line_count: #CHECA SE O ID E IGUAL A LINHA DO CSV
                        contador = line_count -1
                    lines.append(line) #VETOR LINES PUXA O LINE
                    
        del lines[contador]
        with open("filme.csv", 'w', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerows(lines)  #ESCREVE AS NOVAS INFORMACOES DO LINES NO CSV
        return #VOLTA PARA O MENU
                


    def pesquisar_filme():
        nome = input("Qual filme deseja localizar? (Digite o nome): ")
        with open('filme.csv') as filme_csv:
            reader_obj = csv.reader(filme_csv, delimiter=',')

            linhas = float
            linhas = 0
            for coluna in reader_obj:
                if linhas == 0:
                    linhas += 1
                else:
                    if coluna[1] == nome:
                        pesquisado = coluna[1]
                        print(f"Nome: {pesquisado} | Ano: {coluna[0]} | Categoria: {coluna[2]}")
                        return
                    else:
                        linhas += 1
            print("Filme não localizado")
            return


    def lista_de_filme():
        url = './filme.csv'
        df = pd.read_csv(url)

        print(df)
        return

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
                        nf = input('Nome do filme: ')

                        colunas = ['codigo do filme', 'cpf', 'nome', 'data', 'nome do filme']  # colunas da tabela .csv
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
        print('\n------ Devoluçao ------\n')
        while True:
            days = int(input("Digite os dias de aluguel: "))
            if isnumber(days):
                valor = days * 2
                excluir_filme()
                print("O valor final a pagar e de {}R$".format(valor))
                break
            else:
                print('\033[31mERRO!\033[m')
        return None
        

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
                        cadastrar_filme()
                    elif opt == 2:
                        editar_filme()
                    elif opt == 3:
                        excluir_filme()
                    elif opt == 4:
                        alguem = pesquisar_filme()
                        if alguem != None:
                            print(alguem)
                    elif opt == 5:
                        lista_de_filme()
                    elif opt == 6:
                        realizar_emprestimo()
                    elif opt == 7:
                        listar_emprestimos()
                    elif opt == 8:
                        checkout()
                    elif opt == 9:
                        break

            except ValueError:
                print('\033[31mERRO!\033[m')
                
                
    ops = ( "1. Cadastrar filme",
            "2. Editar filme",
            "3. Excluir filme",
            "4. Pesquisar filme",
            "5. Listar filmes",
            "6. Registrar empréstimo",
            "7. Listar Empréstimos",
            "8. Devoluçao",
            "9. Sair")

    start(ops)
