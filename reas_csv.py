import csv


def read_csv(path):
    data = []
    with open(path, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            data.append(row)
    return data


if __name__ == '__main__':
    read_csv('world_population.csv')
