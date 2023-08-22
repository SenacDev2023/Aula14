quantidade_de_numeros = int(input("Quantos números deseja inserir? "))

numeros = []

for i in range(quantidade_de_numeros):
  numero = float(input("Insira o número {}: ".format(i + 1)))
  numeros.append(numero)

media = sum(numeros) / len(numeros)

print("A média dos números é:", media)
