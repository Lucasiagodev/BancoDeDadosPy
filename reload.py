import time, random

def reload():
    contador = 0
    max_contador = random.randint(1,7)  # garante pelo menos 1 repetição

    roda = ['_', '\\', '|', '/'] 
    
    while contador < max_contador:
        for item in roda:
            # \r volta ao início da linha e apaga caracteres antigos
            print('\r' + item + '     ', end='', flush=True)
            time.sleep(0.3)  # tempo entre cada passo

        # opcional: apagar completamente antes da próxima rodada
        print('\r' + ' ' * 5, end='', flush=True)
        
        contador += 1

    

reload()
