import datetime
def today_day():
    now = datetime.datetime.now()
    y=str(now.year)
    final=""
    y2=y[2]+y[3]
    year=int(y2)
    y3=round(year/4)
    start=now
    days={"Sunday":0, "Monday":1, "Tuesday":2,"Wednesday":3, "Thursday":4, "Friday":5, "Saturday":6}
    new_year=(-1+year+y3)%7
    doom=""
    if (now.year%4==0):
        new_year+=3
        if (new_year>6):
            new_year-=7
        start=datetime.date(now.year,1,4)
    elif (now.year%4!=0):
        new_year+=2
        if (new_year>6):
            new_year-=7
        start=datetime.date(now.year,1,3)
    for k,v in days.iteritems():
        if (new_year==v):
            doom=k
    date_1=start
    number=abs(now.date()-date_1)
    c=number.days%7
    e=new_year+c
    if (e>6):
        e=e-7
    for k,v in days.iteritems():
        if (v==e):
            final=k
    return final
print today_day()