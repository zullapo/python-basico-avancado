"""
Aula 17 - Formatando valores com modificadores

Aplicável na função format e f-strings.

:s - string

:d - int

:f - float

:.(número)(s, d ou f) - limita o número de casas decimais para float
e limita o tamanho para int e string, conforme o número inserido antes do tipo

:(caractere)(>, < ou ^)(quantidade)(s, d ou f) - repete caracteres em uma dada
posição, o número de caracteres inseridos será a quantidade menos o tamanho da
string

>: esquerda
<: direita
^: centro (metade na esquerda e direita)
"""

nome = "Red Wacky League Antlez Broke the Stereo Neon Tide Bring Back Honesty Coalition Feedback Hand of Aces Keep Going Captain Let's Pretend Lost State of Dance Paper Taxis Lunar Road Up Down Strange All and I Neon Sheep Eve Hornby Faye Bradley AJ Wilde Michael Rice Dion Watts Matthew Appleyard John Ashurst Lauren Swales Zoe Angus Jaspreet Singh Emma Matthews Nicola Brown Leanne Pickering Victoria Davies Rachel Burnside Gil Parker Freya Watson Alisha Watts James Pearson Jacob Sotheran Darley Beth Lowery Jasmine Hewitt Chloe Gibson Molly Farquhar Lewis Murphy Abbie Coulson Nick Davies Harvey Parker Kyran Williamson Michael Anderson Bethany Murray Sophie Hamilton Amy Wilkins Emma Simpson Liam Wales Jacob Bartram Alex Hooks Rebecca Miller Caitlin Miller Sean McCloskey Dominic Parker Abbey Sharpe Elena Larkin Rebecca Simpson Nick Dixon Abbie Farrelly Liam Grieves Casey Smith Liam Downing Ben Wignall Elizabeth Hann Danielle Walker Lauren Glen James Johnson Ben Ervine Kate Burton James Hudson Daniel Mayes Matthew Kitching Josh Bennett Evolution Dreams"
print(f"33/99 = {33/99:.2f}")
print(f"Nome: {nome:.101}")
print("{:=^30}".format("TABELA DE DADOS"))
print("{:0>10}".format(1000))

# Outras funções de formatação de string

print("10".ljust(10, "0"))
print("01".rjust(10, "0"))
print("1".zfill(5))

print("josé".upper())
print("MARIA".lower())
print("jOão".title())
