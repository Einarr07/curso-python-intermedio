set_coutries = {
    'Estados unidos',
    'Panama',
    'Venezuela'
}

if __name__ == '__main__':
    print(len(set_coutries))
    print('Estados unidos' in set_coutries)
    print('Peru' in set_coutries)

    # Add
    set_coutries.add('Peru')
    print(f'Add country -> {set_coutries}')

    # Update
    set_coutries.update({'Argentina', 'Brazil', 'Peru'})
    print(f'Update country -> {set_coutries}')

    # Remove
    set_coutries.remove('Panama')
    print(f'Remove country -> {set_coutries}')

    # Discard
    # If not exist, the program next
    set_coutries.discard('Ecuador')
    print(f'Discard country -> {set_coutries}')

    # Clear
    set_coutries.clear()
    print(f'Clear country -> {len(set_coutries)}')
