from random import choice

# Default Settings
words = ['python', 'java', 'kotlin', 'javascript']  # Possible words
inputs = set()  # List of attempts
lives = 8  # Number of attempts
set_lives = 8  # Number of attempts fixed (Settings)


def play():
    global lives, inputs
    the_word = choice(words)  # Random word
    hint = "-" * len(the_word)
    print(f'\nRecuerda ingresar únicamente letras en minúscula.\n\nLista de palabras:\n{words}')
    while lives > 0:
        print(f'\nVidas restantes: {lives}\n{hint}')
        if '-' not in hint:
            print('\nAdivinaste!\nHas sobrevivido!')
            inputs = set()
            break
        attempt = input(f'Ingresa una letra: ')

        def error():
            if len(attempt) != 1:
                print('ERROR: Debes ingresar una sola letra.')
                return True
            elif not attempt.isascii() or not attempt.islower():
                print('ERROR: Esto no es una letra ASCII minúscula.')
                return True
            elif attempt in inputs:
                print('ERROR: Ya ingresaste esta letra.')
                return True
            return False

        if error():
            continue
        elif attempt in set(the_word):
            hint = list(hint)
            for n in range(len(the_word)):
                if the_word[n] == attempt:
                    hint[n] = attempt
            hint = "".join(hint)
        else:
            print('La letra no está en la palabra, pierdes una vida!')
            lives -= 1
        inputs.add(attempt)

    else:
        print(f'\nEstás ahorcado!\nLa palabra era "{the_word}"')
    lives = set_lives


def settings():
    global words, lives, set_lives
    while True:
        setting = input(f'\n¿Qué deseas cambiar?\n- palabras\n- vidas\n- volver\n\n> ')
        if setting == 'palabras':
            while True:
                print(f'\nPalabras: {words}')
                option = input(f'¿Quieres agregar o eliminar palabras?\n- agregar\n- eliminar\n- volver\n\n> ')
                if option == 'agregar':
                    while True:
                        n_word = input(f'\nIngresa la palabra (únicamente ASCII) que deseas agregar o "VOLVER" para'
                                       f' regresar: ')
                        if n_word == 'VOLVER':
                            break
                        elif not n_word.isascii():
                            break
                        else:
                            words.append(n_word.lower().strip())
                            print(f'La palabra "{n_word.lower().strip()}" ha sido agregada satisfactoriamente!')
                        continue
                elif option == 'eliminar':
                    while True:
                        try:
                            n_word = input(f'\nIngresa la palabra exacta que deseas eliminar o "VOLVER" para regresar'
                                           f':  ')
                            if n_word == 'VOLVER':
                                break
                            else:
                                words.remove(n_word)
                                print(f'La palabra "{n_word}" ha sido eliminada satisfactoriamente!')
                        except:
                            print('\nERROR: La palabra ingresada no está en la lista de palabras.')
                        continue
                elif option == 'volver':
                    break
                else:
                    print('\nERROR: Opción incorrecta.')

        elif setting == 'vidas':
            while True:
                print(f'\nVidas: {lives}')
                option = input('¿Quieres aumentar o reducir vidas?\n- aumentar\n- reducir\n- volver\n\n> ')
                if option == 'aumentar':
                    n_lives = int(input('Ingresa la cantidad de vidas que deseas agregar: '))
                    lives += n_lives
                    print(f'{n_lives} vidas agregadas satisfactoriamente!')
                    continue
                elif option == 'reducir':
                    while True:
                        n_lives = int(input('\nIngresa la cantidad de vidas que deseas eliminar: '))
                        if lives - n_lives < 0:
                            print('\nERROR: No puede haber menos de 0 vidas.')
                            continue
                        else:
                            lives -= n_lives
                            print(f'{n_lives} vidas eliminadas satisfactoriamente!')
                            break
                    continue

                elif option == 'volver':
                    break

                else:
                    print('\nERROR: Opción incorrecta.\n')
            set_lives = lives

        elif setting == 'volver':
            break

        else:
            print('\nERROR: Opción incorrecta.')


def menu():
    print('H A N G M A N\nAVISO: Los ajustes se reestablecen cada vez que se reinicia el programa.')
    while True:
        action = input(f'\nMENU PRINCIPAL:\nIngresa una opción:\n-jugar\n-ajustes\n-salir\n\n> ')
        if action == 'jugar':
            play()
        elif action == 'ajustes':
            settings()
        elif action == 'salir':
            break
        else:
            print('\nERROR: Opción incorrecta.')


menu()
