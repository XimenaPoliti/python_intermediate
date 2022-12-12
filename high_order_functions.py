from functools import reduce


def run():
    items = [
            {
                "product": "blusa",
                "price": 100
                },
            {
                "product": "gorra",
                "price": 20
                },
            {
                "product": "pantalon",
                "price":200
                }
            ]

    odd = list(filter(lambda x : x % 2 != 0 , range(0, 11)))  
    squares = list(map(lambda x : x**2, odd))
    all_add = reduce(lambda x, y: x + y, squares)
    print(odd)
    print(squares)
    print(all_add)
    taxes = list(map(lambda item: {**item,'taxes': item['price']*19} , items))
    print(taxes)


if __name__ == '__main__':
    run()
