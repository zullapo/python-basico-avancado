"""
Aula 22 - Estrutura de repetição for

Em Python, só existe o for in ao invés do for (contador;condição;incremento)
visto em linguagems como C. O for in acessa cada elemento de uma sequência
e armazena o valor de cada iteração em uma variável auxiliar.

Estrutura de um for-in:

for variavel_auxiliar in sequencia:
    ...
"""

# Iterando sobre uma string:
frase = "o sucesso é ir de fracasso em fracasso sem perder o entusiasmo"

for letra in frase:
    print(letra)

# Função range(começo=0, final, passo=1)
# Gera um intervalo finito de números, geralmente utilizado com o for-in
# para acessar diretamente os índices de uma sequência.
for i in range(10):
    print(i)

for i in range(len(frase)):
    print(frase[i])

# Função enumerate(sequencia)
# Retorna índice e valor de cada interação em uma sequência.
for indice, valor in enumerate(frase):
    print(indice, valor)

# break - interrompe totalmente a execução do loop.
# continue - pula uma iteração, para que outra seja executada.
for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(10):
    if i == 4:
        continue
    print(i)
