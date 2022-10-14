import math

def run():
#    my_dict = {}
#    for i in range(0, 100):
#        if i % 3 != 0:
#            my_dict[i]=i**3
#    print(my_dict)

#    my_dict = {i: i**3 for i in range(0,100) if i % 3 != 0}
#    print(my_dict)
    my_dict_1 = {i: math.sqrt(i) for i in range(0,1000) if i % 3 != 0}
    print(my_dict_1)


if __name__ == '__main__':
    run()
