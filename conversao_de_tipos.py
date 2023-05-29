# Conversão de Tipos

idade = "23" # Idade é uma variável do tipo string
print(idade, type(idade))

idade_inteira = int(idade) # Convertendo o tipo da variável idade de string para inteiro e armazenando em idade_inteira
print(idade_inteira, type(idade_inteira))

# int() -> Converte para o tipo inteiro
# str() -> Converte para o tipo string
# float() -> Converte para o tipo float
# bool() -> Converte para o tipo bool

"""
Python recebe todo valor como str, 
para contornar esse problema podemos adicionar
a função de conversão antes do input quando precisarmos fazer operações matemáticas.
"""

# Exemplo
altura = float(input("Informe a sua altura: "))
