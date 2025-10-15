# O sistema deve ler a média e a frequência do aluno. Ele será aprovado se tiver média ≥ 7 e frequência ≥ 75%. Caso contrário, estará reprovado. Mostre a situação final.
media = float(input("Digite a média do aluno: "))
freq = int(input("Digite a frequência, em porcentagem, do aluno: "))
if media >= 7 and freq <= 75:
    print('aprovado')
else: 
    print('reprovado')
