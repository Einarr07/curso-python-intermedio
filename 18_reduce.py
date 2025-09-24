import functools

numbers = [1, 2, 3, 4]

def accum(counter, item):
    print(f'counter => {counter} item => {item}')
    return counter + item


result = functools.reduce(accum, numbers)

if __name__ == "__main__":
    print(result)