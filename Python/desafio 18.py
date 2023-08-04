import math
angulo= float(input('Digite o valor do ângulo: '))
sen= math.sin(math.radians(angulo))
cos= math.cos(math.radians(angulo))
tan= math.tan(math.radians(angulo))
print(f'No angulo {angulo}º o valor do seno é de {sen:.2f} e do cosseno é de {cos:.2f}.')
print(f'O valor da tangente é de {tan:.2f}')