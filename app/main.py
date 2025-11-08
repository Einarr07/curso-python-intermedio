import utils

data = [
    {
        'Country': 'Argentina',
        'Population': 400000,
    },
    {
        'Country': 'Brazil',
        'Population': 400000,
    }
]

country = input(f'Enter Country: ')
result = utils.population_by_country(data, country)

if __name__ == '__main__':
    keys, values = utils.get_population()
    print(keys, values)
    print(result)
