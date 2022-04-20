palavra_secreta = "perfume"
letras_digitadas = []
chances = 8

while True:
    if chances <= 0:
        print("Acabou suas 8 chances.")
        break

    letra = input("Digite uma letra: ")

    if len(letra) > 1 or letra == "":
        print("Digite apenas uma letra.")
        continue

    letras_digitadas.append(letra)

    if letra in palavra_secreta:
        print(f"A letra \"{letra}\" existe na palavra secreta.")
    else:
        print(f"A letra \"{letra}\" não está na palavra secreta.")
        letras_digitadas.pop()

    # Armazena numa string as letras acertadas e oculta o restante com *.
    secreto_temporario = ""
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += "*"

    if secreto_temporario == palavra_secreta:
        print(f"Correto! A palavra secreta é {secreto_temporario}.")
        break
    else:
        print(f"Sua palavra secreta: {secreto_temporario}")

    if letra not in palavra_secreta:
        chances -= 1

    print(f"Você ainda tem {chances} chances.")
    print()
