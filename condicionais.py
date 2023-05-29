# > Estruturas Condicionais

idade = 15

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")


"""
    Imagine que você queira imprmir "Aprovada(o)", caso o estudante tenha uma média
    superior ou igual a 7, e "Reprovado", caso a média seja inferior a 7.
"""

media = float(input("Informe a média do estudante: "))

if media >= 7:
    print("Você foi Aprovada(o)!")
elif media >= 5:# Caso onde houvesse uma condição de recuperação, onde a média maior ou igual a 5 é recupração
    print("Recuperação")
else:
    print("Você foi Reprovada(o)!")
