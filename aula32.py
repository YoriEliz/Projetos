"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_inteiro = float(input("digite um numero inteiro "))
if numero_inteiro % 2 == 0:
    print(f"{int(numero_inteiro)} È um numero par")
elif numero_inteiro % 2 == 1: 
    print(f"{int(numero_inteiro)} È um numero impar")
else:
    print("Não é um numero inteiro")
