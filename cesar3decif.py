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

parser = argparse.ArgumentParser(description='Descifra un fichero de texto en codigo cesar con desplazamiento 3')

parser.add_argument("entrada",help="el nombre del fichero a Desencriptar", type=str)

parser.add_argument("-o", dest="outputFile", type=str, metavar="salida.txt",help="especifica el nombre del fichero de salida")

args= parser.parse_args()

if args.outputFile == None:
    print("No se han introducido los parametros correctemante: prog entrada -o salida")
    exit()


f = open(args.entrada,"r")
f2= open (args.outputFile,"w")
text = f.read()
f2.write(encrypt(text,-3))
