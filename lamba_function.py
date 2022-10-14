def run():
    palindrome = lambda string : string == string[::-1]

    print(palindrome('ana'))
    print(palindrome('xime'))

    square = lambda number : number**2

    print(square(2))
    print(square(3))
    print(square(4))
    print(square(5))

    add = lambda a, b : a + b

    print(add(7,9))



if __name__ == '__main__':
    run()
