import sys
import gzip
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


parser = argparse.ArgumentParser(description='Descifra un fichero de texto en codigo cesar con desplazamiento 3 despues de descomprimirlo del formato gzip')

parser.add_argument("entrada",help="el nombre del fichero a Desencriptar", type=str)

parser.add_argument("-o", dest="outputFile", type=str, metavar="salida.txt",help="especifica el nombre del fichero de salida")

args= parser.parse_args()

if args.outputFile == None:
    print("No se han introducido los parametros correctemante: prog desplazamiento entrada -o salida")
    exit()




comp = args.entrada
text = ""
with gzip.open(comp,"rb") as file:
    text = file.read()

f2= open (args.outputFile,"w")
f2.write(encrypt(text,-12))
