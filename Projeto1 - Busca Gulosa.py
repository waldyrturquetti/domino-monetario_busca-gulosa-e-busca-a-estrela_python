import random
from random import randint

JOGADOR_CONSEGUE_JOGAR = True
AGENTE_CONSEGUE_JOGAR = True
JOGADOR = 'Jogador'
COMPUTADOR = 'Computador'
POUPANCA_COMPUTADOR = 0
POUPANCA_JOGADOR = 0

print("Início de Jogo: obrigatório escolher a maior peça de valores iguais para começar a partida.")


def jogadorJoga(pecasJogador, mesa, pecas):
    global JOGADOR_CONSEGUE_JOGAR
    print("\033[92m {}\033[00m".format('Peças mesa:'))
    imprimeMesa(mesa)

    print("\033[93m {}\033[00m".format('Pecas Jogador:'))
    imprimePecasJogador(pecasJogador)

    verificaSePrecisaComprar(pecasJogador, mesa, pecas, JOGADOR)
    if not pecas and mesa and pecasJogador:
        JOGADOR_CONSEGUE_JOGAR = verificaSeTemComoJogar(mesa, pecasJogador)

    if JOGADOR_CONSEGUE_JOGAR:
        print('Qual peça você deseja Jogar? Favor inserir o número indicador da peça.', end='')
        qualPeca = int(input())

        onde = 0
        if mesa:
            print('Digite 1 para jogar no canto ESQUERDO ou 2 para Jogar no canto DIREITO:', end='')
            onde = int(input())

        jogar(mesa, pecasJogador, qualPeca, onde, JOGADOR)


def buscaGulosa(pecasAgente, mesa):
    notas = [[0, 0], [0.05, 0], [0.1, 0], [0.25, 0], [0.5, 0], [1, 0], [2, 0], [5, 0], [10, 0], [20, 0], [50, 0], [100, 0], [200, 0]]

    for peca in pecasAgente:
        for nota in notas:
            if peca[0] == nota[0] or peca[1] == nota[0]:
                nota[1] += 1

    if not mesa:
        valor = max(notas, key=lambda i: i[1])[0]
        possiveisEscolhas = []
        for peca in pecasAgente:
            if peca[0] == valor or peca[1] == valor:
                possiveisEscolhas.append(peca)
        pecaEscolhida = escolheUmaPeca(possiveisEscolhas, valor)
        qual = pecasAgente.index(pecaEscolhida) + 1
        return qual, 0
    else:
        pecaEsquerda = mesa[0][0]
        pecaDireita = mesa[len(mesa) - 1][1]
        while True:
            valor = max(notas, key=lambda i: i[1])
            if valor[1] == 0:
                return -1, 0
            if valor[0] == pecaEsquerda or valor[0] == pecaDireita:
                possiveisEscolhas = []
                for peca in pecasAgente:
                    if peca[0] == valor[0] or peca[1] == valor[0]:
                        possiveisEscolhas.append(peca)
                pecaEscolhida = escolheUmaPeca(possiveisEscolhas, valor[0])
                qual = pecasAgente.index(pecaEscolhida) + 1
                if pecaEscolhida[0] == pecaEsquerda or pecaEscolhida[1] == pecaEsquerda:
                    return qual, 1
                if pecaEscolhida[0] == pecaDireita or pecaEscolhida[1] == pecaDireita:
                    return qual, 2
            else:
                notas.remove(valor)


def escolheUmaPeca(pecasEscolhidas, valorReferencia):
    maior = -1
    pecaEscolhida = None
    for peca in pecasEscolhidas:
        if peca[0] == valorReferencia:
            if peca[1] > maior:
                maior = peca[1]
                pecaEscolhida = peca
        elif peca[1] == valorReferencia:
            if peca[0] > maior:
                maior = peca[0]
                pecaEscolhida = peca

    return pecaEscolhida


def agenteJoga(pecasAgente, mesa, pecas):
    global AGENTE_CONSEGUE_JOGAR

    verificaSePrecisaComprar(pecasAgente, mesa, pecas, COMPUTADOR)
    if not pecas and mesa and pecasAgente:
        AGENTE_CONSEGUE_JOGAR = verificaSeTemComoJogar(mesa, pecasAgente)

    if AGENTE_CONSEGUE_JOGAR:
        qualPeca, onde = buscaGulosa(pecasAgente, mesa)
        jogar(mesa, pecasAgente, qualPeca, onde, COMPUTADOR)


def imprimePecasJogador(mesa):
    for peca in mesa:
        print("\033[93m {}\033[00m".format(
            str(mesa.index(peca) + 1) + ': ' + '[ ' + str(peca[0]) + ' | ' + str(peca[1]) + ' ]'))
    print()


def imprimeMesa(mesa):
    for peca in mesa:
        print("\033[92m {}\033[00m".format('[ ' + str(peca[0]) + ' | ' + str(peca[1]) + ' ]'),
              end="\033[92m {}\033[00m".format(' | '))
    print()


def verificaSeTemComoJogar(mesa, mao):
    pecaEsquerda = mesa[0][0]
    pecaDireita = mesa[len(mesa) - 1][1]

    for peca in mao:
        if peca[0] == pecaEsquerda or peca[0] == pecaDireita:
            return True
        if peca[1] == pecaEsquerda or peca[1] == pecaDireita:
            return True

    return False


def verificaSePrecisaComprar(mao, mesa, pecas, entidade):
    if not mesa or not pecas:
        return

    pecaEsquerda = mesa[0][0]
    pecaDireita = mesa[len(mesa) - 1][1]

    while True:
        for peca in mao:
            if peca[0] == pecaEsquerda or peca[1] == pecaEsquerda:
                return
            if peca[0] == pecaDireita or peca[1] == pecaDireita:
                return

        if pecas:
            print("\033[96m {}\033[00m".format(entidade + ' Comprou Uma Peça'))
            compraPeca(pecas, mao)
            if entidade == JOGADOR:
                print(*['Peças', entidade])
                imprimePecasJogador(mao)
        else:
            break


