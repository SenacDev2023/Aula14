produtos = {}

menu = """
Menu de opções:
1. Cadastrar novo produto
2. Verificar estoque de um produto
3. Sair
"""

while True:
  print(menu)

  opcao = int(input("Digite a opção desejada: "))

  if opcao == 1:
    print("Cadastro de novo produto")
    
    nome = input("Insira o nome do produto: ")

    preco = float(input("Insira o preço do produto: "))

    quantidade_em_estoque = int(input("Insira a quantidade em estoque do produto: "))

    produtos[nome] = {"preco": preco, "quantidade_em_estoque": quantidade_em_estoque}

  elif opcao == 2:
    print("Verificação de estoque")

    nome = input("Insira o nome do produto: ")

    if nome in produtos:
      print("Nome:", nome)
      print("Preço:", produtos[nome]["preco"])
      print("Quantidade em estoque:", produtos[nome]["quantidade_em_estoque"])
    else:
      print("O produto não existe no sistema.")

  elif opcao == 3:
    print("Saindo do sistema...")
    exit()

  else:
    print("Opção inválida.")
