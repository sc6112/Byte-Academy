def encrypt():
    message=raw_input("Enter message \n")
    shift=raw_input("Enter shift number \n")
    new=""
    for x in range(len(message)):
        a=ord(message[x])
        if (int(shift)>0):
            if (a<65 or a>122):
                new=new+chr(a)
            else:
                b=a+int(shift)
                if(b>122):
                    new=new+chr(b-58).lower()
                else:
                    new+=chr(b)
        elif(int(shift)<0):
            if (a<65 or a>122):
                new=new+chr(a)
            else:
                b=a+int(shift)
                if (b<65):
                    new=new+chr(b+58).lower()
                else:
                    new+=chr(b)
    return new

def decrypt():
    message=raw_input("Enter message \n")
    shift=raw_input("Enter shift number \n")
    new=""
    for x in range(len(message)):
        a=ord(message[x])
        if (int(shift)>0):
            if (a<65 or a>122):
                new=new+chr(a)
            else:
                b=a-int(shift)
                if (b<65):
                    new=new+chr(b+58).lower()
                else:
                    new+=chr(b)
        elif(int(shift)<0):
            if (a<65 or a>122):
                new=new+chr(a)
            else:
                b=a-int(shift)
                if(b>122):
                    new=new+chr(b-58).lower()
                else:
                    new+=chr(b)
    return new