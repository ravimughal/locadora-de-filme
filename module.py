import csv

def cliente():
    def menu(ops):
        print("-" * 30)
        for op in ops:
            print(op)
        print("-" * 30)
        op = int(input("Qual opção deseja escolher: "))
        return op

    def cadastrar_pessoa():
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        idade = str(idade)
        # falta validar o cpf (cpf teste: 11111111111)
        cpf = input("Digite o cpf: ")

        pessoa = {
            "nome": nome,
            "idade": idade,
            "cpf": cpf
        }

        fields = ['Nome', 'Idade', 'CPF']   
      
        rows = [[nome, idade, cpf], ]  
            
        filename = "university_records.csv"
            
        with open(filename, 'w', newline='') as csvfile:   
            
            csvwriter = csv.writer(csvfile)   
                
            
            csvwriter.writerow(fields)   
                
            
            csvwriter.writerows(rows) 




        print("Pessoa cadastrada com sucesso")
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

def filmes():
    def menu(ops):
        print("-" * 30)
        for op in ops:
            print(op)
        print("-" * 30)
        op = int(input("Qual opção deseja escolher: "))
        return op

    def cadastrar_filme():
        nome = input("Digite o nome: ")
        ano = int(input("Digite o ano de lançamento: "))
        #falta validar o cpf (cpf teste: 11111111111)
        categoria = input("Digite a categoria do filme: ")
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
            #excluindo filme
            for i in range(len(filmes) -1): #para i dentro da lista filmes
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

def jogos():
    def menu(ops):
        print("-" * 30)
        for op in ops:
            print(op)
        print("-" * 30)
        op = int(input("Qual opção deseja escolher: "))
        return op

    def cadastrar_jogo():
        nome = input("Digite o nome: ")
        ano = int(input("Digite o ano de lançamento: "))
        #falta validar o cpf (cpf teste: 11111111111)
        categoria = input("Digite a categoria do jogo: ")
        jogo = {
            "nome": nome,
            "ano": ano,
            "categoria": categoria
        }
        return jogo

    def editar_jogo(jogos):
        alguem = pesquisar_jogo(jogos)
        if alguem == None:
            print("jogo não localizada.")
            op = input("Gostaria de cadastrá-la? (s/n)")
            if op == "s":
                return cadastrar_jogo()
            else:
                return None
        else:
            for i in range(len(jogos) - 1):
                if jogos[i] == alguem:
                    del(jogos[i])
            cadastrar_jogo()        

    def excluir_jogo(jogos):
        alone = pesquisar_jogo(jogos)
        if alone == None:
            print("jogo não localizadas.")
        else:
            #excluindo jogo
            for i in range(len(jogos) -1): #para i dentro da lista jogos
                if jogos[i] == alone: 
                    del(jogos[i])

    def pesquisar_jogo(jogos):
        nome = input("Qual jogo deseja localizar? (Digite o nome)")
        for jogo in jogos:
            if jogo["nome"] == nome:
                return jogo
        return None

    def start(ops, jogos):
        while True:
            op = menu(ops)
            if op == 1:
                jogo = cadastrar_jogo()
                jogos.append(jogo)
            elif op == 2:
                jogo = editar_jogo(jogos)
            elif op == 3:
                alone = excluir_jogo(jogos)
            elif op == 4:
                alguem = pesquisar_jogo(jogos)
                if alguem != None:
                    print(alguem)
            elif op == 5:
                break

    jogos = []
    ops = ("1. Cadastrar jogo",
            "2. Editar jogo",
            "3. Excluir jogo",
            "4. Pesquisar jogo",
            "5. Sair")
    start(ops, jogos)
    print(jogos)