from random import shuffle
a1 = input('Aluno: ')
a2 = input('Aluno: ')
a3 = input('Aluno: ')
a4 = input('Aluno: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print(f'A ordem de apresentação é:{lista}')