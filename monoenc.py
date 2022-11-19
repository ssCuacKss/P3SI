import string
import random
import argparse


key_dict = {'a':'m','b':'n','c':'b','d':'v','e':'c','f':'x','g':'z','h':'a','i':'s','j':'d','k':'f','l':'g','m':'h','n':'j','o':'k','p':'l','q':'p','r':'o','s':'i','t':'u','u':'y','v':'t','w':'r','x':'e','y':'w','z':'q','A':'M','B':'N','C':'D','D':'V','E':'C','F':'X','G':'Z','H':'A','I':'S','J':'D','K':'F','L':'G','M':'H','N':'J','O':'K','P':'L','Q':'P','R':'O','S':'I','T':'U','U':'Y','V':'T','W':'R','X':'E','Y':'W','Z':'Q'}


def monoEnc(text):
    result = ""
    for char in text:
        if char.isalpha():
            char = key_dict.get(char)
            result += char
        else:
            result += char
    return result

def DicToString():
    retVal = ""
    for key,val in key_dict.items():
        retVal+=key+":"+val+" "
    return retVal


l = list(string.ascii_lowercase)+list(string.ascii_uppercase)

random.shuffle(l)

result1 = "".join(l)

random.shuffle(l)

result2 = "".join(l)

dictionary = {}

for i in range(len(result1)):
    dictionary[result1[i]] = result2[i]

key_dict = dictionary

parser = argparse.ArgumentParser(description='Cifra un fichero de texto mediante encriptacion monoalfabetica')

parser.add_argument("entrada",help="el nombre del fichero a encriptar", type=str)


parser.add_argument("-o", dest="outputFile", type=str, metavar="salida.txt",help="especifica el nombre del fichero de salida")

args= parser.parse_args()

if args.outputFile == None:
    print("No se han introducido los parametros correctemante: prog desplazamiento entrada -o salida")
    exit()



f = open(args.entrada,"r")
f2= open (args.outputFile,"w")
text = f.read()
text = monoEnc(text)
text =  result1+"\n"+result2+"\n"+text
f2.write(text)