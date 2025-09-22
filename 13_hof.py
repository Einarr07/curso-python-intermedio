def increment(x) -> int:
    return x + 1

def high_order_function(x, func) -> int:
    return x + func(x)

if __name__ == '__main__':
    print(high_order_function(1, increment))

    increment_2 = lambda i : i + 1
    high_order_function_2 = lambda x, func : x + func(x)

    print(f'Lambda version -> {high_order_function_2(2, increment_2)}')