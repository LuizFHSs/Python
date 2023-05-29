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

# Métodos de listas
lista = [1, 3, 12, 8, 2]
print("Antes do append", lista)

# append
lista.append(3) # Adiciona um novo elemneto no final da lista
print("Depois do append", lista)

# insert
lista.insert(2, 10) # Insere um novo elemento na lista -> o primeiro paramêtro é o indice, o segundo é o novo valor
print("Depois do insert", lista)

# extend
lista2 = [1, 2, 3]
lista.extend(lista2) # Junta duas listas

print("Depois do extend:", lista)

# pop
lista.pop() # Elimina o último elemento da lista
print("Lista após o pop:", lista)

lista.pop(0) # Elimina o elemento que está no indice passado pelo paramêtro
print("Lista após o pop:", lista)

# remove
lista.remove(3) # Remove o primeiro elemento encontrado com o valor do paramêtro
print("Depois do remove:", lista)

# count | Contar qunatas vezes um elemento aparece na lista
print("Quantidade de 2 na lista:", lista.count(2)) # O valor passado é o valor que estamos procurando

# index | Retorna o index de um determinado elemento dentro da lista
print("Índice do elemento 12:", lista.index(12)) # O valor passado é o valor que estamos procurando

# sort
lista.sort() # Ordenar lista em ordem crescente | descrescente 'lista.sort(reverse=true)
print(lista)

# Funcções para listas
# sum
print(sum(lista)) # Soma todos elementos da lista

# max | Retorna o MAIOR valor da lista
print("Maior elemento da lista:", max(lista))

# min | Retorna o MENOR valor da lista
print("Menor elemento da lista:", min(lista))