n = input('Qual seu nome completo? ').strip()
nome = n.split()
print('seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
