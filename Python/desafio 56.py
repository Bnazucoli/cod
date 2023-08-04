somaidade = 0
mediaidade = 0
maioridadeh = 0
nomevelho = ''
totm20 = 0
for p in range (1, 5):
    print(f'---- {p}° pessoa ----')
    nome= str(input('NOME: ')).strip()
    idade= int(input('IDADE: '))
    sexo= str(input('SEXO: [M/F]: ')).strip()
    somaidade += idade
    mediaidade = somaidade / 4
    if p == 1 and sexo in 'Mm':
        maioridadeh = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadeh:
        maioridadeh = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totm20 += 1

print(f'A média de idade do grupo é de {mediaidade} anos.')
print(f'O homem mais velho tem {maioridadeh} anos, e se chama {nomevelho}.')
print(f'Ao todo são {totm20} mulheres com menos de 20 anos.')

