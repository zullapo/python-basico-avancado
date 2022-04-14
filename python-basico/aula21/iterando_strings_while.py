"""
Aula 21 - Iterando strings com while

Iterar é percorrer desde o início de uma sequência até o final.
Como uma string é uma sequência, basta pegar seu tamanho e
implementar um contador para percorrer sobre os índices dela.
"""

frase = "no meio da dificuldade encontra-se a oportunidade"
contador = 0
nova_string = ''

opcao_letra = input("Qual letra deseja mudar para maiúscula? ")

while contador < len(frase):
    letra_frase = frase[contador]
    # print(letra_frase, contador)

    if letra_frase == opcao_letra:
        nova_string += letra_frase.upper()
    else:
        nova_string += letra_frase 

    # print(nova_string)

    contador += 1

print(nova_string)
