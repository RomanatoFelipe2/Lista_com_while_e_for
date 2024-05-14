print("lendo caracteres e selecionando consoantes")

consoantes = []
total_consoantes = 0

for i in range(10):
    caractere = input("Digite um caractere: ").lower()
    if caractere.isalpha() and caractere not in 'aeiou':
        consoantes.append(caractere)
        total_consoantes += 1

print("Consoantes lidas:")
for consoante in consoantes:
    print(consoante)

print("Total de consoantes lidas:", total_consoantes)