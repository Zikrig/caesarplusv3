import razlich,menu
from caesar import caesar_simple as cs
from decryption import menudecr as menud
import pickle
from bigrazl import *

#Чтобы считать частоту употребления текста, запутите нижеследующие несколько строк.
#Обновление словарей из книги.

"""knga=open('kniga.txt','r',encoding='utf-8')
messege=knga.read().lower()
knga.close()
slov = obr(messege)
with open('slov.pickle','wb') as f:
    pickle.dump(slov,f)"""
#Чтобы зашифровать ваш текст, положите его в kniga.txt и запустите это:

"""kl=open('kniga.txt','r',encoding='utf-8')
messege=kl.read().lower()
kniga=open('shifr.txt','w',encoding='utf-8')
shifr = cs(messege.lower(),20,'уюткидва') #можно изменить
kniga.write(shifr)
kl.close()
kniga.close()
"""

#расшифровка шифра
ks=open('shifr.txt','r',encoding='utf-8')
messege=ks.read().lower()
ks.close()

slobr=obr(messege)

with open('slov.pickle','rb') as f:
    sln = pickle.load(f)
#готово два словаря-образца и два на расшифрование
#print(slobr[0])
#print(sln[0])
print(slobr[1])
print(sln[1])
#print(len(sln[0]))

#делаем списки из словарей
nazod=sltolist(slobr[0])
nazdw=sltolist(slobr[1])

normod=sltolist(sln[0])
normdw=sltolist(sln[1])
#print(normdw)
fins = {}
for i in nazod:
    fins[i]="0"

#print(nazod)
#print(nazdw)
#print(normod)
#print(normdw)

Fnazdwstr=listtostr(nazdw)
Fnormdwstr=listtostr(normdw)
nazowstr=listtostr(nazod)
normstr=listtostr(normod)


nazdwstr=''
normdwstr=''
lnaz = len(Fnazdwstr)
for letter in range(lnaz):
    if not Fnazdwstr[letter] in Fnazdwstr[:letter]:
        if not Fnormdwstr[letter] in Fnormdwstr[:letter]:
            nazdwstr+=Fnazdwstr[letter]
            normdwstr+=Fnormdwstr[letter]




#print(nazdwstr)
#print(normdwstr)
#print(nazowstr)
#print(normstr)

for k in range(len(nazdwstr)):
    if fins[nazdwstr[k]] =="0":
        fins[nazdwstr[k]] = normdwstr[k]

a = min(len(nazowstr),len(normstr))

for k in range(a):
    if fins[nazowstr[k]] =="0":
        fins[nazowstr[k]] = normstr[k]
print(fins)

messegenew=''

for l in range(len(messege)):
    bukva =messege[l]
    if bukva.isalpha():
        messegenew+=fins[bukva]
    else:
        messegenew+=bukva

k=open('rash.txt','w',encoding='utf-8')
k.write(messegenew)

"""

print("меню?y/n")
op=input()
if(op=='y'):
    menu.shifr()

kniga=open('shifr.txt','w+',encoding='utf-8')

shifr = cs(messege.lower(),20,'уюткидва')
kniga.write(shifr)
kniga.close()

print("дешифровка?y/n")
op=input()
if(op=='y'):
    menud(shifr)"""



