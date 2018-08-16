def isPermutation(list):
    ans=True
    for x in range(1,len(list)+1):
        if x in list:
            ans= True
        elif x not in list:
            ans= False
            break
    return ans