def currency_converter(num):
    h=0
    if num//100>=1:
        h=num//100
    left=num%100
    fif=0
    if left//50>=1:
        fif=left//50
    left=left%50
    t=0
    if left//10>=1:
        t=left//10
    left=left%10
    fiv=0
    if left//5>=1:
        fiv=left//5
    left=left%5
    o=0
    if left//1>=1:
        o=left//1
    left=left%1
    q=0
    if left//0.25>=1:
        q=left//0.25
    left=left%0.25
    fc=0
    if left//0.05>=1:
        fc=left//0.05
    left=left%0.05
    p=0
    if left//0.01>=1:
        p=left//0.01
    s= str(h)+" $100 bills, "+str(fif)+" $50 bills, "+ str(t)+" $10 bills, "+str(o)+" $1 bills, "+str(q)+" quarters, "+str(fc)+" nickels, "+str(p)+" pennies" 
    return s