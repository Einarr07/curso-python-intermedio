if __name__ == '__main__':
    file = open('text.txt', 'r+')
    for line in file:
        print(line + " \n")
    file.writelines("\nHello World")
    file.close()
