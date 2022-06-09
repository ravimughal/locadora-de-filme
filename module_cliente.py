def cliente():
    print("funcionando")
    def menu(ops):
        print("*" * 30)
        for op in ops:
            print(op)
        print("*" * 30)
        op = int(input("Qual opção deseja escolher: "))
        return op

    def cadastrar_pessoa():
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        cidade = input("Digite a cidade: ")
        pessoa = {
            "nome": nome,
            "idade": idade,
            "cidade": cidade
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
            pass


    def excluir_pessoa(pessoas, nome):
        alone = pesquisar_pessoa(pessoas)
        if alone == None:
            print("Pessoa não localizadas.")
        else:
            del pessoas[nome]


    def pesquisar_pessoa(pessoas):
        nome = input("Qual pessoa deseja localizar? ")
        for pessoa in pessoas:
            if pessoa["nome"] == nome:
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


    if __name__ == '__main__':
        pessoas = []
        ops = ("1. Cadastrar pessoa",
            "2. Editar pessoa",
            "3. Excluir pessoa",
            "4. Pesquisar pessoa",
            "5. Sair")
        start(ops, pessoas)
        print(pessoas)
