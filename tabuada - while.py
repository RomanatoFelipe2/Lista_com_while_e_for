print ("tabuada com while")
valor = int(input('Entre com um número para saber a tabuada: '))  
valor2 = 0  
print('*' * 18)  
print('Tabuada de {}'.format(valor))  
print('*' * 18)  
while(valor2 <= 10):  
  print('{0} X {1} = {2}'.format(valor2, valor, (valor2 * valor)))  
  valor2 = valor2 + 1
