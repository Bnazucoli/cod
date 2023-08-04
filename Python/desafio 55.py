maior = 0
menor = 0
for pess in range (1, 6):
    peso = float(input(f'Qual o peso da {pess}° pessoa?'))
    if pess == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso é {maior}kg.')
print(f'O menor peso é {menor}kg.')
