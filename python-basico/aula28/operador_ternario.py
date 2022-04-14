"""
Aula 28 - Operador ternário

É maneira simplificada do if/else presente em linguagens semelhantes ao C,
ex.: valor1 ? condição : valor2. Em Python, ao ínvés dos operadores ? e :,
é utilizado if e else.
"""

# if/else sem operador ternário:
usuario_logado = False

if usuario_logado:
    print("Usuário logado.")
else:
    print("Faça o login com seu usuário.")

# if/else com operador ternário:
msg = "Usuário logado." if usuario_logado else "Faça o login com seu usuário."

print(msg)
