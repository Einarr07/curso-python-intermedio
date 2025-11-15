if __name__ == '__main__':
    try:
        age = 10
        if age <= 18:
            raise Exception('Age must be greater than or equal to 18')
        print(0 / 0)
        assert 1 != 1, "One no is equal to one"
    except ZeroDivisionError as error:
        print(error)
    except AssertionError as error:
        print(error)
    except Exception as error:
        print(error)

    print('Continue')
