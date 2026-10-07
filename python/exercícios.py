#1 - peça o nome e idade e msotre:___, daqui há 10 anos voce tera X anos
#2 - peça uma temperatura em Celsius e converta para Fahrenheit (F = C * 9/5 + 32)
#3 - peça a base e a altura de um retangulo e mostre a area e o perimetro
#4 - peça 3 notas e mostre a media
#5 - refaça a calculadora IMC, colocando o seguinte:
#•  Baixo peso (magreza)
#• 18,5 a 24,9 kg/m²: Peso adequado (normal)
#• 25,0 a 29,9 kg/m²: Sobrepeso (pré-obesidade)
#• 30,0 a 34,9 kg/m²: Obesidade grau I
#• 35,0 a 39,9 kg/m²: Obesidade grau II
#• 40,0 kg/m² ou mais: Obesidade grau III (grave)

#1 
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
print(f'{nome}, daqui a 10 anos, voce tera {idade + 10} anos ')

#2
c = float(input('digite a temperatura em celsius: '))
f = c * 9 / 5 + 32
print(f'A temperatura {c} celsius fica {f:.2f}')

#3
base = float(input("digite a base do retângulo: "))
altura = float (input("digite a altura do retângulo: "))
area = base * altura 
perimetro = (base + altura) * 2
print(f'A area do retângulo é {area} e o perimetro é {perimetro}')

#4
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a  terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"Media: {media:.2f}")

#5
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / altura**2

if imc < 18.5:
    print('Abaixo do peso.')
elif imc >= 18.5 and imc <= 24.9:
    print('Peso normal.')
elif imc >= 25 and imc <= 29.9:
    print('Sobrepeso.')
elif imc >= 30 and imc <= 34.9:
    print('Obesidade grau I')
elif imc >= 35 and imc <= 39.9:
    print('Obesidade grau II')
else:
    print('Obesidade grau III')



