from random import randint
from random import *
from typing import Dict

from numpy import *


def czestoscZnakow(tekstTab,n):
    words_count={}
    suma=0
    w=1
    i=0
    while(w==1):
        obecny=tekstTab[i:i+n]
        suma+=1
        if (obecny not in words_count):
            words_count[obecny]=0
        words_count[obecny]+=1
        if(i==len(tekstTab)-n):  #-n
            break;
        i+=1
    for i in words_count:
        words_count[i]=(words_count[i]/len(tekstTab))
    return words_count



def entropia(prawdo):
    H=0
    for a in prawdo.items():
        H+= a[1]* math.log(a[1],2)
    H=-H
    return H

def czestoscSlow(tekst,n):
    words_count={}
    suma=0
    tekstTab=tekst.split(' ')
    w=1
    i=0
    while(w==1):
        obecny=" ".join(tekstTab[i:i+n])
        suma+=1
        if (obecny not in words_count):
            words_count[obecny]=0
        words_count[obecny]+=1
        if(i==len(tekstTab)-n):  #-n
            break;
        i+=1
    for i in words_count:
        words_count[i]=(words_count[i]/len(tekstTab))
    return words_count

def Dictionary(x,n):
    dict={}
    tekstTab=x.split(' ')
    w=1
    i=0
    while(w==1):
        obecny=" ".join(tekstTab[i:i+n])
        #obecny=tekstTab[i]   #tu ze wiecej biore
        nastepny=tekstTab[i+n]  #+n
        if (obecny not in dict):
            dict[obecny]={nastepny:1}
        else :
            if(nastepny not in dict[obecny]):
                dict[obecny][nastepny]=1
            else:
                dict[obecny][nastepny]+=1
        i += 1
        if(i==len(tekstTab)-n):  #-n
            break;
    suma=0
    for i in dict:
        for j in dict[i].items():
            suma+=j[1]
        for z in dict[i]:
            dict[i][z]=dict[i][z]/suma
        suma=0
    return dict

def entropiaWarunkowa(prawdoWar,prawdo):
    H=0
    for x in prawdoWar.items():
        pX=prawdo[x[0]]
        for y in x[1].items():
            pXY=y[1]*pX
            H+= pXY* math.log(y[1],2)
    H=-H
    return H

def DictionaryChar(tekstTab,n):
    dict={}
    w=1
    i=0
    while(w==1):
        obecny=tekstTab[i:i+n]
        #obecny=tekstTab[i]   #tu ze wiecej biore
        nastepny=tekstTab[i+n]  #+n
        if (obecny not in dict):
            dict[obecny]={nastepny:1}
        else :
            if(nastepny not in dict[obecny]):
                dict[obecny][nastepny]=1
            else:
                dict[obecny][nastepny]+=1
        i += 1
        if(i==len(tekstTab)-n):  #-n
            break;
    suma=0
    for i in dict:
        for j in dict[i].items():
            suma+=j[1]
        for z in dict[i]:
            dict[i][z]=dict[i][z]/suma
        suma=0
    return dict



