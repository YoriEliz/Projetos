"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
saudacao = int(input("Digite a hora: "))

if saudacao in range(0, 12):
    print("Bom dia")
elif saudacao in range(12, 18):
    print("Boa tarde")
else:
    print("Boa noite")