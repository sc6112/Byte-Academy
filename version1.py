import random
def battleship():
    board=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
    a=random.randint(0,6)
    b=random.randint(0,6)
    message=""
    board[a][b]=1
    for x in range(10):
        row=raw_input("Enter the row\n")
        column=raw_input("Enter the column\n")
        if board[int(row)-1][int(column)-1]==1:
            message="You win!!"
            break
        elif board[int(row)-1][int(column)-1]!=1 and x==9:
            message="You lost :("
    return message
print battleship()
