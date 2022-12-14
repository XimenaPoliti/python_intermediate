import csv


def dict_with_data(clave, value):
    iterable = zip(clave, value)
    country_dict = {clave : value for clave, value in iterable}
    return country_dict


def read_csv():
    with open("./archivos/world_population.csv", "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = list(map(lambda value: dict_with_data(header, value) ,reader))
        return data


def run():
    data = read_csv()
    print(data[0])


if __name__ == '__main__':
    run()

