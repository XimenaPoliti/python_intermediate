def run ():
    my_list=[1, 'Hola', True, 4.5]
    my_dict={"firstname": "Ximena", "lastname": "Politi"}

    super_list = [
       {"firstname": "X", "lastname": "P"},
       {"firstname": "Xi", "lastname": "Po"},
       {"firstname": "Xim", "lastname": "Pol"},   
       {"firstname": "Xime", "lastname": "Poli"},
       {"firstname": "Ximen", "lastname": "Polit"},
       {"firstname": "Ximena", "lastname": "Politi"}
            ]

    super_dict = {
       "my_list_1":[1, 'Hola', True, 4.5],       
       "my_list_2":[2, 'Hola', True, 4.6],
       "my_list_3":[3, 'Hola', True, 4.7]
            }

    for k,v in super_dict.items():
        print(k, '-', v)

    for i in super_list:
        for k,v in i.items():
            print(k, '-', v)


if __name__ == '__main__':
    run()
