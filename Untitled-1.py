operador = input("Digite um operador (+, -, *, /): ")

soma = False
divisao = False
multiplicacao = False
subtracao = False

if operador == "+":
    soma = True
elif operador == "-":
    subtracao = True
elif operador == "*":
    multiplicacao = True
elif operador == "/":
    divisao = True
else:
    print("Operador inválido.")

print(f"Operador digitado: {operador}")
print(f"Soma: {soma}")
print(f"Divisão: {divisao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Subtração: {subtracao}")
print(operador, soma, multiplicacao, subtracao, divisao)