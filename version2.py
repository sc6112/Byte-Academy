import random
def battleship():
    board1=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
    board2=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
    a=random.randint(0,6)
    b=random.randint(0,6)
    message=""
    board1[a][b]=1
    board2[a][b]=1
    s=True
    c=0
    while (s):
        if c%2==0:
            row=raw_input("Enter the row player 1\n")
            column=raw_input("Enter the column player 1\n")
            if board1[int(row)-1][int(column)-1]==1:
                message="You win player 1!!"
                s=False
        elif c%2!=0:
            row=raw_input("Enter the row player 2\n")
            column=raw_input("Enter the column player 2\n")
            if board2[int(row)-1][int(column)-1]==1:
                message="You win player 2!!"
                s=False
        c+=1
    return message
print battleship()