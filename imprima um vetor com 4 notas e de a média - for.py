print("imprima um vetor com 4 notas e de a média - for")

notas = []

for i in range(4):
  nota = int(input("digite sua nota: "))
  notas.append(nota)
print(notas)

media = int (notas[0] + notas[1] + notas[2] + notas[3]) 

print (media/4)


