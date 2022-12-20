
import string
import random
import argparse

#esp_freq = {'a':12.53,'b':1.4,'c':4.68,'d':5.86,'e':13.18,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}

text_freq = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}

parser = argparse.ArgumentParser(description='Cifra un fichero de texto en codigo cesar con desplazamiento k')

parser.add_argument("entrada",help="el nombre del fichero a encriptar", type=str)


args= parser.parse_args()



f = open(args.entrada,"r")
text = f.read()
text = text.lower()

for ch in text:
    if(ch.isalpha() & (ch != "á") & (ch != "é") & (ch != "í") & (ch != "ó") & (ch != "ú") & (ch != "ñ")):
        text_freq[ch] += 1


print(text_freq)

count = 0

for rep in text_freq:
    count += text_freq[rep]

print(count)

for rep in text_freq:
    text_freq[rep] = round((text_freq[rep]/count)*100,2)

print(text_freq)

