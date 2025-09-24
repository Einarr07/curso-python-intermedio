numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_numbers = filter(lambda num: num % 2 == 0, numbers)

if __name__ == "__main__":
    print(list(new_numbers))