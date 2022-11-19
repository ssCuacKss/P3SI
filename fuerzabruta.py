import sys
import argparse

def encrypt(text,s):
    result = ""
    for i in text:
        if i.isalpha():
            num = ord(i)
            num+=s
            if i.isupper():
                if(num>ord('Z')):
                    num-=26
                elif(num<ord('A')):
                    num+=26
            elif i.islower():
                if(num>ord('z')):
                    num-=26
                elif(num<ord('a')):
                    num+=26
            result+=chr(num)
        else:
            result+=i
    return result

parser = argparse.ArgumentParser(description='Descifra un fichero de texto en codigo cesar por fuerza bruta')

parser.add_argument("entrada",help="el nombre del fichero a Desencriptar", type=str)


args= parser.parse_args()



f = open(args.entrada,"r")
text = f.read()
for i in range(26):
    clave = "clave : "+ str(i) + " " + encrypt(text,-i)
    print(clave)
