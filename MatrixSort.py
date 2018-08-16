def matrix():
    string=""
    list=[]
    l1=[]
    list_acc_rows=[]
    list_acc_cols=[]
    for i in range(2):
        if i<1:
            string+=raw_input()+"\n"
        else:
            string+=raw_input()
    list=string.split("\n")
    l1=string.split("\n")
    for x in range(len(list)):
        list[x]=list[x].split(" ")
        l1[x]=l1[x].split(" ")
    l2=[]
    c=len(list[0])
    r=len(list)
    sum_rows=[]
    for x in range(r):
        sum=0
        for y in range(c):
            sum+=int(list[x][y])
        sum_rows.append(sum)
    print sum_rows
    print ("\n")
    sum_cols=[]
    for x in range(c):
        sum=0
        for y in range(r):
            sum+=int(list[y][x])
        sum_cols.append(sum)
    print sum_cols
    print ("\n")
    while(len(sum_rows)>0):
        greatest=0
        greatest_row=0
        for x in range(len(sum_rows)):
            if sum_rows[x]>greatest:
                greatest=sum_rows[x]
                greatest_row=x
        list_acc_rows.append(l1[greatest_row])
        l1.remove(l1[greatest_row])
        sum_rows.remove(greatest)
    for x in range(c):
        new=[]
        for y in range(r):
            new.append(list[y][x])
        l2.append(new)
    while(len(sum_cols)>0):
        greatest=0
        greatest_col=0
        for x in range(len(sum_cols)):
            if sum_cols[x]>greatest:
                greatest=sum_cols[x]
                greatest_col=x
        list_acc_cols.append(l2[greatest_col])
        l2.remove(l2[greatest_col])
        sum_cols.remove(greatest)
    for x in range(r):
        print list_acc_rows[r-x-1]
    print ("\n")
    final=[]
    for x in range(r):
        new=[]
        for y in range(c):
            new.append(list_acc_cols[y][x])
        final.append(new)
    f2=[]
    for x in range(r):
        new=[]
        for y in range(c):
            new.append(final[x][c-y-1])
        f2.append(new)
    for x in range(r):
        print f2[x]
matrix()