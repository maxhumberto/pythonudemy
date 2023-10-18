nota1_primeiro_semestre = float(input("Digite a nota do primeiro semestre: "))
nota2_primeiro_semestre = float(input("Digite a nota do primeiro semestre: "))



nota1_segundo_semestre = float(input("Digite a nota do segundo semestre: "))
nota2_segundo_semestre = float(input("Digite a nota do segundo semestre: "))


media_primeiro_semestre = (nota1_primeiro_semestre + nota2_primeiro_semestre) / 2
media_segundo_semestre = (nota1_segundo_semestre + nota2_segundo_semestre ) / 2

media_total = (media_primeiro_semestre + media_segundo_semestre) / 2


if media_primeiro_semestre >= 7 and media_segundo_semestre >= 7:
    situacao = "Aprovado"
elif (media_primeiro_semestre >= 6 and media_segundo_semestre >= 7) or (media_primeiro_semestre >= 7 and media_segundo_semestre >= 6):
    situacao = "Recuperação"
else:
    situacao = "Reprovado"


print(f"Média Total: {media_total}")
print(f"Situação do aluno: {situacao}")