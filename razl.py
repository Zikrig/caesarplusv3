from bukva import bukva as Letter
def razl(message):
    result = [0 for i in range(32)]
    message = message.lower()
    numberch = 0
    procres = [0.0 for i in range(32)]
    for ch in message:
        numberch += 1

        if (ord(ch) > 1071 and ord(ch) < 1104):
            result[ord(ch) - 1072] += 1
    for i in range(32):
        procres[i] = float(100 * result[i] / numberch)
        #print(str(i)+' '+str(result[i])+' '+chr(i+1072))

    popalf = 'оаеинстлвркмдгуяпыбьзчйшхжюфцщэъ'

    maxr=[]
    newalf = ""
    i = 0
    while (i<32):
        letternum = int(result.index(max(result)))
        maxr.append(max(result))
        newalf += chr(letternum+1072)
        result[letternum] = -1


        i+=1
    alf=[]

    print(newalf)


    for i in range(32):
        alf.append(Letter(popalf[i]))
        #print(alf[i].len())
        verh=i+3
        if verh>32:
            verh=32
        niz=i-3
        if niz<0:
            niz=0
        for bliz in range(niz,verh):
            alf[i].un(newalf[bliz])

    return (alf)

def dvazl(message):
    result=[]
    for l in range(32):
        result.append([])
        for m in range(32):
            result[l].append(0)
    message = message.lower()
    prev = ' '
    for i in message:
        pr = ord(prev)
        nast = ord(i)

        if ((pr > 1071) and (pr < 1104) and (nast > 1071) and (nast < 1104)):
            result[pr - 1072][nast - 1072] += 1
        prev = i

    return(result)

