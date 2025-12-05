# reload.py
import time, random

def reload():  # Linha 1
    contador = 0
    max_contador = random.randint(1,7)
    roda = ['_', '\\', '|', '/'] 
    
    while contador < max_contador:
        for item in roda:
            print('\r' + item + '     ', end='', flush=True)
            time.sleep(0.3)

        print('\r' + ' ' * 5, end='', flush=True)
        contador += 1

    return  # Linha 17: evita mostrar None

