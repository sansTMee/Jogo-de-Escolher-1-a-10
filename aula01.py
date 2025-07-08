import random
def random_game():


    print("Bem vindo ao Random Game")

    numero = 0
    contador = 0
    numeroAleatorio = random.randint(1,10)

    while True:
        try:
            numero = int(input("Escolha um numero de 1 a 10"))
            if numero == numeroAleatorio:
                print("\033[92mAcertou!!!\033[0m")
                break
            else:
                contador = contador + 1
                if numero < numeroAleatorio:
                    print("O numero que você digitou é menor que o numero escolhido")
                else:
                    print("O numero que você digitou é maior que o escolhido")
                    if contador == 3:
                        print("\033[91mErrou!!!\033[0m")
                        print(f"O numero correto era: {numeroAleatorio}")
                        break
                    else:
                        print("Numero errado, tente de novo...\n")
        
        except ValueError:
            print("Por favor, insire um numero valido")


def adivinhação():
    print("/n--- Bem vindo ao jogo de adivinhação de palavras! ---")
    print("Você recebera dicas para adivinhar a palavra secreta. 5 tentativas")
    #list
    palavras = {
        "python": "Uma linguagem de progamação muito popular",
        "computador": "Máquina essencial para pogramar",
        "internet": "Conecta você ao mundo digital",
        "tecnologia": "Esta sempre em evolução e inovação",
        "algoritimo": "Sequência de passos para resolver problemas"
    }
    
    palavra_secreta, dica = random.choice(list(palavras.items()))
    tentativas = 5 

    while tentativas > 0:
        print(f"\nDicas: {dica}")
        print(f"Tentativas restantes: {tentativas}")

        repostas = input("Qual a palavra secreta?").lower()

        if repostas == palavra_secreta:
            print("\n Parabéns! Você acertou a palavra:", palavra_secreta)
            break
        else:
            tentativas -= 1
            print("Palavra errada! Tente novamente.")
    
    if tentativas == 0:
       print("\n Você perdeu! A palavra era:", palavra_secreta)
    print("--- Fim do jogo. ---\n")

def main_menu():
    while True:
        print("=============================")
        print("    MENU DE JOGOS PYTHON     ")
        print("=============================")
        print("1. Number Game")
        print("2. Word Game")
        print("3. Sair")
        print("=============================")

        escolha = input("Escolha uma opção (1, 2 ou 3): ")

        if escolha == "1":
            random_game()
        elif escolha == "2":
                adivinhação()
        elif escolha =="3":
                print("Obrigado por jogar! Até a proxima")
                break
        else:
            print("Opção invalida. Por favor, escolha 1, 2 ou 3")
        print("\n")

if __name__== "__main__":
    main_menu()
