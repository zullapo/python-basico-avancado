"""
Aula 24 - For com else

Assim como o while, o bloco for pode ser utilizado com o else.
Quando a condição do "for" for falsa, o else será executado.
"""

menu = ["Whooper", "Cheeseburger", "Cheddar"]

print("Menu: ")

for item in menu:
    print("-", item)

opcao_menu = input("Insira uma opção do menu (nome): ")

for item in menu:
    if opcao_menu == item:
        print(f"Você escolheu o item \"{item}\"")
        break
else:
    print(f"Item \"{opcao_menu}\" não está no menu.")
