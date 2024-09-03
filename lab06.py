'''
lista = []

nome1 = input("Digite um nome: ")
lista.append(nome1)
nome2 = input("Digite um nome: ")
lista.append(nome2)

lista.sort()

if nome1 and not nome2 in lista:
    print(f"Sim, {nome1} está na lista.")
else:
    print(f"Não, {nome1} não está na lista.")


if not nome2 == "boom" and not nome1 == "john":
    print("Fomos!")
else:
    print("Nao...")

for i in zip(vars):
    globals()[vars[test]]
'''

lista = [3,4,5,6,7]
lista.sort(reversed)
print(lista)