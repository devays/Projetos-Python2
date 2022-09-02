ficha = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome,[nota1, nota2],media])
    continuar = str(input('Deseja continuar? [S/N] '))
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break

print('-='*26)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i,a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<8}{a[2]:>8.1f}')
while True:
    opc = int(input('Deseja ver a nota de qual aluno? (999 interrompe) '))
    if opc == 999:
        print('Obrigado por utilizar nosso programa.')
        break
    if opc <= len(ficha) - 1:
        print(f'O aluno {ficha[opc][0]} tirou as notas {ficha[opc][1]} ')