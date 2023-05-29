# > Variáveis

# 1. Variáveis
idade = 23 # Criando uma variável do tipo inteiro
print(idade)

nome = "Luiz Fernando" # Criando uma variável do tipo string
print(nome)

"""
    Tipos de variáveis

    2. float: números reais
    3. string: cadeia de caracteres
    4. bool: valores lógicos
"""

idade = 23
altura = 1.80
nome = "Luiz Fernando"
estudando = True

# Exibindo o tipo da variável criada
print(type(idade)) # Imprimindo o tipo da variável idade -> int
print(type(altura))# Imprimindo o tipo da variável altura -> float
print(type(nome))# Imprimindo o tipo da variável nome -> str
print(type(estudando))# Imprimindo o tipo da variável estudando -> bool

# Obtendo dados do usuário e salvando em variáveis
linguagem = input("Qual é a linguagem de programação que você está estudando? ")
print("A linguagem que você está estudando é", linguagem)