"""
Aula 18 - Manipulando strings (slice e index)

Strings são sequências, por isso podem ser indexadas, isto é
cada caractere corresponde uma posição. O primeiro caractere
corresponde a posição 0 e o último caractere corresponde ao
tamanho da string - pode ser checado através da função len.

Strings podem ser fatiadas (sliced) para que se obtenha um
pedaço entre determinadas posições (começo e final).
"""

texto = "Python <3"

print(texto[0])
print(texto[8])

# Índices também podem ser negativos, assim a string será acessada da direita para esquerda.

# positivos: 012345678
# Python <3
# negativos (-): 987654321

print(texto[-9])
print(texto[-1])

# Fatiando strings [início:final:passo (opcional)]

# Obs.: o caractere da posição "início" é incluso no intervalo,
# porém o caractere da posição "final" não é, assim é só
# considerado o caractere da posição anterior ao "final".
print("Posição inicial: 2")
print("Posição final: 6")
print(f"texto[0:4] = {texto[2:6]}")

# Ambas formas funcionam, pois o valor padrão para o início é 0.
print(texto[0:2])
print(texto[:2])

# Da mesma forma que o valor padrão para o início é 0, o valor padrão para o final é
# o tamanho da string.
print(texto[7:9])
print(texto[7:])
print("Tamanho da string:", len(texto))

# Fatiando string com índices negativos
print(texto[-2:])
print(texto[:-3])  # Cortando a parte <3

# Usando "passo"
print(texto[::4])
# Inverte a string pulando uma casa da direita para esquerda
print(texto[::-1])
