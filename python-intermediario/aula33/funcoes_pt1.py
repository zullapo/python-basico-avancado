"""
Aula 33 - Funções Pt. 1

Bloco de códigos relacionados a solução de uma tarefa específica.

Por estarem em uma função podem ser re-executados em outras partes
do programa, assim fazendo com que o programa tenha menos linhas
e seja mais coeso.

Estrutura de uma função:

def nome_funcao(parametros):
    ...
"""


def saudacoes():
    print("Olá usuário")


saudacoes()
saudacoes()


def saudacoes(msg, nome):
    print(msg, nome)


# Uso de argumentos para reúso da função:
saudacoes("Olá", "José")
saudacoes("Hi", "Monica")
saudacoes("Hola", "Antonio")


# Argumentos com valor padrão:
def saudacoes(msg="Olá", nome="Usuário"):
    print(msg, nome)


saudacoes()  # Imprime a mensagem com os valores padrões.
saudacoes("Sup", "Trae")
# Valores dos argumentos são preenchidos na ordem (esquerda-direita).
# saudacoes("Otávio")
# Para preencher somente o argumento "nome", use argumentos nomeados:
saudacoes(nome="Otávio")
