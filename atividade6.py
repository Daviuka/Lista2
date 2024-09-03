print('\n')
print(30*'-')
num = []

num_usuario1 = int(input('Digite o primeiro número: '))
num.append(num_usuario1)

num_usuario2 = int(input('Digite o segundo número: '))
num.append(num_usuario2)

num_usuario3 = int(input('Digite o terceiro número: '))
num.append(num_usuario3)

num_usuario4 = int(input('Digite o quarto número: '))
num.append(num_usuario4)

quantidade_num = len(num)

num.sort()
print(num)

test1 = num[0]
test2 = num[3]

print(f"Maior: {test2}, Menor: {test1}")