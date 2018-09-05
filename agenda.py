from funcoes import *

opt = 0
contato = ""
tel = ""
while opt != 5:
    bemvindo()
    opt = int(input("Digite a opção desejada: "))
    print("\n")

    if opt == 1: #adicionar
        contato = input("Insira o nome do contato que será adicionado: ")
        tel = input("Insira o número de telefone do contato: ")
        adicionar(contato, tel)
    elif opt == 2: #listar
        listarR()
    elif opt == 3: #deletar
        contato = input("Insira o nome do contato que será deletado: ")
        deletar(contato)
    elif opt == 4: #buscar
        contato = input("Insira o nome do contato que será buscado: ")
        encontrar(contato)
    elif opt == 5: #encerrar
        print("Encerrando aplicação.")
    elif opt < 1 or opt > 5: #opção invalida
        falha()
