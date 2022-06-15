import csv
import os

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
        nome = input("Digite o nome: ")
        ano = int(input("Digite o ano de lançamento: "))
        categoria = input("Digite a categoria do filme: ")
        filme[nome] =[ano,categoria]

        colunas = ['nome', 'ano', 'categoria'] 
        file_exists = os.path.isfile('filmes.csv')
        with open('filmes.csv', 'a', newline='') as filme_csv:
            cadastrar = csv.DictWriter(
                filme_csv, fieldnames=colunas, delimiter=';', lineterminator='\r\n')
        print('Cadastro realizado com sucesso!')
        return filme

        
        filme = {
            "nome": nome,
            "ano": ano,
            "categoria": categoria
        }
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
                break

    filmes = []
    ops = ("1. Cadastrar filme",
           "2. Editar filme",
           "3. Excluir filme",
           "4. Pesquisar filme",
           "5. Sair")
    start(ops, filmes)
    print(filmes)
