#Dicionários
dicionario = {'nome':'Nick', 'idade':16}
print(dicionario)
print(dicionario['nome'])

#Adcionando Chaves
dicionario['gênero'] = 'Não Binário'
dicionario['doce'] = 'chocolate'
print(dicionario)

#Deletando Valores
del dicionario['doce']
print(dicionario)

#Diferença emtre valores, chaves e itens
print(dicionario.values()) #Valores
print(dicionario.keys()) #Chaves
print(dicionario.items()) #Itens

for k, v in dicionario.items():
    print(f'{k}: {v}')

#Adicionando Dicionários a uma lista
cadastrados = []
dicionario1 = {'nome': 'João', 'idade': 18, 'gênero': 'Masculino'}
dicionario2 = {'nome': 'Leonardo', 'idade': 17, 'gênero': 'Masculino'}
dicionario3 = {'nome': 'Luiz', 'idade': 19, 'gênero': 'Masculino'}
cadastrados.append(dicionario)
cadastrados.append(dicionario1)
cadastrados.append(dicionario2)
cadastrados.append(dicionario3)
print(cadastrados[0])
print(cadastrados[1])
print(cadastrados[3]['nome'])

#Fazendo uma cópia do dicionário
dados1 = {'nome':'Nick', 'idade':16}
dados2 = []
dados1['CPF'] = 13999998938
dados2.append(dados1.copy())
print(dados2)