from random import randint
escolhido = randint(0, 5)
print('-=-'*20)
print('vou pensar em um nº entre 0 e 5, tente adivinhar... ')
print('-=-'*20)
jogador = int(input('Em que número pensei? '))
if jogador == escolhido:
    print('PARABÉNS!! Você conseguiu me vencer.')
else:
    print(f'GANHEI!! Eu pensei no nº {escolhido} e não no nº {jogador}.')

