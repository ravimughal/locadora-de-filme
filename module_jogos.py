import csv
import os

def jogos():
    def menu(ops):
        print("-" * 30)
        for op in ops:
            print(op)
        print("-" * 30)
        op = int(input("Qual opção deseja escolher: "))
        return op

    def cadastrar_jogo():
        jogo = {}
        nome = input("Digite o nome: ")
        ano = int(input("Digite o ano de lançamento: "))
        categoria = input("Digite a categoria do jogo: ")
        jogo[ano] = [nome,categoria]
        
        

        return jogo

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
            # excluindo jogo
            for i in range(len(jogos) - 1):  # para i dentro da lista jogos
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