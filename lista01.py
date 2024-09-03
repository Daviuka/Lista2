print("\n")
# Declaramos uma variável e craimos uma lista
lista = [5,8,2,9,1]
print(20*"-")
#Ordem crescente
lista.sort(reverse=False)
print(lista)
print(20*"-")
#Ordem decrescente
lista.sort(reverse=True)
print(lista)
print(20*"-")
lista.sort(reverse=False)
#adicionar na lista
lista.append(7)
print(lista)
print(20*"-")
#inserção
lista.insert(2, 3)
print(lista)
print(20*"-")
#substituição
lista[1] = 10
print(lista)
print(20*"-")
#remover o elemento da lista
lista.remove(9)
print(lista)
print(20*"-")
#Remover aas posições
del lista[2:5]
print(lista)
print(20*"-")
print("\n")