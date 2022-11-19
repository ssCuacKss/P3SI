from asyncore import file_dispatcher
import sys
import gzip

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


s = sys.argv[1]
f = open(sys.argv[2],"r")
f2= open (sys.argv[3],"w")
text = f.read()
f2.write(encrypt(text,int(s)))