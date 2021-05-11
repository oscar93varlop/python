import random

def run():
    num_aleatoreo = random.randint(1, 100)
    num_elegido = int(input('elige un numero del 1 al 100: '))
    while num_elegido != num_aleatoreo:
        if num_elegido < num_aleatoreo:
            print('Intenta con un numero más grande')
        else:
            print('Busca un numero más pequeño')
        num_elegido = int(input('escribe otro numero: '))
    print('Es numero es el correcto')


if __name__ == '__main__':
    run()