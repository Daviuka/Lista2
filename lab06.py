lista = []

nome1 = input(' digite um nome: ')
lista.append(nome1)

nome2 = input('digite um nome: ')
lista.append(nome2)
 
lista.sort()

if nome1 in lista:
    print(f'Sim, o {nome1} e o {nome2} está adicionado na lista.')
else:
    print(f'Não, o {nome1} e o {nome2} não está na lista')

num1 = 10
num2 = 20
 