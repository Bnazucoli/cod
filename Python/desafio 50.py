print('SOMANDO NÚMEROS INTEIROS PARES:')
soma = 0
cont = 0
for c in range (0, 6):
    n= int(input(f'Digite o {c} valor: '))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print(f'Você informou {cont} números pares, e a soma desses números resulta em: {soma}.' )
