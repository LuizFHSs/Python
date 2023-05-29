# > Listas

# Criando uma lista
lista = []
lista = list()
lsita = [23, "Luiz", 3.1415, True]
lista_de_listas = [10, [1,2,3]]

# Indexação e  Slices (fatiamento)
lista = [23, "Luiz", 3.1415, False]

# Indexando com números positivos
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

# Indexando com números negativos
print(lista[-1]) # Imprime o último valor da lista
print(lista[-2]) # Imprime o penúltimo valor da lista
print(lista[-3]) # Imprime o antepenúltimo valor da lista
print(lista[-4]) # Imprime o (no caso) o primero valor da lista

# Slices | Pedaços da lista
lista = [10,50,30,40,25,60,5]

print(lista[0:3]) # O Primeiro valor é onde começa o 'pedaço', o segundo valor é até onde vai menos o valor passado.
print(lista[0:]) # Sem o segundo valor, vai até o final da lista
print(lista[2:6:2]) # Com o terceiro valor, irá iterar('pular') de acordo com o valor passado

# Iterações com FOR
# 1.
for elemento in lista:
    print(elemento)

# 2.
for i in range(len(lista)):
    print(lista[i]) # Exibindo cada ELemento da lista | print(i) -> Exibiria soomente os indices da lista


# Verificar tamanho da lista
print("Comprimento da lista:", len(lista)) # A função len() pode ser usada para saber o tamnho da lista
