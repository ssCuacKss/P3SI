import sys

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



f = open(sys.argv[1],"r")
text = f.read()
for i in range(26):
    clave = "clave : "+ str(i) + " " + encrypt(text,-i)
    print(clave)