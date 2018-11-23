import random
from colorama import Fore

r = random.randint(1,6)

if r == 1:
    print(Fore.RED +
        '''
        ---------
        |       |
        |   O   |
        |       |
        ---------
        '''
    )

elif r == 2:
    print(Fore.GREEN +
        '''
        ---------
        | O     |
        |       |
        |     O |
        ---------
        '''
    )
elif r == 3:
    print(Fore.YELLOW +
        '''
        ---------
        | O     |
        |   O   |
        |     O |
        ---------
        '''
    )
elif r == 4:
    print(Fore.BLUE +
        '''
        ---------
        | O   O |
        |       |
        | O   O |
        ---------
        '''
    )
elif r == 5:
    print(Fore.CYAN +
        '''
        ---------
        | O   O |
        |   O   |
        | O   O |
        ---------
        '''
    )
elif r == 6:
    print(Fore.MAGENTA +
        '''
        ---------
        | O O O |
        |       |
        | O O O |
        ---------
        '''
    )
