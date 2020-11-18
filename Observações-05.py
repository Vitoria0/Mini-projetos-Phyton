# Interactive Help

#Ele explica como funciona e os valores de determinada função
help(print)
print('\n')

#Outra maneira seria
print(input.__doc__)
print('\n')

###
#Docstrings

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: Inicio da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: Sem retorno
    Função criada por nick
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p

#-----Programa principal
contador(2, 20, 2)
print('\n')
help(contador)
print('\n')

###
#Parâmetros Opcionais

def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela
    :param a: O primeiro valor
    :param b: O segundo valor
    :param c: O terceiro valor
    :return: Sem retorno
    """
    s = a + b + c
    print(f'A soma vale {s}')

#------Programa Principal
somar(3, 2, 5)
somar(7, 7)
somar(9)
somar()
print('\n')

###
#Escopo de Variáveis

def teste():
    x = 8 #--- 'X' Tem um escopo local, pois vale apenas na função
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

#------Programa Principal
n = 2 #--- 'N' Tem um escopo global pois foi criado fora da função e pode ser citada dentro dela
print(f'No programa principal n vale {n}')
teste()
#  print(f'No programa principal, x vale {x}') ----Dá erro
print('\n')

###
#Escopo Local
def teste(b):
    global a #--- Não crie uma nova variável 'a'
    a = 8 #--- Cria uma variavel a local
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

#------Programa Principal
#Escopo Global
a = 5
print(f'A fora vale {a}')
teste(a)
print(f'Agora "A" fora vale {a}')
print('\n')

###
#Retornando Valores
def soma(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela
    :param a: O primeiro valor
    :param b: O segundo valor
    :param c: O terceiro valor
    :return: Sem retorno
    """
    s = a + b + c
    return s

r1 = soma(3, 2, 5)
r2 = soma(18, 61)
r3 = soma(99, -81)
print(f'As somas deram {r1}, {r2} e {r3}')