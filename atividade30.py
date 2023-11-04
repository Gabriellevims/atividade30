# Exercício Python 30: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.
med=0
soma=0
homenvelho = ""
idadehomevelho = 0
mulhercom20 = 0
for i in range(4):
    nome = str(input("Digite o seu nome:"))
    id= int(input("Digite sua idade:"))
    sex= int(input("Digite o número 1 se você é HOMEN: Digite 2 se você é MULHER:"))
    while sex != 1 and sex != 2:
        print("Digite um valor válido. 1 ou 2.")
        sex= int(input("Digite o número 1 se você é HOMEN: Digite 2 se você é MULHER:"))
    soma += id
    if sex == 1 and id >= idadehomevelho:
        homenvelho = nome
        idadehomevelho =id
    elif sex == 2 and id<20:
        mulhercom20 += 1 

        

med=soma/4
print("A média de idade do grupo é", med)
print(f"""Nome do homen mais velho:{homenvelho}.
e sua idade é: {idadehomevelho}anos.""")
print(f"A quantidade de mulher com -20 anos é {mulhercom20}")

