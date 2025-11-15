import csv


def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            print(row)


if __name__ == '__main__':
    read_csv('world_population.csv')
