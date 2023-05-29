# Estrutura de repetição FOR

# Passando um paramêtro para a funcção range -> o range começa em 0 e vai até o paramêtro passado
for variavel in range(5): # Para a variável dentro de uma faixa faça...
   print(variavel)

# Passando dois paramêtros para a função range -> o range começa no primeiro paramêtro e vai até o segundo paramêtro menos um.
for variavel in range(1, 11):
    print(variavel)

# Passando três paramêtros para a função range -> o range começa no primeiro paramêtro e vai até o segundo paramêtro menos um e incrementa a quantidade passada no terceiro paramêtro
for variavel in range(0, 11, 2):
    print(variavel)

for nota in range(1, 4):
    nota = float(input(f"Informe sua nota {nota}:"))

# Variavel Acumuladora
soma = 0

for i in range(1, 4):
    nota = float(input(f"Informe a sua nota {i}: "))
    soma = soma + nota

print(soma)