print("3 vetores, pares e ímpares - for")

vetor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for vetor1 in range(1, 21, 1):
  print (vetor1)
print("entre os números acima:")

vetorpar = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
vetorimpar = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

print("estes são pares:")
for vetorpar in range(2, 21, 2):
  print(vetorpar)
  
print("estes são ímpares:")  
for vetorimpar in range(1, 20, 2):
  print(vetorimpar)

