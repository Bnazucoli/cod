dias=int(input('Quantos dias alugado? '))
km=float(input('Quantos km rodados? '))
pago= (dias * 60) + (km * 0.15)
print(f'valor total: R${pago}')
