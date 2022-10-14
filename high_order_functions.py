from functools import reduce


def run():
    odd = list(filter(lambda x : x % 2 != 0 , range(0, 11)))  
    squares = list(map(lambda x : x**2, odd))
    all_add = reduce(lambda x, y: x + y, squares)
    print(odd)
    print(squares)
    print(all_add)


if __name__ == '__main__':
    run()
