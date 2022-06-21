import module_cadastro
import module_filme
import module_jogos



print("\033[1;35m-\033[m"*100)
print("\033[1;35mLazywax\033[m")
print("\033[1;35mPucpr.BES.2022-1\033[m")
print()

print("\033[1;35mIntegrantes da equipe:\033[m")
print("\033[1;35mMateus Augusto Tozin, Julia Engels, R1avi Mughal, João Dadas e Felipe Gabriel\033[m")
print("\033[1;35m-\033[1;34m"*100)
# ---------------------------------------------------------------------------------------------

while True:

    print()
    print("\033[1;36mBem vindo ao menu principal!\033[m")
    print()
    print("\033[1;36m[1] Gerenciamento de cliente:\033[m")
    print("\033[1;36m[2] Gerenciamento de Filmes:\033[m")
    print("\033[1;36m[3] Gerenciamento de Jogos:\033[m")
    print("\033[1;36m[4] Sair do programa:\033[m")




    select = int(input("\033[1;36mSelecionar opção:\033[1;36m"))

    if select == 1:
        module_cadastro.cliente()
    elif select == 2:
        module_filme.filmes()
    elif select == 3:
        module_jogos.jogos()
    if select == 4:
        print("Nunca é um adeus :)")
        break