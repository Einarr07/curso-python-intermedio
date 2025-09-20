price = 100 # Global

def increment()-> int:
    price = 200
    result = price + price
    return result

if __name__ == '__main__':
    print(increment())