def jogar(mesa, mao, qual, onde=0, entidade=''):
    if qual == -1 and onde == 0:
        print(*[entidade, 'não pode jogar. Não há peças disponíveis para compra.'])
        return

    if not mesa:
        peca = mao[qual - 1]
        mesa.append(peca)
        mao.remove(peca)
    else:
        if onde == 1:
            pecaEsquerda = mesa[0][0]
            pecaEscolhida = mao[qual - 1]

            if pecaEscolhida[0] == pecaEsquerda or pecaEscolhida[1] == pecaEsquerda:
                if pecaEscolhida[1] == pecaEsquerda:
                    mesa.insert(0, pecaEscolhida)
                    mao.remove(pecaEscolhida)
                else:
                    mesa.insert(0, tuple(reversed(pecaEscolhida)))
                    mao.remove(pecaEscolhida)
            else:
                print("\033[91m {}\033[00m".format('Erro: Peça escolhida inválida'))
                return

        elif onde == 2:
            pecaDireita = mesa[len(mesa) - 1][1]
            pecaEscolhida = mao[qual - 1]

            if pecaEscolhida[0] == pecaDireita or pecaEscolhida[1] == pecaDireita:
                if pecaEscolhida[0] == pecaDireita:
                    mesa.append(pecaEscolhida)
                    mao.remove(pecaEscolhida)
                else:
                    mesa.append(tuple(reversed(pecaEscolhida)))
                    mao.remove(pecaEscolhida)
            else:
                print("\033[91m {}\033[00m".format('Erro: Peça escolhida inválida'))
                return

        else:
            print("\033[91m {}\033[00m".format('Opção Inválida'))
            return


def verificaQuemInicia(pecasJogador, pecasAgente):
    notas = [0, 0.05, 0.1, 0.25, 0.5, 1, 2, 5, 10, 20, 50, 100, 200]
    notas.reverse()
    jogadores = [JOGADOR, COMPUTADOR]

    for i in notas:
        if pecasJogador.count((i, i)) > 0:
            return jogadores[0]
        if pecasAgente.count((i, i)) > 0:
            return jogadores[1]

    return random.choice(jogadores)


def compraPeca(pecas, mao):
    if pecas:
        peca = random.choice(pecas)
        mao.append(peca)
        pecas.remove(peca)
    else:
        print('Impossível comprar peça, acabaram as peças para comprar.')


def distribuiPecas(pecas):
    jogador = []
    agente = []

    for _ in range(13):
        pecaJogador = pecas[randint(0, len(pecas) - 1)]
        jogador.append(pecaJogador)
        pecas.remove(pecaJogador)

        pecaAgente = pecas[randint(0, len(pecas) - 1)]
        agente.append(pecaAgente)
        pecas.remove(pecaAgente)

    return jogador, agente


def depositaPoupanca(mao, poupanca):
    for peca in mao:
        poupanca += peca[0]
        poupanca += peca[1]

    return poupanca


def verificaQuemGanhou(pecasJogador, pecasAgente):
    if len(pecasJogador) < len(pecasAgente):
        return JOGADOR
    elif len(pecasJogador) > len(pecasAgente):
        return COMPUTADOR
    else:
        return 'EMPATE'


def geraPecas():
    notas = [0, 0.05, 0.1, 0.25, 0.5, 1, 2, 5, 10, 20, 50, 100, 200]

    pecas = []
    for i in notas:
        for j in notas:
            if pecas.count((i, j)) == 0 and pecas.count((j, i)) == 0:
                pecas.append((i, j))

    return pecas


if __name__ == '__main__':

    for _ in range(3):
        mesa = []
        pecas = geraPecas()

        pecasJogador, pecasAgente = distribuiPecas(pecas)
        quemInicia = verificaQuemInicia(pecasJogador, pecasAgente)

        quemGanhou = None
        while pecasJogador and pecasAgente:
            if quemInicia == JOGADOR:
                jogadorJoga(pecasJogador, mesa, pecas)
                agenteJoga(pecasAgente, mesa, pecas)
                print('Peças:', end='')
                print(pecas)
                if not JOGADOR_CONSEGUE_JOGAR and not AGENTE_CONSEGUE_JOGAR:
                    quemGanhou = verificaQuemGanhou(pecasJogador, pecasAgente)
                    break
            elif quemInicia == COMPUTADOR:
                agenteJoga(pecasAgente, mesa, pecas)
                jogadorJoga(pecasJogador, mesa, pecas)
                print('Peças:', end='')
                print(pecas)
                if not JOGADOR_CONSEGUE_JOGAR and not AGENTE_CONSEGUE_JOGAR:
                    quemGanhou = verificaQuemGanhou(pecasJogador, pecasAgente)
                    break

        if not pecasJogador or quemGanhou == JOGADOR:
            POUPANCA_JOGADOR = depositaPoupanca(pecasAgente, POUPANCA_JOGADOR)
            print('Você venceu!')
        elif not pecasAgente or quemGanhou == COMPUTADOR:
            POUPANCA_COMPUTADOR = depositaPoupanca(pecasJogador, POUPANCA_COMPUTADOR)
            print('O Computador venceu!')
        elif quemGanhou == 'EMPATE':
            print('EMPATE')

        JOGADOR_CONSEGUE_JOGAR = True
        AGENTE_CONSEGUE_JOGAR = True

    print(*['Poupança Jogador', POUPANCA_JOGADOR])
    print(*['Poupança Computador', POUPANCA_COMPUTADOR])
