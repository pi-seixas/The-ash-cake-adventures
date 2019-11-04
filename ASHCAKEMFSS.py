# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 11:18:14 2019

@author: pisei
"""

def carregar_cenarios():
    cenarios = {
        "introdução": {
            "titulo": "Ponte de controle da Nautilus",
            "descricao": "Tudo parecia ok até que BOOOOOOOOOOOOM! A nave que a Nautilus estava escoltndo explode e cai no planeta abaixo levando a preciosa carga junto. O que você quer fazer capitão?",
            "opcoes": {
                "ignorar": "Tomar o elevador para o andar do professor",
                "enviar equipe de resgate": "Ir para a biblioteca"
            }
        },
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "professor": "Falar com o professor"
            }
        },
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {}
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada"
            }
        }
    }
    nome_cenario_atual = "introdução"
    return cenarios, nome_cenario_atual


def main():
    print("The ash cake adventures")
    print("------------------")
    print()
    print("Voce esta observando o vasto vazio do espaço, sete anos de missão como Comandante da Nautillus," 
          "levando uma carga desconhecida a um planeta novo."
          "Tudo parecia bem, faltam apenas duas semanas para o fim desta viagem inacabável,"
          "ou seja, nada pode dar errado.")
    print()
    print("O seu comunicador começa a apitar, ao acioná-lo, surge um holograma do sargento Diaz, "
        "o oficial responsável pela Exploradora, a nave que você está escoltando, e que contém a tão"
        "preciosa carga. O holograma está instável, e você não consegue entender uma palavra dita por Diaz,"
        "quando BOOOOOOOOOOOOOOOOOOM a explosão soou pela sala de comando enquanto a tripulação pasma olhava "
        "os restos da nave ewscoltada eram puxados pela atmosfera do plantea próximo, levando os tripulantes e a carga consigo..."
        "O que você vai fazer Comandante?")
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]

        # Aluno A: substitua este comentário pelo código para imprimir 
        # o cenário atual.

        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:

            # Aluno B: substitua este comentário e a linha abaixo pelo código
            # para pedir a escolha do usuário.
            escolha = ""

            if escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()