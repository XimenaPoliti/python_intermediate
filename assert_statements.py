def divisors(number): 
    divisors = []
    for i in range(1, number +1):
        if number % i == 0:
            divisors.append(i)
    return divisors


def run():
    number = input('Ingresa un número: ')
    assert number.isnumeric(), "Ingresar un número"
    print(divisors(int(number)))


if __name__ == '__main__':
    run()   
