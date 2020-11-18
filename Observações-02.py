#Listas
lanche = ['Bolo', 'Pepsi', 'Pizza', 'Pudim']
print(lanche)

#Muda um ítem na lista
lanche[3] = 'Sorvete'
print(lanche)

#Adiciona algo a lista
lanche.append('Bolacha')
print(lanche)

#Adcionar em uma posição específica
lanche.insert(0, 'Iogurte')
print(lanche)

#Remove
lanche.remove('Bolo')
print(lanche)

#Colocar em ordem
valores = [8, 2, 5, 4, 9, 3, 0]
print(valores)
valores.sort()
print(valores)
valores.sort(reverse=True)
print(valores)

#Quantidade de valores
print(len(valores))

#Listas dentro de listas
pessoa = []
pessoa.append('João')
pessoa.append(18)
pessoa1 = ['Vitória', 16]
pessoa2 = ['Leonardo', 17]
pessoa3 = ['Luiz', 19]

grupo = []
grupo.append(pessoa[:]) # [:] Faz uma cópia para que não mude a lista original
grupo.append(pessoa1[:])
grupo.append(pessoa2[:])
grupo.append(pessoa3[:])
print(grupo)
print(f'No grupo temos o {grupo[0][0]} e ele tem {grupo[0][1]} anos')
print(pessoa1)
pessoa1 [1] = 19 #Trocando a informação
print(pessoa1)

#Criar e excluir
galera = list()
dado = list ()
for c in range (0, 6):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
galera.append(dado[:])
dado.clear()
print(dado)
print(galera)