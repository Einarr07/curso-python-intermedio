import random

dict = {}

for i in range(1,6):
    dict[i] = i * 2

## Dictionary comprehension
dict_2 = {i: i*2 for i in range(1,6)}

# Countries
countries = ['col', 'mex', 'bol', 'peru']
population = {}

for country in countries:
    population[country] = random.randint(1,100)

## Countries comprehension
population_2 = {country: random.randint(100, 200) for country in countries}

# Users
names = ['Martin', 'John', 'Anne', 'Smith']
ages = [25, 35, 45, 55]

data_users_for = {}
for name, age in zip(names, ages):
    data_users_for[name] = age

# Users comprehension
data_users = {name: age for (name, age) in zip(names, ages)}




if __name__ == '__main__':
    print(f'Normal -> {dict}')
    print(f'Dict comprehension -> {dict_2}')

    print(f'Population -> {population}')
    print(f'Population comprehension -> {population_2}')

    print(f'With two lists -> {data_users_for}')
    print(f'With two lists in comprehension -> {data_users}')