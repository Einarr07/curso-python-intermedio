def increment(x):
    return x + 1

result = increment(10)

if __name__ == '__main__':
    print(result)

    increment_2 = lambda x : x + 1
    print(increment_2(20))

    full_name = lambda name, last_name : f'Full name is {name} {last_name}'
    print(full_name('Enrique', 'Segoviano'))


