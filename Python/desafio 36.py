casa = float(input('Qual valor da casa? '))
salario = float(input('Qual seu salário? '))
anos = float(input('Quantos anos de parcelas?' ))
prestacao = casa / (anos * 12)
print(f'O valor da prestação do imóvel é: {prestacao:.2f}')
if prestacao <= salario * 30 /100:
    print('Empréstimo residêncial: Aprovado!')
else:
    print('Empréstimo residêncial: Negado!')