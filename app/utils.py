def get_population():
    keys = ['arg', 'bra']
    values = [300, 400]
    return keys, values


def population_by_country(data, country):
    result = list(filter(lambda item: item['Country'] == country, data))
    if not result:
        return 'This country does not exist'
    return result
