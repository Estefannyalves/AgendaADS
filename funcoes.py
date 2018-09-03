import csv       

def deletar():
        with open("agendatelefonica.csv","r") as agenda:
                reader = csv.reader(agenda)
                data = list(reader)
        nome=str("")
        while nome not in ([row[0] for row in data]):
                nome = input("Nome do contato a ser deletado: ")
        data.pop([row[0] for row in data].index(nome))
        with open("agendatelefonica.csv","w",newline="") as file:
                writer = csv.writer(file)
                for row in data :
                        writer.writerow(row)
        print("\n")
        print("Contato removido com sucesso!!")
        print("\n")

def falha():
	print("Selecione uma opção válida.")
	print("\n")

def encontrar(busca):
    agenda = open("agendatelefonica.csv")
    lista = (agenda.readlines())
    nome = False
    for i in range (0,len(lista)):
        if busca in lista[i]:
                print("\n")
                print("O contato buscado é: ", lista[i])
                nome = True
                
    if nome == False:
            print("\n")
            print("Nome não encontrado")
            print("\n")
