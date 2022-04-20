"""
Aula 19 - Estrutura de repetição while

Uma estrutura de repetição testa se uma condição é verdadeira,
executa bloco de código e repete a execução enquanto condição
for verdadeira.

Estrutura de um while:

while condicao:
    ...

O bloco while significa enquanto, ou seja, enquanto dada condição
for True, execute código e teste novamente se condição continua
sendo True.
"""

# Quando a condição testada é sempre True, o código será executado
# até que feche o programa, isso é chamado de loop infinito.
# while True:
#    print(1)

x = 0
while x < 10:
    print(x)
    x = x + 1

print()

# O "continue" pula a iteração de um loop para que outra seja executada.
x = 0
while x < 10:
    # Se o "continue" for utilizado sem que o valor testado
    # mude de alguma forma para que a condição seja True, o
    # loop será infinito.
    # if x == 3:
    #   continue

    if x == 3:
        x = x + 1
        continue
    x = x + 1
    print(x)

print()

# O "break" interrompe a execução de um loop totalmente.
while True:
    print("Menu:\n"
          "1) Sair\n"
          "2) Explicação de estruturas condicionais\n"
          "3) Explicação de estruturas de repetição")
    opcao = input("Insira uma das opções do menu acima: ")

    print()

    if opcao == "1":
        break
    elif opcao == "2":
        print("Determinam a execução de um bloco de código por meio de condições.")
    elif opcao == "3":
        print("Testam se uma condição é verdadeira, executam bloco de código e "
              "repetem execução do bloco enquanto condição for verdadeira.")
    else:
        print("Opção inválida")

    print()

# Loops aninhados:
# Tabela 5x5
x = 0
while x < 5:
    y = 0
    while y < 5:
        y = y + 1
        print(f"Ln {x}, Col {y}")
    x = x + 1
