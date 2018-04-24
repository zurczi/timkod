from bitarray import bitarray



#encode – tworzy zakodowaną reprezentację tekstu
def encode(text,code):
    codeText=bitarray()
    for t in text:
        for c in code[t]:
            codeText.append(c)
    return codeText

#decode – odkodowuje zakodowany tekst
def decode(code,codeText):
    decodeText=""
    w=0
    i=0

    for i in range(0,len(codeText),6):
        x=bitarray(codeText[i:i+6])
        for d in code.items():
            if(d[1]==x):
                decodeText+=d[0]
    return decodeText
#save – zapisuje kod oraz zakodowany tekst
def save(code,codeText):
    with open('./kod.txt', 'w') as kod:
        for c in code.keys():
            kod.write(c+"\t")
            kod.write(str(code[c].to01())+"\t")
    codeText2 = codeText.copy()
    for x in range(8-codeText2.length() % 8):
        codeText2.append(1)
    with open('./wynik.bin', 'wb') as file:
        codeText2.tofile(file)

#load – wczytuje zakodowany tekst oraz kod
def load():
    codeText = bitarray()
    code= {}
    str = open('./kod.txt').read().split('\t')
    for i in range(0, len(str) - 1, 2):
        if (str[i] not in code):
            code[str[i]] = bitarray(str[i + 1])
    with open('./wynik.bin', 'br') as w:
        codeText.fromfile(w)
    return codeText, code
#create – na podstawie listy częstości poszczególnych znaków tworzy kod
def create():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', ' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    code={}
    i=0
    for a in range(len(alphabet)):
            codeX=bin(i)[2:]
            codeX = bitarray(codeX.rjust(6, '0'))
            code[alphabet[a]]=codeX
            i+=1
    return code


def main():
    x = open('./norm_wiki_sample.txt').read()
    code=create()
    encodeText=encode(x,code)
    save(code,encodeText)
    codeText,code=load()
    text=decode(code,codeText)
    if(x==text):
         print("OK")
    #else:
     #   print("Error")
if __name__ == "__main__":
    main()