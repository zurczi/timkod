from random import randint
from random import *
from numpy import *

def rouletka(prawdo):

    summ=0
    wartosc = random.uniform(0, 1)
    #print(prawdo)
    for i in prawdo.items():
        summ+=i[1]
        if(wartosc<summ):
            y=i[0]
            break
    return y

def words2(prawdo):
    ciag = ''
    for i in range(1000):
        x = rouletka(prawdo)
        ciag = ciag + x
        ciag+=' '
    print("Ciag:",ciag)
    return ciag


def words1(tekst):
    #tab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ','1','2','3','4','5','6','7','8','9','0']
    words_count={}
    suma=0
    tekstTab=tekst.split(' ')
    for i in tekstTab:
        suma+=1
        if (i not in words_count):
            words_count[i]=0
        words_count[i]+=1
    for i in words_count:
        words_count[i]=(words_count[i]/len(tekstTab))
    #lista=sorted(words_count.items(),key=lambda words_count: words_count[1],reverse=True)
    #lenList=len(lista)
    #lista=lista[:6000]
    #sumPra=0
    #for i in lista:
     #   sumPra+=i[1]

    #print(sumPra/suma)
    #print(lista)
    return words_count
def Dictionary2(x):
    dict={}
    tekstTab=x.split(' ')
    w=1
    i=0
    while(w==1):
        obecny=tekstTab[i]+" "+tekstTab[i+1]
        nastepny=tekstTab[i+2]
        if (obecny not in dict):
            dict[obecny]={nastepny:1}
        else :
            if(nastepny not in dict[obecny]):
                dict[obecny][nastepny]=1
            else:
                dict[obecny][nastepny]+=1
        i += 1
        if(i==len(tekstTab)-2):
            break;
    suma=0
    for i in dict:
        for j in dict[i].items():
            suma+=j[1]
        for z in dict[i]:
            dict[i][z]=dict[i][z]/suma
        suma=0

    return dict


def Dictionary(x):
    dict={}
    tekstTab=x.split(' ')
    w=1
    i=0
    while(w==1):
        obecny=tekstTab[i]
        nastepny=tekstTab[i+1]
        if (obecny not in dict):
            dict[obecny]={nastepny:1}
        else :
            if(nastepny not in dict[obecny]):
                dict[obecny][nastepny]=1
            else:
                dict[obecny][nastepny]+=1
        i += 1
        if(i==len(tekstTab)-1):
            break;

    suma=0
    for i in dict:
        for j in dict[i].items():
            suma+=j[1]
        for z in dict[i]:
            dict[i][z]=dict[i][z]/suma
        suma=0

    return dict

def MarkovaFirst(dict,war):
    text=[]
    if(war==False):
        text.append(choice(list(dict.keys())))
    else:
        text.append("probability")
    iterator=0
    for i in range(3000):
        current = text[iterator]
        pCurrent=dict[current]
        next=rouletka(pCurrent)
        text.append(next)
        iterator+=1
    text=' '.join(text)
    print(text)
    return text

def MarkovaSecond(dict,war):
    text = []
    if(war==False):
        new=choice(list(dict.keys()))
        text.append(new[0])
        text.append(new[1])
    if(war==True):
        start="probability"
        for i in dict.keys():
            new=i.split(" ")
            if(new[0]==start):
                text.append(new[0])
                text.append(new[1])
                break;
    iterator = 1
    for i in range(3000):
        current=text[iterator-1]+" "+text[iterator]
        pCurrent = dict[current]
        next = rouletka(pCurrent)
        text.append(next)
        iterator += 1
    text = ' '.join(text)
    print(text)
    return text

def main():
    x = open('./norm_wiki_sample.txt').read()
    print("Markowa Pierwszego Rzędu")
    dict=Dictionary(x)
    MarkovaFirst(dict,False)
    print("Markowa Drugiego Rzędu")
    dict=Dictionary2(x)
    MarkovaSecond(dict,False)
    print("Markowa Pierwszego Rzędu z probability")
    dict=Dictionary(x)
    MarkovaFirst(dict,True)
    print("Markowa Drugiego Rzędu z probability")
    dict=Dictionary2(x)
    MarkovaSecond(dict,True)


if __name__ == "__main__":
    main()