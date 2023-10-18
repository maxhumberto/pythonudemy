def validar_nome(texto):
    return texto.isalpha()

def validar_idade(texto):
    return texto.isdigit()

nome = input("Digite seu nome: ")
while not validar_nome(nome):
    print("Por favor, digite apenas letras para o nome.")
    nome = input("Digite seu nome: ")

sobrenome = input("Digite seu sobrenome: ")
while not validar_nome(sobrenome):
    print("Por favor, digite apenas letras para o sobrenome.")
    sobrenome = input("Digite seu sobrenome: ")

idade = input("Digite sua idade: ")
while not validar_idade(idade):
    print("Por favor, digite uma idade válida (número inteiro).")
    idade = input("Digite sua idade: ")

cidade = input("Digite sua cidade: ")

print("Nome:",nome , "; Sobrenome: " , sobrenome , "; Idade: " , idade , "; Cidade: " , cidade )