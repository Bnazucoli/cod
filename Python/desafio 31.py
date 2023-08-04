distancia = float(input('Qual a distancia da sua viagem? '))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.40
print(f'O preço de sua passagem será {preço}.')