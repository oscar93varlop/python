import random
def generate_psswd():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0' ]
    simbolos = ['!','#','$','%','&','/','.',]

    caracteres = mayusculas + minusculas + simbolos + numeros
    passwd = []
    for i in range(15):
        caracter_random = random.choice(caracteres)
        passwd.append(caracter_random)
    passwd = "".join(passwd)
    return passwd
def run():
    passwd = generate_psswd()
    print('Tu nueva contraseña es:' +passwd )


if __name__ == '__main__' :
    run()