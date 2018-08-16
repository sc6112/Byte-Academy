def toRoman(num):
    if (num/1000>=1):
        return (num//1000)*"M"+toRoman(num%1000)
    elif (num/900>=1):
        return (num//900)*"CM"+toRoman(num%900)
    elif (num/500>=1 and num/500<4):
        return (num//500)*"D"+toRoman(num%500)
    elif (num/400>=1):
        return (num//400)*"CD"+toRoman(num%400)
    elif (num/100>=1 and num/100<4):
        return (num//100)*"C"+toRoman(num%100)
    elif (num/90>=1):
        return (num//90)*"XC"+toRoman(num%90)
    elif (num/50>=1 and num/50<4):
        return (num//50)*"L"+toRoman(num%50)
    elif (num/40>=1):
        return (num//40)*"XL"+toRoman(num%40)
    elif (num/10>=1 and num/10<4):
        return (num//10)*"X"+toRoman(num%10)
    elif (num/9>=1):
        return (num//9)*"IX"+toRoman(num%9)
    elif (num/5>=1 and num/5<4):
        return (num//5)*"V"+toRoman(num%5)
    elif (num/4>=1):
        return (num//4)*"IV"+toRoman(num%4)
    elif (num/1>=1 and num/1<4):
        return (num//1)*"I"+toRoman(num%1)
    else:
        return ""
print toRoman(1998)