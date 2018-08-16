import io
def word_stats(filename, n):
    lines=[]
    with open(filename) as f:
        for line in f:
            lines.append(line)
    list=[]
    dict={}
    for x in range(len(lines)):
        l1=lines[x].split(" ") 
        for y in range(len(l1)):
            if (l1[y].lower() not in dict):
                dict.update({l1[y].lower():1})
            elif (l1[y].lower() in dict):
                dict[l1[y].lower()]+=1
    k=""
    list2=[]
    while (len(dict)>0):
        highest=0
        for key, value in dict.iteritems():
            print ("Y")
            if highest<value:
                highest=value
                k=key
        list2.append([k, highest])
        dict.pop(k,highest)
    for c in range(n):
        print list2[c]
        
word_stats("article 2.txt",5)
        