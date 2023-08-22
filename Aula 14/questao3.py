quantidade_de_alunos = int(input("Quantos alunos estão na turma? "))

alunos = {}

for i in range(quantidade_de_alunos):
  nome = input("Insira o nome do aluno {}: ".format(i + 1))
  nota = float(input("Insira a nota do aluno {}: ".format(i + 1)))
  alunos[nome] = nota

media = sum(alunos.values()) / len(alunos)

aluno_com_maior_nota = max(alunos, key=lambda aluno: alunos[aluno])
print("O aluno com a maior nota é:", aluno_com_maior_nota)

alunos_com_nota_abaixo_da_media = [aluno for aluno, nota in alunos.items() if nota < media]

if alunos_com_nota_abaixo_da_media:
  print("Os alunos com nota abaixo da média são:", alunos_com_nota_abaixo_da_media)
else:
  print("Nenhum aluno tirou nota abaixo da média.")
