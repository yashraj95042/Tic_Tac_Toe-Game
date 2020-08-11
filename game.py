theBoard={"top-L":" ","top-M":" ","top-R":" ","mid-L":" ","mid-M":" ","mid-R":" ","low-L":" ","low-M":" ","low-R":" "}
def printBoard(board):
    print(board['top-L']+'|'+board['top-M']+'|'+board['top-R'])
    print('-+-+-')
    print(board['mid-L']+'|'+board['mid-M']+'|'+board['mid-R'])
    print('-+-+-')
    print(board['low-L']+'|'+board['low-M']+'|'+board['low-R'])
turn='X'
for i in range(9):
    #printBoard(theBoard)
    if (i>4):
        if theBoard['top-L']!=" ":
            if (theBoard['top-L']==theBoard['top-M']and theBoard['top-M']==theBoard['top-R']):
                print('you are winner')
                break
        if theBoard['mid-L']!=" ":
            if (theBoard['mid-L']==theBoard['mid-M']and theBoard['mid-M']==theBoard['top-R']):
                print('you are winner')
                break
        if theBoard['low-L']!=" ":
            if (theBoard['low-L']==theBoard['low-M']and theBoard['low-M']==theBoard['low-R']):
                print('you are winner')
                break
        if theBoard['top-L']!=" ":
            if (theBoard['top-L']==theBoard['mid-L']and theBoard['mid-L']==theBoard['low-L']):
                print('you are winner')
                break
        if theBoard['top-M']!=" ":
            if (theBoard['top-M']==theBoard['mid-M']and theBoard['mid-M']==theBoard['low-M']):
                print('you are winner')
                break
        if theBoard['top-R']!=" ":
            if (theBoard['top-R']==theBoard['mid-R']and theBoard['mid-R']==theBoard['low-R']):
                print("you are a winner")
                break
        if theBoard['top-L']!=" ":
            if (theBoard['top-L']==theBoard['mid-M']and theBoard['mid-M']==theBoard['low-R']):
                print("you are a winner")
                break
        if theBoard['top-R']!=" ":
            if (theBoard['top-R']==theBoard['mid-M']and theBoard['mid-M']==theBoard['low-L']):
                print("you are a winner")
                break
    while(True):
        printBoard(theBoard)
        print('turn for'+ turn+ 'move on which space?')
        move=input()
        if move=='top-L' or move=='top-M' or move=='top-R' or move=='mid-L' or move=='mid-M' or move=='mid-R' or move=='low-L' or move=='low-M' or move=='low-R':
            if theBoard[move]==" ":
                theBoard[move]=turn
                if turn=='X':
                    turn='O'
                else:
                    turn='X'
                break
            else:
                print("place already filled up")

        else:
            print("invalid")
printBoard(theBoard)
input()
    
