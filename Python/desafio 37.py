num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] Binário
[2] Octal
[3] Hexadecimal''')
escolhido = int(input('Sua opção: '))
if escolhido == 1:
    print(f'O número {num} convertido em binário é: {bin(num)[2:]}.')
elif escolhido == 2:
    print(f'O número {num} convertido em octal é: {oct(num)[2:]}')
else:
    print(f'O número{num} convertido em hexadecimal é: {hex(num)[2:]}')