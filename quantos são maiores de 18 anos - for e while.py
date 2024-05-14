print ("quantos são maiores de 18?")

maiores_dezoito = 0

for i in range(5):
    idade = int(input("Digite a idade da pessoa {}: ".format(i + 1)))

    if idade > 18:
        maiores_dezoito += 1

print("Quantidade de pessoas maiores de 18 anos:", maiores_dezoito)
