numbers = []

for number in range(1,11):
    numbers.append(number * 2)


# with list comprehensions
numbers_2 = [number*2 for number in range(1,11)]

# Conditional
numbers_conditional = []

for number in range(1,11):
    if number % 2 == 0:
        numbers_conditional.append(number*2)


if __name__ == '__main__':
    print(f'Normal -> {numbers}')
    print(f'With list comprehension -> {numbers_2}')

    # Conditional
    print(f'Normal conditional -> {numbers_conditional}')

    # With list comprehension
    numbers_conditional_2 = [number * 2 for number in range(1,11) if number % 2 == 0]
    print(f'List comprehension with conditional -> {numbers_conditional_2}')
