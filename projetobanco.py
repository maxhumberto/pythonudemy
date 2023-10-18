menu = """
[d]Depositar
[s]sacar
[e]Extrato
[q]sair

=>"""
saldo= 1500.00
limite = 500
extrato = ""
numeros_saques = 0
Limite_saques = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor a ser depositado: R$ "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ { valor:.2f}"\n

        else:
            print("Operação falhou! O valor informado é invalido.")

    elif opcao == "s":
        valor = float(input("Digite o valor a ser sacado: R$ "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite

        excedeu_saques = numeros_saques >= Limite_saques 

        if excedeu_saldo:
            print("saldo insulficiente")
        elif excedeu_limite:
            print("excede o limite")
        elif excedeu_saques:
            print("número de saque excedido.") 

        elif valor > 0:
            saldo += valor
            extrato += f"saque: R${valor:.2f}\n"
            numeros_saques += 1              

        else:
            print("Valor informado é invalido.")
        
    elif opcao == "e":
        print("\n==========EXTRATO==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nsaldo: R$ {saldo:.2f}")
        print('================================')
    elif opcao == "q":
        break
    else:
        print("Operação invalido, por favor selicionar novamente a operação desejada.")


