from random import randint
from numpy import *
import math


def wczytajplik(plik):
    text = open(plik, 'rb').read()
    print(text)
    return text

def srednia(tekst):
    tekst2=tekst.split(" ")
    sum=0
    dl=len(tekst2)
    for i in tekst2:
        if(len(i)>0):
            sum+=len(i)
        else:
            dl=dl-1
    print(sum/dl)
    return sum/dl

def generator():
    ciag=''
    tab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', ' ','1','2','3','4','5','6','7','8','9','0']
    for i in range(1000000):
        x=tab[randint(0,(len(tab)-1))]
        ciag=ciag+x
    print(ciag)
    return ciag

def rouletka(wartosc,prawdo):
    tab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', ' ','1','2','3','4','5','6','7','8','9','0']
    suma=0
    y=''
    for i in range(len(prawdo)):
        suma=suma+prawdo[i]
        if(wartosc<suma):
            y=tab[i]
            break
    return y


def czestoscLiter2(tekst):
    tab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', ' ','1','2','3','4','5','6','7','8','9','0']

    wynik=zeros(len(tab))
    for i in tekst:
        for j in range(len(tab)):
            if(i==tab[j]):
                wynik[j]+=1
                continue
    wynik=((wynik/len(tekst)))
    #print(wynik)
    return wynik

def czestoscLiter(tekst):
    tab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', ' ','1','2','3','4','5','6','7','8','9','0']
    char_count={}
    for i in tekst:
        if (i not in char_count):
            char_count[i]=0
        char_count[i]+=1
    for i in char_count:
        char_count[i]=(char_count[i]/len(tekst))
    print(char_count.items())
    return char_count

def zad4(tekst,czestosc):
    tab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', ' ','1','2','3','4','5','6','7','8','9','0']
    pierwsza=tab[argmax(czestosc)]
    for i in range(len(czestosc)):
        if(czestosc[i]==max(czestosc)):
            czestosc[i]=0.0
            break
    druga=tab[argmax(czestosc)]
    print("pierwsza:",pierwsza,"druga:",druga)
    dlaPierwsza=zeros(len(tab))
    dlaDruga=zeros(len(tab))
    tekst=tekst[:3000]
    for i in range(len(tekst)):
        if(tekst[i]==pierwsza):
            nast=tekst[i+1]
            tu=tab.index(nast)
            dlaPierwsza[tu]+=1
        if(tekst[i]==druga):
            nast=tekst[i+1]
            tu = tab.index(nast)
            dlaDruga[tu]+=1
    print("dlaPierwsza\n",(dlaPierwsza/3000),"\ndlaDruga\n",(dlaDruga/3000))

def generujKolejna(tekst,literka):
    tab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', ' ','1','2','3','4','5','6','7','8','9','0']
    prawdo=zeros(len(tab))
    tekst=tekst[:3000]

    for i in range(len(tekst)-1):
        if(tekst[i]==literka):
            nast=tekst[i+1]
            tu=tab.index(nast)
            prawdo[tu]+=1
    print(prawdo)
    wynik=tab[argmax(prawdo)]
    return wynik

def SlownikDlaPierwszego(tekst):
    tekst = tekst[:100000]
    slownik=[]
    prawdo=[]
    suma=0
    for i in tekst:
        if(slownik.count(i)>0):
            continue
        else:
            slownik.append(i)
            for j in range(len(tekst)-1):
                if(tekst[j]==i):
                    suma+=1
                    if (prawdo.count(tekst[j+1])==0):
                        prawdo.append(tekst[j+1])
                        prawdo.append(1)
                    else:
                        prawdo[prawdo.index(tekst[j+1])+1]+=1
            for z in range(1,len(prawdo),2):
                prawdo[z]=prawdo[z]/suma
            slownik.append(prawdo)
            prawdo=[]
            suma=0
    #print(slownik)
    return slownik

def Slownik(tekst,n):
    slownik=[]
    prawdo=[]
    i=1
    iterator=0
    while(i==1):
        obecny=tekst[iterator:iterator+n]
        nastepny=tekst[iterator+n]
        if(slownik.count(obecny)>0):
            obecnyIndex=slownik.index(obecny)
            prawdoIndex=obecnyIndex+1
            if(slownik[prawdoIndex].count(nastepny)>0):
                nastepnyIndex=slownik[prawdoIndex].index(nastepny)
                (slownik[prawdoIndex])[nastepnyIndex+1]+=1
            else:
                slownik[prawdoIndex].append(nastepny)
                slownik[prawdoIndex].append(1)
        else:
            slownik.append(obecny)
            prawdo.append(nastepny)
            prawdo.append(1)
            slownik.append(prawdo)
        prawdo=[]
        iterator += 1
        if(iterator==len(tekst)-n):
            break;
    suma=0
    for i in range(len(slownik)):
        if(i%2!=0):
            for j in range(len(slownik[i])):
                if(j%2!=0):
                    suma+=(slownik[i])[j]
            for z in range(len(slownik[i])):
                if (z % 2 != 0):
                    slownik[i][z]=slownik[i][z]/suma
        suma=0
    #print(slownik)
    return slownik

def rouletka(prawdo):
    suma=0
    y=''
    wartosc = random.uniform(0, 1)
    if(len(prawdo)>0):
        for i in range(1,len(prawdo),2):
            suma=suma+prawdo[i]
            if(wartosc<suma):
                y=prawdo[i-1]
                break
    return y

def MarkovaSlownik(slownik,n):
    nowyTekst="probability"
    for i in range(30000):
        obecna = nowyTekst[len(nowyTekst)-n:len(nowyTekst)]
        try:
            indeks=slownik.index(obecna)
        except ValueError:
            indeks=-1
        if(indeks<0):
            continue
        else:
            prawdoObecna=slownik[indeks+1]
            nast=rouletka(prawdoObecna)
            nowyTekst+=nast
    print(nowyTekst)
    return nowyTekst

def Markova(tekst,n):
    nowyTekst="probability"
    for i in range(3000):
        obecna = nowyTekst[len(nowyTekst)-n:len(nowyTekst)]
        indeks=tekst.find(obecna,randint(0,(len(tekst)-2*n)),len(tekst)-n)
        if(indeks>0):
            indeks=indeks+n
            nowyTekst+=tekst[indeks]
    print(nowyTekst)
    return nowyTekst
def entropia(prawdo):

    H=0
    for a in prawdo:

        H+= a* math.log(a,2)
    H=-H
    print(H)
    return H


def main():
    x = open('./norm_wiki_sample.txt').read()
    y=czestoscLiter2(x)
    entropia(y)
    '''
    print("Ciag Markova Pierwszego")
    slownik=SlownikDlaPierwszego(x)
    z=MarkovaSlownik(slownik,1)
    print("Srednia:")
    print(srednia(z))

    print("Ciag Markova Piatego z find")
    y=Markova(x,5)
    print("Srednia:")
    print(srednia(y))

    print("Ciag Markova Trzeciego z find")
    y=Markova(x,3)
    print("Srednia:")
    print(srednia(y))

    print("Ciag Markova Trzeciego ze słownikiem")

    slownik=Slownik(x,3)
    z=MarkovaSlownik(slownik,3)
    print("Srednia:")
    print(srednia(z))

    print("Ciag Markova Piatego ze słownikiem")

    slownik=Slownik(x,5)
    print(slownik)
    z=MarkovaSlownik(slownik,5)
    print("Srednia:")
    print(srednia(z))
    '''


if __name__ == "__main__":
    main()
