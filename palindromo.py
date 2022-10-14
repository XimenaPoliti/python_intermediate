def palindromo(palabra):
    try:
        if len(palabra) == 0:
            raise ValueError('No ingresar una cadena vacía')
        if palabra == palabra[::-1]:
            return "La palabra es un palíndromo"
        else:
            return "No es un palindromo"
    except ValueError as ve:
        print(ve)
        return 'Coloque el valor nuevamente'


def run():
    try:
        palabra = ''
        print(palindromo(palabra))
    except:
        print('Solo ingresar strings')
    


if __name__ == '__main__':
    run()
