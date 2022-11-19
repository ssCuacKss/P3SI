import sys
import random
import string

key_dict = {'a':'m','b':'n','c':'b','d':'v','e':'c','f':'x','g':'z','h':'a','i':'s','j':'d','k':'f','l':'g','m':'h','n':'j','o':'k','p':'l','q':'p','r':'o','s':'i','t':'u','u':'y','v':'t','w':'r','x':'e','y':'w','z':'q','A':'M','B':'N','C':'D','D':'V','E':'C','F':'X','G':'Z','H':'A','I':'S','J':'D','K':'F','L':'G','M':'H','N':'J','O':'K','P':'L','Q':'P','R':'O','S':'I','T':'U','U':'Y','V':'T','W':'R','X':'E','Y':'W','Z':'Q'}

def value_key(value):
    for key, val in key_dict.items():
        if val == value:
            return key

def monoDec(text):
    result = ""
    for char in text:
        if char.isalpha():
            char = value_key(char)
            result += char
        else:
            result += char
    return result

f = open(sys.argv[1],"r")
f2= open (sys.argv[2],"w")
keys = f.readline()
values = f.readline()

dictionary = {}

for i in range(len(keys)):
    dictionary[keys[i]] = values[i]

key_dict = dictionary

text = f.read()
f2.write(monoDec(text))