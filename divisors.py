def list_of_divisors(num):
    list=[]
    for x in range(1,num+1):
        if num%x==0:
            list.append(x)
    return list
def divisors(num):
    list=list_of_divisors(num)
    s="["
    for y in range(len(list)):
        if y!=len(list)-1:
            s=s+str(list[y])+", "
        else:
            s=s+str(list[y])+"]"
    return s
def sum_of_divisors(num):
    list=list_of_divisors(num)
    sum=0
    for y in range(len(list)):
        sum=sum+list[y]
    return sum
def num_of_divisors(num):
    list=list_of_divisors(num)
    return len(list)
def totatives(num):
    list=list_of_divisors(num)
    tote=[]
    for x in range(1,num):
        c=0
        for y in range(len(list)):
            if x%list[y]==0:
                c+=1
        if (c<2):
            tote.append(x)
    s="["
    for y in range(len(tote)):
        if y!=len(tote)-1:
            s=s+str(tote[y])+", "
        else:
            s=s+str(tote[y])+"]"
    return s
def totient(num):
    list=list_of_divisors(num)
    tote=[]
    for x in range(1,num):
        c=0
        for y in range(len(list)):
            if x%list[y]==0:
                c+=1
        if (c<2):
            tote.append(x)
    return len(tote)