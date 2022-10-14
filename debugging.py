def divisors(number):
    divisors = []
    for i in range(1, number +1):
        if number % i == 0:
            divisors.append(i)
    return divisors


def run():
    try:
        number = int(input('Ingresa un número: '))
        if number < 0:
            raise ValueError
        print(divisors(number))
    except ValueError as ve:
        print('Ingresar solo números positivos')


if __name__ == '__main__':
    run()
