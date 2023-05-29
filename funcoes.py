# Criando uma Função

# Função inicial
def saudacao():
    print("Seja bem-vinda(o)")

saudacao()

# Funcção com paramêtros
def saudacao(nome, curso):
    print(f"Seja bem-vinda(o), {nome}")
    print(f"Olá, é um prazer ter você fazendo parte do curso de {curso}")

saudacao("Luiz", "Python")

# Funcção com paramêtros default
def saudacao(nome, curso="C++"):
    print(f"Seja bem-vinda(o), {nome}")
    print(f"Olá, é um prazer ter você fazendo parte do curso de {curso}")

saudacao("Luiz")

# Função com retorno
def soma(num1, num2):
    return num1 + num2

resultado = soma(5, 7)
print("O resultado da soma é", resultado)