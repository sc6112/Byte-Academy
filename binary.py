def convertor(num):
    string=""
    if (num==1):
        return "1"
    else:
        return convertor(num//2)+str(num%2)