import random

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
