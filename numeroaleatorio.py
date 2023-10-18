import random

numero_aleatorio = random.randint(0, 9)

tentativas_maximas = 5
tentativas = 0

while tentativas < tentativas_maximas:
    tentativa = int(input("Tente adivinhar o número (entre 0 e 9): "))
    tentativas += 1

    if tentativa == numero_aleatorio:
        print("Parabéns! Você acertou o número.")
        break
    else:
        print("Tentativa incorreta. Tente novamente.")


if tentativas == tentativas_maximas:
    print(f"Você esgotou todas as tentativas. O número correto era {numero_aleatorio}.")