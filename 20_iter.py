if __name__ == '__main__':
    for i in range(1, 11):
        print(i)

    ## For manual iteration control, use the reserved word 'next'
    ## Passing the value 1 iteration will throw an exception
    my_iter = iter(range(1, 3))
    print(next(my_iter))  # 1
    print(next(my_iter))  # 2
    print(next(my_iter))  # 3
