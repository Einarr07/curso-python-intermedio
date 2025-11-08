import sys
import re
import time
import collections

# Module re
text = 'My phone number is: 311 123 321, the country code is 54, my favorite number is 3'
result = re.findall('[0-9]+', text) # Returns a list of strings: ['311', '123', '321', '54', '3']

# Module time
timestamp = time.time()
local = time.localtime()
result_time = time.asctime(local)

# Module collections
numbers = [1,2,3,4,3,12,32,32,4,3,1,2,43,]
counter = collections.Counter(numbers)
# Counter builds a frequency map like {3: 3, 2: 2, 4: 2, 1: 2, 32: 2, 12: 1, 43: 1}

if __name__ == "__main__":
    print(f'The path is -> {sys.path}')
    print(f'The numbers are -> {result}')
    print(f'The time is -> {result_time}')
    print(f'The collection is -> {counter}')