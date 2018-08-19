import datetime
from datetime import timedelta
def double_day(p):
    birth1=raw_input("Enter first birthdate in YYYY/MM/DD format\n")
    birth2=raw_input("Enter second birthdate in YYYY/MM/DD format\n")
    now=datetime.datetime.now()
    y=""
    m=""
    d=""
    for x in range(len(birth1)):
        if x<4:
            y=y+birth1[x]
        elif x>4 and x<7:
            m=m+birth1[x]
        elif x>7:
            d=d+birth1[x]
    year=int(y)
    month=int(m)
    day=int(d)
    date1=datetime.date(year,month,day)
    y=""
    m=""
    d=""
    for x in range(len(birth2)):
        if x<4:
            y=y+birth2[x]
        elif x>4 and x<7:
            m=m+birth2[x]
        elif x>7:
            d=d+birth2[x]
    year=int(y)
    month=int(m)
    day=int(d)
    date2=datetime.date(year,month,day)
    age1=abs(now.date()-date1)
    age2=abs(now.date()-date2)
    n=str(age1.days)
    m=str(age2.days)
    num1=int(n)
    num2=int(m)
    x=0
    a=True
    final=now
    if (num1>num2):
        current=date2
        while(a):
            current=current+timedelta(days=1)
            age1=abs(current-date1)
            a1=age1.days
            age2=abs(current-date2)
            a2=age2.days
            if a1==p*a2 or a2==a1*p:
                a=False
            x+=1
            final=date2+timedelta(days=x)
    b=True
    if (num2>num1):
        current=date1
        while(b):
            current=current+timedelta(days=1)
            age1=abs(current-date1)
            a1=age1.days
            age2=abs(current-date2)
            a2=age2.days
            if a1==p*a2 or a2==a1*p:
                b=False
            x+=1
            final=date1+timedelta(days=x)
    return "Your "+p +" day is "+str(final)