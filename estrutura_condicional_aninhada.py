


conta_normal = True
conta_universitaria = False
saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("saque relizado com sucesso") # "Conta normal"
    elif saque <= ( saldo + cheque_especial):
        print("saque relizado com uso do cheque especial!")
    else:
        print("saldo insuficiente!")    
elif conta_universitaria:
    if saldo >= saque:
        print ("saque realizado com sucesso") 
    else:
        print("saldo insuficiente!")
else:
    print("sistema não reconheceu seu tipo de conta, entre em contato com seu gerente")
