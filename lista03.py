print('\n')
print(30*'-', ' BOLETIM ESCOLAR ', 30*'-')
#Declaramos a variável e criamos uma lista para colocar as informações do aluno
notas = []
# Aqui será colocado as notas que o aluno vai digitar
numero_usuario1 = int(input('Digite uma nota: '))
notas.append(numero_usuario1)

numero_usuario2 = int(input('Digite outra nota: '))
notas.append(numero_usuario2)

numero_usuario3 = int(input('Digite outra nota: '))
notas.append(numero_usuario3)

numero_usuario4 = int(input('Digite outra nota: '))
notas.append(numero_usuario4)

numero_usuario5 = int(input('Digite outra nota: '))
notas.append(numero_usuario5)

# len conta a quantidade de elementos dentro de uma lista
quantidade_notas = len(notas)

# sum irá sommar todos os valores da lista
soma = sum(notas)

# Cálculamos a média dividindo a soma das notas e a quantidade de notas que foi adcionado na lista
media = soma / quantidade_notas

# Depois colocamos as informações que foram adicionados e tammbém os resultaddos que foi cálculado
print(f'As notas: {notas}')
print(f'A quantidade de notas são: {quantidade_notas}')
print(f'A soma de todas as notas são: {soma}')
print(f'A média: {media}')

'''
    #TODO: Situação
    Aprovado >= 7
    Recuperação >=5
    reprovado
'''
# Para finalizar, precisamos declara se o aluno passou de ano, ficou de recperação ou foi reprovado
if media >= 7:
    print(f'Aprovado com média {media}')
elif media >= 5:
    print(f'Recuperação com média {media}')
else:
    print(f'Reprovado com média {media}')    

print(60*"-")