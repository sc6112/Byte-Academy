def titlecase(title,exceptions):
        list=title.split(" ")
        l=len(list)
        for x in range(l):
            if x==0:
                t=list[0].lower()
                p=t[0].upper()
                u=""
                for o in range(len(t)):
                    if o==0:
                        u=u+p
                    else:
                        u=u+t[o]
                list[0]=u
            else:
                if list[x] in exceptions:
                    b=list[x].lower()
                    list[x]=b
                else:
                    j=list[x].lower()
                    y=j[0].upper()
                    h=""
                    for g in range(len(j)):
                        if g==0:
                            h=h+y
                        else:
                            h=h+j[g]
                    list[x]=h
        r=""
        for y in range(l):
            if y!=(l-1):
                r=r+list[y]+" "
            else:
                r=r+list[y]
        return (r)
print (titlecase ("the quick brown fox jumps over the lazy dog", ["quick", "brown"]))