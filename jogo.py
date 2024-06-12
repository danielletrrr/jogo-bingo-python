import random

def gerar_cartela():
    cartela = []
    for col in range(5):
        if col == 2:  # Coluna do meio com espaço livre
            numeros = random.sample(range(col * 15 + 1, col * 15 + 16), 4)
            cartela.extend(numeros[:2] + [0] + numeros[2:])
        else:
            numeros = random.sample(range(col * 15 + 1, col * 15 + 16), 5)
            cartela.extend(numeros)
    return cartela

def verificar_bingo(cartela, numeros_sorteados):
    # Verificar linhas
    for i in range(0, 25, 5):
        if all(num in numeros_sorteados or num == 0 for num in cartela[i:i+5]):
            return True

    # Verificar colunas
    for i in range(5):
        if all(cartela[i + j * 5] in numeros_sorteados or cartela[i + j * 5] == 0 for j in range(5)):
            return True

    # Verificar diagonal principal
    if all(cartela[i * 6] in numeros_sorteados or cartela[i * 6] == 0 for i in range(5)):
        return True

    # Verificar diagonal secundária
    if all(cartela[(i + 1) * 4] in numeros_sorteados or cartela[(i + 1) * 4] == 0 for i in range(5)):
        return True

    return False

def mostrar_cartela(cartela):
    for i in range(5):
        print(cartela[i*5:(i+1)*5])

########################################################################

numeros_ja_sorteados = []
cartelas = []

quantidade_jogadores = 10  # Para facilitar, reduza a quantidade de jogadores
cartelas_por_jogador = 1   # Cada jogador terá apenas uma cartela

# GERAR CARTELAS
for _ in range(quantidade_jogadores):
    for _ in range(cartelas_por_jogador):
        cartelas.append(gerar_cartela())

# Mostrar todas as cartelas
for i, cartela in enumerate(cartelas):
    print(f"Cartela {i + 1}:")
    mostrar_cartela(cartela)
    print()

# SORTEIO DOS NÚMEROS
jogo_rodando = True
while jogo_rodando:
    numero_sorteado = random.randint(1, 75)
    if numero_sorteado not in numeros_ja_sorteados:
        numeros_ja_sorteados.append(numero_sorteado)
        print(f"Sorteado: {numero_sorteado}")

        for i, cartela in enumerate(cartelas):
            if verificar_bingo(cartela, numeros_ja_sorteados):
                print(f"Bingo na Cartela {i + 1}!")
                mostrar_cartela(cartela)
                jogo_rodando = False
                break

print(f"Finalizado!!!")