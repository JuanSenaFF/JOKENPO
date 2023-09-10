import random as rd
import emoji
import time as tm

# Primeira mensagem exibida no jogo
mensagem = ("\33[32m-" * 10 + "J O K E N P O" + "-" *  10 + "\33[m")
print(mensagem)

# Declaração de variáveis globais
vitorias_jogador = 0
vitorias_maquina = 0

# Função para o jogador escolher
def jogador_escolhe():
    opcoes = {
        "1": "PEDRA" + emoji.emojize("👊"),
        "2": "PAPEL"  + emoji.emojize("✋"),
        "3": "TESOURA" + emoji.emojize('✌')   
    }
    # Loop para garantir que o jogador faça uma escolha válida
    while True:
        jogada_jogador = input("Faça sua jogada:\n"
            "[ 1 ] PEDRA " + emoji.emojize("👊\n") +
            "[ 2 ] PAPEL " + emoji.emojize("✋\n") +
            "[ 3 ] TESOURA " + emoji.emojize('✌\n') +
            "Sua escolha: ").strip().lower()
        if jogada_jogador in opcoes:
            return opcoes[jogada_jogador]
        else:
            print("\33[31mOpção invalida, digite uma das opções a cima.\33[m")

# Função da maquina escolher
def maquina_escolhe():
    opcoes_maquina = ["PEDRA" + emoji.emojize("👊"), "PAPEL" + emoji.emojize("✋"), "TESOURA" + emoji.emojize('✌')]
    jogada_maquina = rd.choice(opcoes_maquina)
    return jogada_maquina

# Função para deterinar o vencedor da rodada  
def decidindo_vencedor(jogador, maquina):
    global vitorias_jogador, vitorias_maquina
    
    # Remove os emojis para facilitar a comparação
    # Sem isso os pontos irão apenas para a maquina
    jogador_sem_emoji = jogador.replace(emoji.emojize("👊"), "").replace(emoji.emojize("✋"), "").replace(emoji.emojize("✌"), "")
    maquina_sem_emoji = maquina.replace(emoji.emojize("👊"), "").replace(emoji.emojize("✋"), "").replace(emoji.emojize("✌"), "")
    
    # Verifica se a maquina empatou
    if jogador_sem_emoji == maquina_sem_emoji:
        print("Empate!")
    
    # Veirifica se o jogador ganhou    
    elif (jogador_sem_emoji == "PEDRA" and maquina_sem_emoji == "TESOURA") or \
        (jogador_sem_emoji == "TESOURA" and maquina_sem_emoji == "PAPEL") or \
        (jogador_sem_emoji == "PAPEL" and maquina_sem_emoji == "PEDRA"):
        vitorias_jogador += 1
        return "jogador"
    
    # Caso contrario, a maquina ganhou    
    else:
        vitorias_maquina += 1
        return "maquina"
    
# Contagem regressiva
def contagem_regressiva():
    print("\33[32mJO")
    tm.sleep(1)
    print("KEN")
    tm.sleep(1)
    print("PO!!!\33[m")
    tm.sleep(1)
    print("-=" * 12)
    
#Função para jogar uma rodada    
def jogar_jokenpo():
    global jogador, maquina
    jogador = jogador_escolhe()
    maquina = maquina_escolhe()
    contagem_regressiva()
    print("Jogador" + emoji.emojize("😀") + " jogou:", jogador)
    print("Computador" + emoji.emojize("👾") + " jogou:", maquina)
    print("-=" * 12)
    placar = decidindo_vencedor(jogador, maquina)
    print(F"\33[32m P L A C A R\33[m\n"
            "Você: ",vitorias_jogador, "\n"
            "Computador: ", vitorias_maquina)

# Função para jogar mais uma partida    
def jogar_novamente():
    global vitorias_jogador, vitorias_maquina
    while True:
        jogar_de_novo = str(input("Digite [S/N] se deseja continuar: ")).strip().upper()
        
        # Verifica se a opção é SIM e inicia uma nova partida
        if jogar_de_novo == "S":
            jogar_jokenpo()
            
        # Veirifica se a opção é NÃO e imprimi o placar.    
        elif jogar_de_novo == "N":
            print(f"Foi divertido enquanto durou\n"
                "33[32m P L A C A R   F I N A L\33[m\n"
                "Você:", vitorias_jogador, 
                "Computador:", vitorias_maquina)
            break
        else:
            print("\33[31Opção invalida, digite [S/N] se deseja continuar.\33[m")

# Inicio do jogo
jogar_jokenpo()
jogar_novamente()