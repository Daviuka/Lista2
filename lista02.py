print("\n")
print(30*'-')
lista = ['Janeiro', 'Fevereiro', 'Março', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
if 'Junho' in lista:
    #esse bloco só será executado quando a condição é True
    print("Sim, o Junho está na lista.")
else: 
     #esse bloco só será executado quando a condição é False
    print("Não, o Junho não está na lista.")
print(30*'-')
#inserção
lista.insert(3, 'Abril')
print(lista)
print(30*'-')
#substituição
lista[6] = 'Dezembro'
print(lista)
print(30*'-')
#remover o elemento da lista
lista.pop(11)
print(lista)
print(20*"-")
print('\n')