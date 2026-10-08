#1 - crie uma list com 5 filmes favoritos, mostre o primeiro, o ultimo e o total
#2 - peça 5 numeros, guare em uma lista e mostre o maior, menor e a soma (max, min, sum)
numeros = []
for i in range(5):
    numero.append(int(input(f'numero { i + 1 }:')))
    print(f'maior: {max(numeros)} | menor: {min(numeros)}' )
#3 - crie uma diconario com os dados de um celular (marca, modelo, preço) e mostre cada par chave-valor com for chave, valor in dicionario.items()