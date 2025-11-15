if __name__ == '__main__':
    file = open('text.txt', 'r')
    line = file.readline()
    while line:
        print(line, end="")
        line = file.readline()
    file.close()
