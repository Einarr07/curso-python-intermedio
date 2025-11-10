import utils

data = [
    {
        'Country': 'Argentina',
        'Population': 400000,
    },
    {
        'Country': 'Brazil',
        'Population': 50000,
    }
]


def run():
    keys, values = utils.get_population()
    print(f'Keys -> {keys}, Values -> {values}')

    # Country input
    country = input(f'Enter Country: ')
    result = utils.population_by_country(data, country)
    print(result)


if __name__ == '__main__':
    run()
