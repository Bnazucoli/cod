from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range (1, 8):
    nasc = int(input(f'Em que ano a {pess}° pessoa nasceu?'))
    idade = atual - nasc
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo tem {totmaior} pessoas MAIOR de idade. ')
print(f'E {totmenor} pessoas MENOR de idade.')
