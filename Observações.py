#Tipos Primitivos
#----int = 7, -4, 0, 4971
#----float = 4.5, 0.72, 0.7985, 7.0
#----bool = True False
#----str = 'Olá', '7.5'

#Operadores Aritmeticos
#-1- ()__O que está em parenteses
#-2- **__Potenciação
#-3 *, /, //, %
#-4- +, -

#Modulos
#Cada arquivo em Python é chamado de módulo.
#Módulos são um conjunto de códigos como funções, classes, variáveis, etc.
#Vários módulos podem se comunicar através do comando import módulo.
##import math
##import time
##import datetime
##import abc

#Manipulação de texto
#Fatiamento
frase = 'Aprendendo a Programar em python'
print(frase[9])
print(frase[:9])
print(frase[9:])
print(frase[3:17])
#Analize
print(len(frase))
print(frase.count('a'))
print(frase.find('pr'))
print('Programa' in frase)
#Transformações
print(frase.replace('Programar', 'cozinhar'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip()) #Ele tira espaços desnecessários
print(frase.split()) #Divide as palavras

#Condições
if 'a' in frase:
    tot = frase.count('a')
    print(f'Essa frase tem {tot} a`s')

elif 'o' in frase:
    total = frase.upper()
    print(total)

else:
    print('Acabou')

#Cores no Terminal
#estilo
print('\033[0mOi')
print('\033[1mOi')
print('\033[4mOi')
print('\033[7mOi')

#Texto
print('\033[31mOi')
print('\033[32mOi')
print('\033[33mOi')
print('\033[34mOi')
print('\033[35mOi')
print('\033[36mOi')
print('\033[37mOi')

#Fundo
print('\033[41;30mOi')
print('\033[42mOi')
print('\033[43mOi')
print('\033[44mOi')
print('\033[45mOi')
print('\033[46mOi')
print('\033[47mOi')

#Condições aninhadas é if dentro de if e etc

#Estruturas de repetição
#for
#peso = []
#for i in range(0, 5):
        #peso.append(float(input('\033[0minforme o peso: ')))
#print('O menor peso informado foi: {} é o maior peso informado foi {}'.format(min(peso), max(peso)))

#while
#sistema de repetição infinita que é determinado o começo e o fim com False e True
#Pode parar com Break em uma condição

#Tuplas
#Ficam entre parenteses
#Não podem ser mudadas ao decorrer do programa
#duplas podem ser deletadas com del(nome da tupla)
print('\033[0m~' * 50)
lista = ('maça', 'banana', 'maracujá', 'morango', 'limão')
print(lista)
print(lista[2])
print(lista[-2])
print(lista[1:4])
for fruta in lista:
    print(f'Eu vou comer {fruta}')
print('Comi pra caramba')

for cont in range (0, len(lista)):
    print(lista[cont])
print(sorted(lista))

lista2 = (1, 2, 3)
lista3 = (4, 5, 6, 7, 8)
lista4 = lista2 + lista3
print(lista4)
