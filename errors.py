def run():
    try:
        print(0/0)
    except Exception as error:
        print(error)

    print('- Except')

    try:
        assert 1!=1, "Error de assert"
    except Exception as error:
        print(error)

    print('- Assert')

    try:
        
        if 10 > 100: 
            print('Hola')
        else:
            raise Exception('Error raise')
    except Exception as error:
        print(error)

    print('- Raise')


    try:
        print(0/0)
        assert 1!=1, "Error de assert"
        if 10 > 100: 
            print('Hola')
        else:
            raise Exception('Error raise')
        print('Estoy en el try')
    except ZeroDivisionError as error:
        print(error)
    except AssertionError as error:
        print(error)
    except Exception as error:
        print(error)


if __name__ == '__main__':
    run()
