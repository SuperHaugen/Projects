import random
import time
from colorama import Fore


def write (write, b = True):
    if b:
        print(colors[random.randint(0, 4)])
    print(write)


r = random.randint(1, 6)


colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA]
print(r)

green = Fore.GREEN

if r == 1:
    write('''
        ---------
        |       |
        |   O   |
        |       |
        ---------
        ''')

elif r == 2:
    write(
          '''
        ---------
        | O     |
        |       |
        |     O |
        ---------
        '''
          )
elif r == 3:
    write(
          '''
        ---------
        | O     |
        |   O   |
        |     O |
        ---------
        '''
          )
elif r == 4:
    write(
          '''
        ---------
        | O   O |
        |       |
        | O   O |
        ---------
        '''
          )
elif r == 5:
    write(
          '''
        ---------
        | O   O |
        |   O   |
        | O   O |
        ---------
        '''
          )
elif r == 6:
    write(
          '''
        ---------
        | O O O |
        |       |
        | O O O |
        ---------
        '''
          )
time.sleep(0.2)
