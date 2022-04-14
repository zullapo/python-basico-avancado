"""
Aula 20 - While com else e acumuladores

O bloco else é executado quando a condição do bloco while é False.

Em um while podem haver contadores e acumuladores. Um contador
controla a execução de um loop e o acumulador soma seu valor
atual com algum outro valor a cada iteração.
"""

contador = 1
acumulador = 2

while contador < 10:
    print(f"Contador: {contador}, Acumulador: {acumulador}")
    
    # Se loop for interrompido pelo break, o bloco else não será executado.
    # if contador == 8:
    #     break

    acumulador += contador  # acumulador = acumulador + contador
    contador += 1
else:
    print("Terminei a execução do loop.")
