'''
conteudo 
            - in ok
            - insert ok
            - append ok
            - lista[indice] = valor substituido ok
            - remove ok
            - if else elif ok                                              
'''
lista = [1,45,23,12,11,6,8,4,34,19,14]

#print[0]
#print[0:5]

#lista.sort
#lista.pop(5)
#del lista[2:]

nome = "tricia"
lista.append(nome)
print(lista)

#inserção
lista.insert(2, "santos") 
print(lista)

#substituição
lista[2] = 'lucas'
print(lista)

print('tricia' in lista)