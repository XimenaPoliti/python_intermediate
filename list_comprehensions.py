#def squares(number):
#    list = []
#    for i in range(0,number +1):
#        if i % 3 != 0:
#            list.append(i**2)
#    return list


def run ():
    number = int(input('Escribe el número: '))
#    print(squares(number))
    squares = [i**2 for i in range(0,number+1) if i % 3 != 0]
    print(squares)


if __name__ == '__main__':
    run()


