numero = int(input("Insira um número inteiro: "))

for i in range(2, numero):
  if numero % i == 0:
    print(numero, "não é primo.")
    exit()

print(numero, "é primo.")
