# import random

# numero_secreto = 7
# chute = int(input('Escolha um numero de 1 a 10'))
# print(f'Você escolheu o numro: {chute}')

# if chute > numero_secreto:
#     print('Você acertou')
# elif chute < numero_secreto:
#     print('Você errou! Tente um numero menor')    
# else:
#     print('Você errou! tente um numero maior')   

numero_secreto = random.randint(1, 20)

print('Tente adivinhar o número que estou pensando... Entre 1 e 20. Você tem 5 tentativas')

for tentativa in range(1, 6):
    chute = int(input('Seu palpite: '))

    if chute < numero_secreto:
        print('Você erro! Tente um número maior')
    elif chute > numero_secreto:
        print('Você errou! Tente um número menor')    
    else:
        print(f'Acertou em {tentativas} tentativas(s)')    
    break
else:
    print(f'Acabaram as tentativas. O número era {numero_secreto}')

# while True:
#     chute = int(input('Seu palpite: '))
#     tentativas += 1

#     if chute < numero_secreto:
#         print('Você errou! Tente um número maior')
#     elif chute > numero_secreto:
#         print('Você errou! Tente um número menor')    
#     else:
#         print(f'Acertou em {tentativas} tentativas(s)')    
#         break

