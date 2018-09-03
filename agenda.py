from funcoes import *

opt = 0
contato = ""
while opt != 5:
    bemvindo()
    opt = int(input("Digite a opção desejada: "))
    print("\n")

    if opt == 1:
        adicionar()
    elif opt == 2:
        listarR()
    elif opt == 3:
        deletar()
    elif opt == 4:
        contato = input("Insira o nome do contato que será buscado: ")
        encontrar(contato)
    elif opt == 5:
        print("Encerrando aplicação.")
    elif opt < 1 or opt > 5:
        falha()
