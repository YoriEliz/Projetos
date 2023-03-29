while True:
    print("Digite primeiro um número e depois um operador (+-/*): ")
    try:
        numero_1 = float(input("Digite o primeiro número: "))
        numero_2 = float(input("Digite o segundo número: "))
        operador = input("Digite o operador (+-/*): ")
    except ValueError:
        print("Digite apenas números válidos!")
        continue

    if operador == "+":
        resultado = numero_1 + numero_2
    elif operador == "-":
        resultado = numero_1 - numero_2
    elif operador == "*":
        resultado = numero_1 * numero_2
    elif operador == "/":
        if numero_2 == 0:
            print("Não é possível dividir por zero!")
            continue
        resultado = numero_1 / numero_2
    else:
        print("Operador inválido!")
        continue

    print(f"O resultado de {numero_1} {operador} {numero_2} é: {resultado:.2f}")

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    if sair:
        break