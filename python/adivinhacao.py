import random

numero_secreto = 7
chute = int(input('Escolha um numero de 1 a 10'))
print(f'Você escolheu o numro: {chute}')

if chute == numero_secreto:
    print('Você acertou')
elif chute > numero_secreto:
    print('Você errou! Tente um numero menor')    
else:
    print('Você errou! tente um numero maior')    