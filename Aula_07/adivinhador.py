
from random import randint

while True:
    tentativas = []
    contador_tentativas = 0
    numero = 0

    numeroAleatorio = randint(1,10)

    while numero != numeroAleatorio:
        
        numero = int(input("\nDe 1 a 10, qual é o seu palpite?\n\nR.: "))
       

        if numero in tentativas:
            print("\nja foi mano\n")

        else:
            tentativas.append(numero)
            contador_tentativas += 1

            if numeroAleatorio > numero:
                print("\ntenta de novo, maior kk")

            elif numeroAleatorio < numero: 
                print("\nmenor mano, tenta dnv lkk")

            elif numeroAleatorio == numero:
                print(f"\npronto, acertou em {contador_tentativas} mano")

