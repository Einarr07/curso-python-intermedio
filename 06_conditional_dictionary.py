import random

peripherals = ['mouse', 'keyboard', 'headphones', 'usb port', 'cable usb']

result = {peripheral: value
          for peripheral in peripherals
          for value in [random.randint(30, 100)]
          if value > 80
          }

# Example 2
text = 'Hi, how are you?'
unique = {c: text.count(c)
          for c in text
          if c in 'aeiou'
          }

if __name__ == '__main__':
    print(result)

    print(unique)

