def find_volume(length=1, width=1, depth=9):
    return length * width * depth, depth, 'Im part of funtion'

if __name__ == '__main__':
    result, depth, text = find_volume(width=2)
    print(result)
    print(depth)
    print(text)