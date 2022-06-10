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
        #falta validar o cpf (cpf teste: 11111111111)
        cpf = input("Digite o cpf: ")
        pessoa = {
            "nome": nome,
            "idade": idade,
            "cpf": cpf
        }
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
            #excluindo pessoa
            for i in range(len(pessoas) -1): #para i dentro da lista pessoas
                if pessoas[i] == alone: 
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
