from funcoes import *

#teste unitário função adicionar e deletar

print("Agenda antes do teste: ")
print("\n")

listarR() #agenda base

print("Adicionando valor teste...")
print("\n")

adicionar("teste","teste") #valor de teste adicionado

print("Listando agenda após adicionar valor teste: ")
print("\n")

listarR() #validando valor adicionado a lista

print("Deletando valor teste...")
print("\n")

deletar("teste") #valor de teste deletado

print("Listando agenda após deletar valor teste: ")
print("\n")

listarR() #validando remoção do valor de teste

a = input("Teste concluído. Pressione ENTER para encerrar.")
