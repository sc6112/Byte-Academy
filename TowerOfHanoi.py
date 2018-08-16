def move(number, start, stop, middle):
    moves=0
    if (number==1):
        moves=1
        return moves
    else:
        return move(number-1,start,middle,stop)+move(1,start,stop,middle)+move(number-1,middle,stop,start)