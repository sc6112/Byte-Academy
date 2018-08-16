def mc_nug(num):
    list=[]
    if num<6:
        for y in range(1,num+1):
            list.append(y)
    for x in range(1,num+1):
        if x<6:
            list.append(x)
        else:
            if (x%3==0):
                c=0
                for i in range((x//6)+1):
                    for j in range((x//9)+1):
                        if (6*i+9*j==x):
                            c=1
                if (c!=1):
                    list.append(x)
            elif (x%2==0):
                c=0
                for i in range((x//6)+1):
                    for j in range((x//20)+1):
                        if (6*i+20*j==x):
                            c=1
                if (c!=1):
                    list.append(x)
            else:
                c=0
                for i in range((x//6)+1):
                    for j in range((x//20)+1):
                        for k in range((x//9)+1):
                            if (6*i+20*j+9*k==x):
                                c=1
                if (c!=1):
                    list.append(x)
    print list
def new_mc_nug(num):
    list=[]
    if num<4:
        for y in range(1,num+1):
            list.append(y)
    else:
        for x in range(1,num+1):
            if x<4:
                list.append(x)
            else:
                if (x%2==0):
                    c=0
                    for i in range((x//4)+1):
                        for j in range((x//6)+1):
                            for k in range((x//10)+1):
                                if (4*i+6*j+10*k==x):
                                    c=1
                    if (c!=1):
                        list.append(x)
                else:
                    list.append(x)
    print list