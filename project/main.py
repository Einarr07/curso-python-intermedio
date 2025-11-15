import charts
import reas_csv
import utils


def run():
    data = reas_csv.read_csv('../world_population.csv')
    country = input('Choose a country: ')

    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(labels, values)


if __name__ == '__main__':
    run()
