#Funções == Rotinas
def linha():
    print('-' *  40)

#Programa principal
linha()
print('Cadastro')
linha()
print('Menu')
linha()
print('Sair')
linha()

def mensagem(msg):
    print('-' * 40)
    print(msg)
    print('-' * 40)

mensagem('Sistema de Cadastro')
mensagem('Carregando...')

def soma(a, b):
    s = a + b
    print(s)


#Programa principal
soma(4, 5)
soma(19, 4)
