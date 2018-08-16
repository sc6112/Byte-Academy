import datetime
def age_to_time():
    a=raw_input("How old are you?")
    b=int(a)
    m=b*12
    d=m*30
    h=d*24
    mi=h*60
    s="months : "+ str(m)+", days : "+str(d)+", hours : "+str(h)+", and minutes : "+str(mi)
    return (s)
    
def birthdate_to_time():
    a=raw_input("What is you birthday in `YYYY-MM-DD` format?")
    now=datetime.datetime.now()
    y=""
    m=""
    d=""
    for x in range(len(a)):
        if x<4:
            y=y+a[x]
        elif x>4 and x<7:
            m=m+a[x]
        elif x>7:
            d=d+a[x]
    year=int(y)
    month=int(m)
    day=int(d)
    age=0
    if (now.month-month)>=0 and (now.day-day)>=0:
        age=now.year-year
    else:
        age=now.year-year-1
    k=age*12
    j=k*30
    g=j*24
    r=g*60
    s="months : "+ str(k)+", days : "+str(j)+", hours : "+str(g)+", and minutes : "+str(r)
    return (s)