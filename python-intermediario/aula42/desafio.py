"""
Aula 42 - Desafio - Dicionários

Criar um programa de quiz, sendo que as questões e respostas devem estar num dicionário
aninhado e um loop deve ser criado para iterar sobre as questões, verificando
se a entrada do usuário corresponde a resposta de múltipla escolha esperada.
"""

# Créditos - Band Esportes - https://www.band.uol.com.br/esportes/teste-seus-conhecimentos-nba-16455475

print("Quiz NBA, temporada 21/22")

print()

questoes = {
    "Questão 1": {
        "questao": "Lakers e Celtics são os maiores campeões da NBA com quantos títulos?",
        "respostas": {
            "A": "20",
            "B": "14",
            "C": "17",
            "D": "22",
        },
        "resposta_certa": "C",
        "resposta_comentada": "Rivais e duas das maiores franquias da NBA, Celtics e Lakers possuem 17 títulos cada. "
        "O último da equipe de Boston foi em 2008 e a de Los Angeles em 2020.",
    },
    "Questão 2": {
        "questao": "Quantas equipes disputam a temporada regular da NBA?",
        "respostas": {
            "A": "28",
            "B": "30",
            "C": "26",
            "D": "24",
        },
        "resposta_certa": "B",
        "resposta_comentada": "A NBA atualmente é formada por 30 equipes. "
        "Elas são divididos em duas conferências, Conferência Leste e Conferência Oeste.",
    },
    "Questão 3": {
        "questao": "Qual é o jogador com mais títulos na NBA?",
        "respostas": {
            "A": "Michael Jordan",
            "B": "LeBron James",
            "C": "Bill Russell",
            "D": "Kobe Bryant",
        },
        "resposta_certa": "C",
        "resposta_comentada": "Lenda do Boston Celtics, o ex-pivô Bill Russell possui 11 títulos da NBA "
        "e é o maior vencedor da liga.",
    },
    "Questão 4": {
        "questao": "Quantos títulos o LeBron conquistou?",
        "respostas": {
            "A": "4",
            "B": "2",
            "C": "3",
            "D": "6",
        },
        "resposta_certa": "A",
        "resposta_comentada": "King James já disputou as finais da NBA por dez vezes e conquistou quatro títulos, "
        "sendo dois com o Miami Heat, um com o Cleveland Cavaliers e o último com os Lakers.",
    },
    "Questão 5": {
        "questao": "Em que ano Michael Jordan se aposentou pela primeira vez?",
        "respostas": {
            "A": "1998",
            "B": "2003",
            "C": "1996",
            "D": "1993",
        },
        "resposta_certa": "D",
        "resposta_comentada": "Michael Jordan se aposentou três vezes da NBA, sendo a última e definitiva em 2003. "
        "Mas a primeira foi em 1993, após conquistar o tricampeonato com os Bulls."
    },
    "Questão 6": {
        "questao": "Quem é o maior cestinha de 3 pontos da história da NBA?",
        "respostas": {
            "A": "Stephen Curry",
            "B": "Ray Allen",
            "C": "James Harden",
            "D": "Damian Lilliard",
        },
        "resposta_certa": "B",
        "resposta_comentada": "Stephen Curry tem 2,832 pontos de 3 e pode até assumir o posto de maior pontuador "
        "em cesta de três pontos na nova temporada, mas o líder do ranking é Ray Allen, "
        "com 2,973 pontos de cesta de 3.",
    },
    "Questão 7": {
        "questao": "Qual jogador marcou mais pontos em um único jogo da temporada regular?",
        "respostas": {
            "A": "Michael Jordan",
            "B": "Klay Thompson",
            "C": "Lebron James",
            "D": "Wilt Chamberlain",
        },
        "resposta_certa": "D",
        "resposta_comentada": "Em 1962, jogando pelo Philadelphia Warriors, "
        "Wilt Chamberlain marcou 100 pontos contra o New York Knicks, na vitória por 169 a 147.",
    },
    "Questão 8": {
        "questao": "Por qual equipe Kobe Bryant foi draftado em 1996?",
        "respostas": {
            "A": "Los Angeles Lakers",
            "B": "Boston Celtics",
            "C": "Charlotte Hornets",
            "D": "Los Angeles Clippers",
        },
        "resposta_certa": "C",
        "resposta_comentada": "No draft de 96, Kobe estava decidido, só jogaria pelos Lakers. "
        "Mas quem draftou Bryant foi o Charlotte Hornets, na 13ª escolha, que o trocou com os Lakers "
        "pouco tempo depois por Vlade Divac.",
    },
}

respostas_certas = 0

for questao_chave, questao_valor in questoes.items():
    print(f"{questao_chave}: {questao_valor['questao']}")
    for resposta_chave, resposta_valor in questao_valor['respostas'].items():
        print(f"{resposta_chave}) {resposta_valor}")

    opcoes_validas = ("A", "B", "C", "D")
    resposta_usuario = input("Digite sua resposta: ")

    while resposta_usuario not in opcoes_validas:
        print()
        print(f"Escolha uma das alternativas: {', '.join(opcoes_validas)}.")
        resposta_usuario = input("Digite sua resposta: ")

    resposta_correta = questao_valor["respostas"][questao_valor["resposta_certa"]]

    if resposta_usuario == questao_valor["resposta_certa"]:
        print(f"Certa resposta: {resposta_correta}.")
        respostas_certas += 1
    else:
        print(f"Resposta errada. Era {resposta_correta}.")
    print()

    print(f"Resposta comentada: {questao_valor['resposta_comentada']}")

    print()

qtd_questoes = len(questoes)
porcentagem_acerto = respostas_certas / qtd_questoes * 100

print(f"Você acertou {respostas_certas} questões.")
print(f"Sua porcentagem de acerto {porcentagem_acerto}%.")
