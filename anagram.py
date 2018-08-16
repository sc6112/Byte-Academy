def isAnagram(a,b):
    dict1={}
    dict2={}
    str1=a.lower()
    str2=b.lower()
    answer=False
    list1=[]
    list2=[]
    words1=[]
    words2=[]
    list1=(str1.split(" "))
    list2=str2.split(" ")
    for x in range(len(list1)):
        string=list(list1[x])
        for y in range(len(string)):
            words1.append(string[y])
    for x in range(len(list2)):
        string=list(list2[x])
        for y in range(len(string)):
            words2.append(string[y])
    for x in range(len(words1)):
        if (words1[x] not in dict1):
            dict1[words1[x]]=1
        elif (words1[x] in dict1):
            dict1[words1[x]]+=1
    for x in range(len(words2)):
        if (words2[x] not in dict2):
            dict2[words2[x]]=1
        elif (words2[x] in dict2):
            dict2[words2[x]]+=1
    if (dict1==dict2):
        answer=True
        return answer
    else:
        return answer
print isAnagram("I am Sirjan", "Sirjan am I")