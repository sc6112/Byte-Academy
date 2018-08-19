import datetime
from datetime import timedelta
def birthday():
    birth=raw_input("Enter your birthdate in YYYY/MM/DD format\n")
    y=""
    m=""
    d=""
    for x in range(len(birth)):
        if x<4:
            y=y+birth[x]
        elif x>4 and x<7:
            m=m+birth[x]
        elif x>7:
            d=d+birth[x]
    year=int(y)
    month=int(m)
    day=int(d)
    birth_date=datetime.date(year,month,day)
    now=datetime.datetime.now()
    number=abs(now.date()-birth_date)
    age=number.days//365
    year=year+age+1
    new=datetime.datetime(year,month,day,0,0,0)
    to_go=abs(new-now)
    print ("Your age is "+str(age)+"\n"+"You also have "+str(to_go)+" to go for your next birthday")
birthday()