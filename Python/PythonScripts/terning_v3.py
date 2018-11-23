import random
import time
from colorama import Fore


def dice (dice0):
    print(colors[random.randint(0, 4)] + '''
        ---------
        | %s %s %s |
        | %s %s %s |
        | %s %s %s |
        ---------
        ''' % (dice0[0][0], dice0[0][1],dice0[0][2],dice0[1][0],dice0[1][1],dice0[1][2],dice0[2][0],dice0[2][1],dice0[2][2]))

r = random.randint(1, 6)

colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA]

dice0 =  [[" "," "," "], [" "," "," "], [" "," "," "]]

if r == 1:
    dice0[1][1] = "0"
elif r == 2:
    dice0[0][0] = dice0[2][2] = "0"
elif r == 3:
    dice0[0][0] = dice0[1][1] = dice0[2][2] = "0"
elif r == 4:
    dice0[0][0] = dice0[0][2] = dice0[2][0] = dice0[2][2] = "0"
elif r == 5:
    dice0[0][0] = dice0[0][2] = dice0[2][0] = dice0[2][2] = dice0[1][1] = "0"
elif r == 6:
    dice0[0][0] = dice0[0][2] = dice0[2][0] = dice0[2][2] = dice0[0][1] = dice0[2][1] =  "0"
dice(dice0)