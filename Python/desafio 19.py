from random import choice
a1 = input('Aluno nº1: ')
a2 = input('Aluno nº2: ')
a3 = input('Aluno nº3: ')
a4 = input('Aluno nº4: ')
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print(f'O aluno escolhido é: {escolhido}')
