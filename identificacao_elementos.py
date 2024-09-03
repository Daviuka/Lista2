dias = ["Segunda","Terça","Quarta","Quinta","Sexta","Sabado","Domingo"]
nome = str(input("Digite o dia da semana: "))
if nome in dias:
    print("__________________________________________")
    print("EXERCICIO 05 - Identificação de Elementos |")
    print("￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣")
    print("::::::::::::::::::::::::::::::::::::")
    print(f"\"{nome}\" foi encontrado na lista.")
    print("::::::::::::::::::::::::::::::::::::\n")
else:
    print("__________________________________________")
    print("EXERCICIO 05 - Identificação de Elementos |")
    print("￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣")
    print(":::::::::::::::::::::::::::::::::::::::::::")
    print(f"\"{nome}\" não existe ou não foi encontrado.")
    print(":::::::::::::::::::::::::::::::::::::::::::\n")