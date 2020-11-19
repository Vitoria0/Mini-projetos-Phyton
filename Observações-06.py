# Modulos e Pacotes
#------Programa principal
from uteis import numeros

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobre de {num} é {numeros.dobro(num)}')
