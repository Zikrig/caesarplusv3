
def obr(stroka):
    odngram={}
    bgram={}
    for i in range(len(stroka)-1):
        if stroka[i].isalpha():
            if stroka[i] in odngram:
                odngram[stroka[i]]+=1
            else:
                odngram[stroka[i]]=1

            if stroka[i+1].isalpha():
                if stroka[i:i+2] in bgram:
                    bgram[stroka[i:i+2]]+=1
                else:
                    bgram[stroka[i:i+2]] = 1
    i=0
    chist={}
    while(i<50):
        maxa=0
        for a in bgram:
            na=int(bgram[a])
            if na>maxa:
                maxa=na
                znach=a

        chist[znach]=maxa
        bgram[znach] = 0
        i+=1

    chistodn={}
    maxa=1
    while maxa!=0:
        maxa=0
        for letter in odngram:
            na = int(odngram[letter])
            if na > maxa:
                maxa = na
                znach = letter

        odngram[znach]=0
        if(maxa!=0):
            chistodn[znach]=maxa

    return chistodn,chist


def sltolist(a):
    maxel=1
    maxz=''
    fin=[]
    while(maxel>0):
        maxel=0
        for el in a:
            if int(a[el])>maxel:
                maxel=a[el]
                maxz=el
                a[el]='0'
        fin.append(maxz)
    return(fin)


def listtostr(list):
    str=''
    for i in list:
        str+=i
    return(str)