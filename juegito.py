import random
import os
def run():
    IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

    DB = [
        "JAVA",
        "JAVASCRIPT",
        "C",
        "PYTHON",
        "PHP"
    ]
    palabra = random.choice(DB)
    espacios = ["_"] * len(palabra)
    intentos = 6;
    
    while True:
        os.system("cls")
        for caracteres in espacios:
            print(caracteres, end="")
        print(IMAGES[intentos])
        letra = input("Elige una letra").upper()
        found = False
        for idx, caracteres in enumerate(palabra):
            if caracteres == letra:
                espacios[idx] = letra
                found = True
        if not found:
            intentos -= 1
        if "_" not in espacios:
            os.system("cls")
            print("Ganaste")
            break
            input()
        if intentos == 0:
            os.system("cls")
            print("Perdiste")
            break
            input()
if __name__ == '__main__':
    run()