lista_de_numeros = input("Insira uma lista de números inteiros separados por espaço: ").split()

numeros = [int(numero) for numero in lista_de_numeros]

numeros_pares = 0
numeros_impares = 0

for numero in numeros:
  
  if numero % 2 == 0:
    numeros_pares += 1
  else:
    numeros_impares += 1

print("O número de números pares é:", numeros_pares)
print("O número de números ímpares é:", numeros_impares)

