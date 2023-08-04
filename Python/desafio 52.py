print(' '*10,'É OU NÃO É PRIMO?',' '*10)
n = int(input('Digite o n°: '))
tot = 0
for c in range (1, n + 1):
    if n % c == 0:
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print('\n\033[mresultado:')
if tot == 2:
    print('O número é divisível somente por 1 e por ele mesmo, por isso ele É PRIMO.')
else:
    print(f'O número {n} é divisível por todos os números que estão azul, por isso ele NÂO É PRIMO.')
