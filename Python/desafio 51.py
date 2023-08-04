print('-'*10, 'TERMOS DA PA','-'*10)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Qual a razão? '))
decimo = primeiro + (10 - 1) * razao
for c in range (primeiro, decimo + razao, razao):
    print(f'{c}', end=' - ')
print('FIM')