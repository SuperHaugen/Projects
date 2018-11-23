import random

def printBoard():
    
    print(
    '''
      |  |
    %s | %s| %s
    ---------
      |  |
    %s |%s | %s
    ---------
      |  |
    %s | %s| %s
    ''' % (ruter[0][0],ruter[0][1],ruter[0][2],ruter[1][0],ruter[1][1],ruter[1][2],ruter[2][0],ruter[2][1],ruter[2][2]))

def checkWin():
    for x in range(0,7):
        print("X= ",x)
        a = wincomb[x][0]
        print("a= ",a)
        b = wincomb[x][1]
        print("b= ",b)
        c = wincomb[x][2]
        print("c= ",c)


        if(a == b == c and a != ' '):
            print('game is over!')
            global notwon
            notwon = 0


#gameboard
ruter = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]


#                           0                                          1                                          2                                               3                                          4                                                 5                                        6                                       7                                      
wincomb = [ [ ruter[0][0],ruter[0][1],ruter[0][2] ], [ ruter[1][0], ruter[1][1], ruter[1][2] ], [ ruter[2][0], ruter[2][1], ruter[2][2] ], [ ruter[0][0], ruter[1][0], ruter[2][0] ], [ ruter[0][1],ruter[1][1],ruter[2][1] ], [ ruter[0][2], ruter[1][2], ruter[2][2] ], [ ruter[0][0],ruter[1][1],ruter[2][2] ], [ ruter[0][2],ruter[1][1],ruter[2][0] ] ]

#wincondision
notwon = 1

#printing the board
printBoard()

while notwon != 0:
    input0 = input('write "y" to start, "q" to quit')
    #to start game print y
    if input0 == "y":
        
        print('game started')
        while notwon != 0:
            while notwon != 0:
                input0 = input("player1's turn:")
                if len(input0) == 2 and ruter[int(input0[0])][int(input0[1])] == ' ':
                    ruter[int(input0[0])][int(input0[1])] = 'x'
                    printBoard()
                    checkWin()
                    print("notwon", notwon)
                    print(ruter)
                    break
            
            while notwon != 0:
                input0 = input("player2's turn:")
                if len(input0) == 2 and ruter[int(input0[0])][int(input0[1])] == ' ':
                    ruter[int(input0[0])][int(input0[1])] = '0'
                    printBoard()                   
                    checkWin()
                    print("notwon", notwon)
                    print(ruter)
                    break
    
    #to quit game type q
    elif input == 'q':
        break
    
   
    
    
    print('quit')
    break