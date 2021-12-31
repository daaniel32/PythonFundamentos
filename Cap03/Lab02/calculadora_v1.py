# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

def soma(x, y):
    return x + y

def sub(x, y):
    return  x - y

def div(x,y):
    return x / y

def mult(x,y):
    return x * y

print('Digite o número da operação desejada: ')
print('1 - Soma')
print('2 - Subtração')
print('3 - Divisão')
print('4 - Multiplicação')

op = input(' \nDigite a sua opção (1/2/3/4): ')

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if op == '1':
    print('\n')
    print(num1, "+ ", num2, "=" , soma(num1, num2))
    print('\n')

elif op == '2':
    print('\n')
    print(num2, "-", num2, "=", sub(num1, num2))
    print('\n')

elif op == '3':
    print('\n')
    print(num2, "/", num2, "=", div(num1, num2))
    print('\n')

elif op == '4':
    print('\n')
    print(num2, "*", num2, "=", sub(num1, num2))
    print('\n')

else:
    print("Opção Inválida")
    print('\n')
    print("Digite uma Opção Válida")

