# Criando dicionarios
dicionario = {}
dicionario = dict()
dicionario = {'nome': "Luiz Fernando", 'idade': 23, 'altura': 1.80}

print(dicionario)
print(dicionario['idade'])

# Adicionando elementos em um dicionario
dicionario['programador'] = True
print(dicionario)

dicionario['altura'] = 2 # Sobrescrever valor com uma chave já existente
print(dicionario)

# Iterando sobre um dicionario
for chave in dicionario:
    print(chave, dicionario[chave])


# Testando a existencia de uma chave
print("peso" in dicionario)
print("altura" in dicionario)