def main():

   # x = open('./norm_wiki_en.txt').read()
    '''
    znaki=czestoscZnakow(x,1)
    entr=entropia(znaki)
    print("Język angielski. Entropia znaków")
    print(entr)

    znakiW=DictionaryChar(x,1)
    entr=entropiaWarunkowa(znakiW,znaki)
    print("Język angielski. Entropia warunkowa pierwszego rzędu-znaki")
    print(entr)

    znakiW = DictionaryChar(x, 2)
    znaki=czestoscZnakow(x,2)
    entr = entropiaWarunkowa(znakiW, znaki)
    print("Język angielski. Entropia warunkowa drugiego rzędu-znaki")
    print(entr)

    znakiW = DictionaryChar(x, 3)
    znaki=czestoscZnakow(x,3)
    entr = entropiaWarunkowa(znakiW, znaki)
    print("Język angielski. Entropia warunkowa trzeciego rzędu-znaki")
    print(entr)

    slowa=czestoscSlow(x,1)
    entr=entropia(slowa)
    print("Język angielski. Entropia słów")
    print(entr)

    slownik=Dictionary(x,1)
    entr=entropiaWarunkowa(slownik,slowa)
    print("Język angielski. Entropia warunkowa pierwszego rzędu")
    print(entr)

    slownik=Dictionary(x,2)
    slowa = czestoscSlow(x, 2)
    entr=entropiaWarunkowa(slownik,slowa)
    print("Język angielski. Entropia warunkowa drugiego rzędu")
    print(entr)

    slownik=Dictionary(x,3)
    slowa = czestoscSlow(x, 3)
    entr=entropiaWarunkowa(slownik,slowa)
    print("Język angielski. Entropia warunkowa trzeciego rzędu")
    print(entr)

    #---------------------------------------------------------------------------------
    x = open('./norm_wiki_la.txt').read()
    znaki = czestoscZnakow(x,1)
    entr = entropia(znaki)
    print("Język łaciński. Entropia znaków")
    print(entr)

    znakiW = DictionaryChar(x, 1)
    entr = entropiaWarunkowa(znakiW, znaki)
    print("Język łaciński. Entropia warunkowa pierwszego rzędu-znaki")
    print(entr)

    znakiW = DictionaryChar(x, 2)
    znaki = czestoscZnakow(x, 2)
    entr = entropiaWarunkowa(znakiW, znaki)
    print("Język łaciński. Entropia warunkowa drugiego rzędu-znaki")
    print(entr)

    znakiW = DictionaryChar(x, 3)
    znaki = czestoscZnakow(x, 3)
    entr = entropiaWarunkowa(znakiW, znaki)
    print("Język łaciński. Entropia warunkowa trzeciego rzędu-znaki")
    print(entr)

    slowa = czestoscSlow(x, 1)
    entr = entropia(slowa)
    print("Język łaciński. Entropia słów")
    print(entr)

    slownik = Dictionary(x, 1)
    entr = entropiaWarunkowa(slownik, slowa)
    print("Język łaciński. Entropia warunkowa pierwszego rzędu")
    print(entr)

    slownik = Dictionary(x, 2)
    slowa = czestoscSlow(x, 2)
    entr = entropiaWarunkowa(slownik, slowa)
    print("Język łaciński. Entropia warunkowa drugiego rzędu")
    print(entr)

    slownik = Dictionary(x, 3)
    slowa = czestoscSlow(x, 3)
    entr = entropiaWarunkowa(slownik, slowa)
    print("Język łaciński. Entropia warunkowa trzeciego rzędu")
    print(entr)
'''
    #------------------------------------------------------------
    x = open('./sample4.txt').read()

    znaki = czestoscZnakow(x,1)
    entr = entropia(znaki)
    print("Sample1. Entropia znaków")
    print(entr)


    znakiW = DictionaryChar(x, 1)
    entr = entropiaWarunkowa(znakiW, znaki)
    print("Sample5. Entropia warunkowa pierwszego rzędu-znaki")
    print(entr)

    znakiW = DictionaryChar(x, 2)
    znaki = czestoscZnakow(x, 2)
    entr = entropiaWarunkowa(znakiW, znaki)
    print("Sample5. Entropia warunkowa drugiego rzędu-znaki")
    print(entr)

    znakiW = DictionaryChar(x, 3)
    znaki = czestoscZnakow(x, 3)
    entr = entropiaWarunkowa(znakiW, znaki)
    print("Sample5. Entropia warunkowa trzeciego rzędu-znaki")
    print(entr)
"""
    slowa = czestoscSlow(x, 1)
    entr = entropia(slowa)
    print("Sample0. Entropia słów")
    print(entr)

    slownik = Dictionary(x, 1)
    entr = entropiaWarunkowa(slownik, slowa)
    print("Sample0. Entropia warunkowa pierwszego rzędu")
    print(entr)

    slownik = Dictionary(x, 2)
    slowa = czestoscSlow(x, 2)
    entr = entropiaWarunkowa(slownik, slowa)
    print("Sample0. Entropia warunkowa drugiego rzędu")
    print(entr)

    slownik = Dictionary(x, 3)
    slowa = czestoscSlow(x, 3)
    entr = entropiaWarunkowa(slownik, slowa)
    print("Sample0. Entropia warunkowa trzeciego rzędu")
    print(entr)
"""
if __name__ == "__main__":
    main()